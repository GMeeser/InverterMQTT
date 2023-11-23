#! /bin/bash
echo "Installing InvertMQTT"
mkdir /usr/InverterMQTT/
cp *.py /usr/InverterMQTT/
cp *.ini /usr/InverterMQTT/ -n
cp *.txt /usr/InverterMQTT/
chmod 777 /usr/InverterMQTT -R
cd /usr/InverterMQTT
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
deactivate
cp inverterMQTT.service /etc/systemd/system/inverterMQTT.service
systemctl daemon-reload
systemctl enable inverterMQTT.service
echo "Installation Complete"
