# InverterMQTT
This is a basic python script that will query your MPP-Solar inverter for its status and post that to an MQTT server. A Home Assistant auto discovery is also available to allow this status to be available within Home Assistant

## Installation
### Requirements:
* Python3
* PIP3
* Python VENV

You can install these quickly with:
`sudo apt update;sudo apt install python3 python3-pip python3-venv -y`

### Steps to Install
* Clone the repo .
* `cd` to the directory you cloned the repo to.
* Run the install bash script ( `sudo bash install.sh` )
  * This script copies the content of the repo to `/usr/InverterMQTT` and copies the service file to the `/etc/systemd/system/` directory
  * Installs the required python packages using the pip3. ( see `requirements.txt` )
  * It then enables the service to auto start on boot.
* open the config file to configure the set-up to match your systems details.
  * `/usr/InvertMQTT/congif.ini`
  * Make sure the MQTT username, password and host are set correctly
  * Configure the invertes serial device ( This will be `/dev/tty*` ). This is the serial port connected to the inverter.
  * Configure the inverters manufacture and model. These are only used as part of the Home Assistant device configuration and can be set to anything you like.
* Finally start the program by running `sudo service inverterMQTT start`
  * you can check the status of the program by running `sudo service inverterMQTT status` to confirm it is running.
