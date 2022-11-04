import paho.mqtt.client as mqtt
from Inverter import Inverter
import json, time, homeassistant, configparser

config = configparser.ConfigParser()
config.read( 'config.ini' )

availability_topic = config['mqtt']['availability_topic']
state_topic        = config['mqtt']['state_topic']
update_interval    = int( config['mqtt']['update_interval'] )
username           = config['mqtt']['username']
password           = config['mqtt']['password']
host               = config['mqtt']['host']
port               = int( config['mqtt']['port'] )

home_assistant_discovery_enabled = int( config['homeassistant']['enable_auto_discovery'] )

mqtt_client = mqtt.Client()
mqtt_client.username_pw_set( username=username, password=password )
mqtt_client.will_set( availability_topic, 'offline', 0, True )
mqtt_client.connect( host, port, 120 )

inverter_serial_device = config['inverter']['serial_device']
inverter_baud_rate     = int( config['inverter']['baud_rate'] )
inverter_rety_attempts = int( config['inverter']['retry_attempts'] )
inverter_manufacturer  = config['inverter']['manufacturer']
inverter_model         = config['inverter']['model']

home_assistant_discovery_topic = config['homeassistant']['home_assistant_discovery_topic']

inverter = Inverter( inverter_serial_device, inverter_baud_rate, inverter_rety_attempts )
inverter.update_inverter_settings()

def update_inverter_data( topic, delay ):
    while True:
        try:
            inverter.update_inverter_status()
            inverter_json = inverter.json()
            mqtt_client.publish( availability_topic, 'online', 0, True )
            mqtt_client.publish( topic, inverter_json, 0, True )
            time.sleep( delay )
        except:
            print( 'error' )

if __name__ == '__main__':
    if home_assistant_discovery_enabled == 1:
        sensors = homeassistant.generate_mqtt_sensors( inverter, availability_topic, state_topic, home_assistant_discovery_topic, inverter_manufacturer, inverter_model )
        for sensor in sensors:
            mqtt_client.publish( sensor['topic'], json.dumps( sensor['data'] ), 0, True )

    update_inverter_data( state_topic, update_interval )