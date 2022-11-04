import serial, time, datetime, json

class Inverter:
    def __init__( self, serial_device, baud_rate, retry_attempts ):
        self.protocol_version                     = 0
        self.device_serial_number                 = ''
        self.firmware_version                     = 0
        self.ac_output_voltage                    = 0
        self.ac_output_frequency                  = 0
        self.max_ac_charging_current              = 0
        self.battery_under_voltage                = 0
        self.charging_float_voltage               = 0
        self.charging_bulk_voltage                = 0
        self.batter_default_recharge_voltage      = 0
        self.max_charging_current                 = 0
        self.ac_input_voltage_range               = 0
        self.output_source_priority               = ''
        self.charger_source_priority              = ''
        self.battery_type                         = ''
        self.buzzer_disabled                      = 0
        self.enable_power_saving_mode             = 0
        self.enable_overload_restart              = 0
        self.enable_over_temprature_restart       = 0
        self.enable_LCD_backlight                 = 0
        self.enable_alarm_on_primary_source       = 0
        self.enable_fault_code_record             = 0
        self.overload_bypass                      = 0
        self.enable_LCD_default_timeout           = 0
        self.output_mode                          = ''
        self.battery_redischarge_voltage          = 0
        self.pv_ok                                = 0
        self.pv_power_balance                     = 0
        self.current_mode                         = ''
        self.current_grid_voltage                 = 0
        self.current_grid_frequency               = 0
        self.current_ac_output_voltage            = 0
        self.current_ac_output_frequency          = 0
        self.current_ac_output_apparent_power     = 0
        self.current_ac_output_active_power       = 0
        self.current_output_load_percentage       = 0
        self.current_bus_voltage                  = 0
        self.current_battery_voltage              = 0
        self.current_battery_charging_current     = 0
        self.current_battery_capacity_percentage  = 0
        self.current_heat_sink_temprature         = 0
        self.current_pv_input_current_for_battery = 0
        self.current_pv_input_voltage             = 0
        self.current_battery_voltage_from_scc     = 0
        self.current_battery_discharge_current    = 0
        self.current_device_status                = ''
        self.total_energy                         = 0

        self.retry_attempts = retry_attempts
        self.baudrate       = baud_rate
        self.serial_device  = serial_device

        self.last_reset_time  = datetime.datetime.now().isoformat()
        self.last_update_time = 0


    def checkCRC( self, message ):
        #CRC-16-CITT poly the CRC sheme used by ymodem protocol
        poly = 0x1021
        #16bit operation register initialized to zeros
        reg = 0
        #pad the end of the message with the size of the poly
        message += '\x00\x00' 
        #for each bit in the message
        for byte in message:
            mask = 0x80
            while(mask > 0):
                #left shift by one
                reg<<=1
                #input the next bit from the message into the right hand side of the op reg
                if ord(byte) & mask:   
                    reg += 1
                mask>>=1
                #if a one popped out the left of the reg xor reg w/poly
                if reg > 0xffff:            
                    #eliminate any one that popped out the left
                    reg &= 0xffff           
                    #xor with the poly this is the remainder
                    reg ^= poly
        return reg

    def connect( self ):
        self.serial = serial.Serial( self.serial_device, baudrate = self.baudrate, bytesize = serial.EIGHTBITS, parity = serial.PARITY_NONE, stopbits = serial.STOPBITS_ONE, timeout = 2 )

    def close_connection( self ):
        self.serial.close()

    def send_cmd( self, cmd ):
        data_to_send = cmd.encode() + self.checkCRC( cmd ).to_bytes( 2, 'big' ) + b'\r'
        self.connect()
        attemps = 0
        while attemps <= self.retry_attempts:
            attemps += 1
            try:
                self.serial.write( data_to_send )
                response = self.serial.read_until( b'\x0D' )[:-3].decode()
                if '(' == response[0]:
                    data_to_return = response[1::]
                    break
                data_to_return = False
            except:
                data_to_return = False 
            time.sleep( 1 )

        self.close_connection()

        if False is data_to_return:
            raise Exception( 'Failed to communicate with inverter' )
        return data_to_return
        
    def get_serial_number( self ):
        if '' == self.device_serial_number:
            self.device_serial_number = self.send_cmd( 'QID' )
        return self.device_serial_number

    def get_protocol_version( self ):
        if 0 == self.protocol_version:
            self.protocol_version = self.send_cmd( 'QPI' )
        return self.protocol_version
    
    def get_firmware_version( self ):
        if 0 == self.firmware_version:
            self.firmware_version = self.send_cmd( 'QVFW' )
        return self.firmware_version

    def get_current_mode( self ):
        current_mode = self.send_cmd( 'QMODE' )
        modes = {
            'P': 'Power On Mode',
            'S': 'Standby Mode',
            'L': 'Line Mode',
            'B': 'Battery Mode',
            'F': 'Fault Mode',
            'H': 'Power saving Mode',
        }

        self.current_mode = modes[ current_mode ]
        return self.current_mode

    def update_inverter_settings( self ):
        self.get_serial_number()
        self.get_protocol_version()
        self.get_firmware_version()

        battery_types = [
            'AGM',
            'Flooded',
            'Customized',
        ]

        output_source_priority = [
            'Utility first',
            'Solar first',
            'SBU first',
        ]

        charger_source_priority = [
            'Utility first',
            'Solar first',
            'Solar + Utility',
            'Only solar charging permitted',
        ]

        response =self.send_cmd( 'QDI' )
        if response is False:
            raise Exception( 'Failed to get valid response from Inverter' )
        
        data = response.split( ' ' )

        self.ac_output_voltage               = data[0]
        self.ac_output_frequency             = data[1]
        self.max_ac_charging_current         = data[2]
        self.battery_under_voltage           = data[3]
        self.charging_float_voltage          = data[4]
        self.charging_bulk_voltage           = data[5]
        self.batter_default_recharge_voltage = data[6]
        self.max_charging_current            = data[7]
        self.ac_input_voltage_range          = data[8]
        self.output_source_priority          = output_source_priority[ int( data[9] ) ]
        self.charger_source_priority         = charger_source_priority[ int( data[10] ) ]
        self.battery_type                    = battery_types[ int( data[11] ) ]
        self.buzzer_disabled                 = data[12]
        self.enable_power_saving_mode        = data[13]
        self.enable_overload_restart         = data[14]
        self.enable_over_temprature_restart  = data[15]
        self.enable_LCD_backlight            = data[16]
        self.enable_alarm_on_primary_source  = data[17]
        self.enable_fault_code_record        = data[18]
        self.overload_bypass                 = data[19]
        self.enable_LCD_default_timeout      = data[20]
        self.output_mode                     = data[21]
        self.battery_redischarge_voltage     = data[22]
        self.pv_ok                           = data[23]
        self.pv_power_balance                = data[24]

    def update_inverter_status( self ):
        response =self.send_cmd( 'QPIGS' )
        if response is False:
            raise Exception( 'Failed to get valid response from Inverter' )
        
        data = response.split( ' ' )
        self.current_grid_voltage                 = data[0]
        self.current_grid_frequency               = data[1]
        self.current_ac_output_voltage            = data[2]
        self.current_ac_output_frequency          = data[3]
        self.current_ac_output_apparent_power     = data[4]
        self.current_ac_output_active_power       = data[5]
        self.current_output_load_percentage       = data[6]
        self.current_bus_voltage                  = data[7]
        self.current_battery_voltage              = data[8]
        self.current_battery_charging_current     = data[9]
        self.current_battery_capacity_percentage  = data[10]
        self.current_heat_sink_temprature         = data[11]
        self.current_pv_input_current_for_battery = data[12]
        self.current_pv_input_voltage             = data[13]
        self.current_battery_voltage_from_scc     = data[14]
        self.current_battery_discharge_current    = data[15]
        self.current_device_status                = data[16]

        if 0 == self.last_update_time:
            self.last_update_time = datetime.datetime.now()

        watt_seconds          = int( self.current_ac_output_active_power ) * ( datetime.datetime.now() - self.last_update_time ).total_seconds()
        kilowatt_hours        = ( watt_seconds / 3600000 )
        self.last_update_time = datetime.datetime.now()
        self.total_energy     = self.total_energy + kilowatt_hours

        self.get_current_mode()
        
    def json( self ):
        data = {}

        data['protocol_version']                     = self.protocol_version
        data['device_serial_number']                 = self.device_serial_number
        data['firmware_version']                     = self.firmware_version
        data['ac_output_voltage']                    = self.ac_output_voltage
        data['ac_output_frequency']                  = self.ac_output_frequency
        data['max_ac_charging_current']              = self.max_ac_charging_current
        data['battery_under_voltage']                = self.battery_under_voltage
        data['charging_float_voltage']               = self.charging_float_voltage
        data['charging_bulk_voltage']                = self.charging_bulk_voltage
        data['batter_default_recharge_voltage']      = self.batter_default_recharge_voltage
        data['max_charging_current']                 = self.max_charging_current
        data['ac_input_voltage_range']               = self.ac_input_voltage_range
        data['output_source_priority']               = self.output_source_priority
        data['charger_source_priority']              = self.charger_source_priority
        data['battery_type']                         = self.battery_type
        data['buzzer_disabled']                      = self.buzzer_disabled
        data['enable_power_saving_mode']             = self.enable_power_saving_mode
        data['enable_overload_restart']              = self.enable_overload_restart
        data['enable_over_temprature_restart']       = self.enable_over_temprature_restart
        data['enable_LCD_backlight']                 = self.enable_LCD_backlight
        data['enable_alarm_on_primary_source']       = self.enable_alarm_on_primary_source
        data['enable_fault_code_record']             = self.enable_fault_code_record
        data['overload_bypass']                      = self.overload_bypass
        data['enable_LCD_default_timeout']           = self.enable_LCD_default_timeout
        data['output_mode']                          = self.output_mode
        data['battery_redischarge_voltage']          = self.battery_redischarge_voltage
        data['pv_ok']                                = self.pv_ok
        data['pv_power_balance']                     = self.pv_power_balance
        data['current_mode']                         = self.current_mode
        data['current_grid_voltage']                 = self.current_grid_voltage
        data['current_grid_frequency']               = self.current_grid_frequency
        data['current_ac_output_voltage']            = self.current_ac_output_voltage
        data['current_ac_output_frequency']          = self.current_ac_output_frequency
        data['current_ac_output_apparent_power']     = self.current_ac_output_apparent_power
        data['current_ac_output_active_power']       = self.current_ac_output_active_power
        data['current_output_load_percentage']       = self.current_output_load_percentage
        data['current_bus_voltage']                  = self.current_bus_voltage
        data['current_battery_voltage']              = self.current_battery_voltage
        data['current_battery_charging_current']     = self.current_battery_charging_current
        data['current_battery_capacity_percentage']  = self.current_battery_capacity_percentage
        data['current_heat_sink_temprature']         = self.current_heat_sink_temprature
        data['current_pv_input_current_for_battery'] = self.current_pv_input_current_for_battery
        data['current_pv_input_voltage']             = self.current_pv_input_voltage
        data['current_battery_voltage_from_scc']     = self.current_battery_voltage_from_scc
        data['current_battery_discharge_current']    = self.current_battery_discharge_current
        data['current_device_status']                = self.current_device_status
        data['total_energy']                         = self.total_energy
        data['retry_attempts']                       = self.retry_attempts
        data['baudrate']                             = self.baudrate
        data['serial_device']                        = self.serial_device
        data['last_reset_time']                      = self.last_reset_time

        return json.dumps( data )
