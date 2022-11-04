from Inverter import Inverter

def generate_mqtt_sensors( inverter, availability_topic, state_topic, home_assistant_discovery_topic, manufacturer, model ):
    unique_id = inverter.get_serial_number()
    node_id = unique_id

    sensors = [
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/protocol_version/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Protocol Version",
                "state_topic": state_topic,
                "unique_id": unique_id + '_protocol_version',
                "value_template": "{{value_json.protocol_version}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
 
            } 
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/device_serial_number/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Device Serial Number",
                "state_topic": state_topic,
                "unique_id": unique_id + '_device_serial_number',
                "value_template": "{{value_json.device_serial_number}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/firmware_version/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Firmware Version",
                "state_topic": state_topic,
                "unique_id": unique_id + '_firmware_version',
                "value_template": "{{value_json.firmware_version}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/ac_output_voltage/config',
            'data': {
                "device_class": "voltage",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "AC Output Voltage",
                "unit_of_measurement": "V",
                "state_topic": state_topic,
                "unique_id": unique_id + '_ac_output_voltage',
                "value_template": "{{value_json.ac_output_voltage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/ac_output_frequency/config',
            'data': {
                "device_class": "frequency",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "AC Output Frequency",
                "unit_of_measurement": "Hz",
                "state_topic": state_topic,
                "unique_id": unique_id + '_ac_output_frequency',
                "value_template": "{{value_json.ac_output_frequency}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/max_ac_charging_current/config',
            'data': {
                "device_class": "current",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Max AC Charging Current",
                "unit_of_measurement": "A",
                "state_topic": state_topic,
                "unique_id": unique_id + '_max_ac_charging_current',
                "value_template": "{{value_json.max_ac_charging_current}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/battery_under_voltage/config',
            'data': {
                "device_class": "voltage",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Battery Under Voltage",
                "unit_of_measurement": "V",
                "state_topic": state_topic,
                "unique_id": unique_id + '_battery_under_voltage',
                "value_template": "{{value_json.battery_under_voltage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/charging_float_voltage/config',
            'data': {
                "device_class": "voltage",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Charging Float Voltage",
                "unit_of_measurement": "V",
                "state_topic": state_topic,
                "unique_id": unique_id + '_charging_float_voltage',
                "value_template": "{{value_json.charging_float_voltage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/output_source_priority/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Output Source Priority",
                "state_topic": state_topic,
                "unique_id": unique_id + '_output_source_priority',
                "value_template": "{{value_json.output_source_priority}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/charger_source_priority/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Charger Source Priority",
                "state_topic": state_topic,
                "unique_id": unique_id + '_charger_source_priority',
                "value_template": "{{value_json.charger_source_priority}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/battery_type/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Battery Type",
                "state_topic": state_topic,
                "unique_id": unique_id + '_battery_type',
                "value_template": "{{value_json.battery_type}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/pv_ok/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "PV Ok",
                "state_topic": state_topic,
                "unique_id": unique_id + '_pv_ok',
                "value_template": "{{value_json.pv_ok}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
                 } },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/pv_power_balance/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "PV Power Balance",
                "state_topic": state_topic,
                "unique_id": unique_id + '_pv_power_balance',
                "value_template": "{{value_json.pv_power_balance}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_mode/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Mode",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_mode',
                "value_template": "{{value_json.current_mode}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_grid_voltage/config',
            'data': {
                "device_class": "voltage",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Grid Voltage",
                "unit_of_measurement": "V",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_grid_voltage',
                "value_template": "{{value_json.current_grid_voltage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_grid_frequency/config',
            'data': {
                "device_class": "frequency",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Grid Frequency",
                "unit_of_measurement": "Hz",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_grid_frequency',
                "value_template": "{{value_json.current_grid_frequency}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_ac_output_voltage/config',
            'data': {
                "device_class": "voltage",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current AC Output Voltage",
                "unit_of_measurement": "V",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_ac_output_voltage',
                "value_template": "{{value_json.current_ac_output_voltage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_ac_output_frequency/config',
            'data': {
                "device_class": "frequency",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current AC Output Frequency",
                "unit_of_measurement": "Hz",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_ac_output_frequency',
                "value_template": "{{value_json.current_ac_output_frequency}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_ac_output_apparent_power/config',
            'data': {
                "device_class": "apparent_power",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current AC Output Apparent Power",
                "unit_of_measurement": "VA",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_ac_output_apparent_power',
                "value_template": "{{value_json.current_ac_output_apparent_power}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_ac_output_active_power/config',
            'data': {
                "device_class": "power",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current AC Output Active Power",
                "unit_of_measurement": "W",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_ac_output_active_power',
                "value_template": "{{value_json.current_ac_output_active_power}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_output_load_percentage/config',
            'data': {
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Output Load Percentage",
                "unit_of_measurement": "%",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_output_load_percentage',
                "value_template": "{{value_json.current_output_load_percentage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_battery_voltage/config',
            'data': {
                "device_class": "voltage",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Battery Voltage",
                "unit_of_measurement": "V",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_battery_voltage',
                "value_template": "{{value_json.current_battery_voltage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_battery_charging_current/config',
            'data': {
                "device_class": "current",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Battery Charging Current",
                "unit_of_measurement": "A",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_battery_charging_current',
                "value_template": "{{value_json.current_battery_charging_current}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_battery_capacity_percentage/config',
            'data': {
                "device_class": "battery",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Battery Capacity Percentage",
                "unit_of_measurement": "%",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_battery_capacity_percentage',
                "value_template": "{{value_json.current_battery_capacity_percentage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_pv_input_voltage/config',
            'data': {
                "device_class": "voltage",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current PV Input Voltage",
                "unit_of_measurement": "V",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_pv_input_voltage',
                "value_template": "{{value_json.current_pv_input_voltage}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_battery_discharge_current/config',
            'data': {
                "device_class": "current",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Battery Discharge Current",
                "unit_of_measurement": "A",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_battery_discharge_current',
                "value_template": "{{value_json.current_battery_discharge_current}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/current_device_status/config',
            'data': {
                "device_class": "current",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Current Device Status",
                "unit_of_measurement": "A",
                "state_topic": state_topic,
                "unique_id": unique_id + '_current_device_status',
                "value_template": "{{value_json.current_device_status}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
            }
        },
        {
            'topic': home_assistant_discovery_topic + '/sensor/' + node_id + '/total_energy/config',
            'data': {
                "device_class": "energy",
                "device": {
                    "name": "Inverter",
                    "model": model,
                    "manufacturer": manufacturer,
                    "identifiers": unique_id,
                    "sw_version": inverter.get_firmware_version(),
                },
                "name": "Total Energy",
                "unit_of_measurement": "kWh",
                "state_topic": state_topic,
                "unique_id": unique_id + '_total_energy',
                "value_template": "{{value_json.total_energy}}",
                "availability": {
                    "topic": availability_topic,
                    "payload_available": "online",
                    "payload_not_available": "offline"
                },
                "state_class": "total",
                "last_reset_value_template": "{{value_json.last_reset_time}}",
            }
        },
    ]

    return sensors


