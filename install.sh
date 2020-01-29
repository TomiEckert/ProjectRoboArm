# !/bin/bash

sudo cp ./robot-arm.service /etc/systemd/system/robot-arm.service

sudo systemctl enable robot-arm

sudo cp ./pixy.rules /etc/udev/rules.d/pixy.rules

sudo apt update
sudo apt upgrade --yes
sudo apt install python3-pip python3.7 libopenblas-dev libblas-dev m4 cmake cython python3-dev python3-yaml python3-setuptools libatlas-base-dev --yes
python3.7 -m pip install pip
pip3 install flask adafruit-pca9685 numpy
pip3 install torch-1.0.0a0+8322165-cp37-cp37m-linux_armv7l.whl

echo "alias python = 'python3.7'" > ~/.bashrc
sudo reboot
