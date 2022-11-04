#! /bin/bash
echo "Installing InvertMQTT"
mkdir /usr/InverterMQTT/
cp *.py /usr/InverterMQTT/
cp *.ini /usr/InverterMQTT/ -n
cp *.txt /usr/InverterMQTT/
pip3 install -r requirements.txt
cp inverterMQTT.service /etc/systemd/system/inverterMQTT.service
systemctl daemon-reload
systemctl enable inverterMQTT.service
echo "Installation Complete"
