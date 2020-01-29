# !/bin/bash

sudo systemctl disable robot-arm

sudo rm /etc/systemd/system/robot-arm.service

sudo rm /etc/udev/rules.d/pixy.rules

#pip3 uninstall flask torch adafruit-pca9685
#sudo apt remove python3-pip python3.7 --yes

sudo reboot
