#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
print(bcolors.FAIL+" \n LUTFEN bu dosyayı SUDO izni ile calistirdiginiza emin olunuz. ( Whezy sürümü önerilir )  \n"+bcolors.ENDC)
print(bcolors.OKBLUE+" \n LUTFEN bu dosyayı SUDO izni ile calistirdiginiza emin olunuz. ( Whezy sürümü önerilir )  \n"+bcolors.ENDC)

import os;
os.system("sudo apt-get install -y motion")

print(bcolors.OKGREEN+" \n \n motion kuruldu !\n"+bcolors.ENDC)

os.system("sudo mv /etc/motion/motion.conf /etc/motion/motion.conf_old ")
os.system("sudo mv /etc/default/motion /etc/default/motion_old ")

os.system("sudo cp motion.conf /etc/motion/motion.conf ")


metin = """
# set to 'yes' to enable the motion daemon
start_motion_daemon=yes
"""

os.getcwd()
VHostDosya = open("/etc/default/motion", "w")
VHostDosya.write(metin)
VHostDosya.close();

os.system("sudo service motion start")

print(bcolors.OKBLUE+" \n servis ve konfigürasyon ayarlama işlemi tamam ! \n \n"+bcolors.ENDC)
exit();
