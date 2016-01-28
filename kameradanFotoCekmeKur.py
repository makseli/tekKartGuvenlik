#!/usr/bin/env python
# -*- coding: utf-8 -*- 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
print(bcolors.FAIL+" \n LUTFEN bu dosyayı SUDO izni ile calistirdiginiza emin olunuz  \n"+bcolors.ENDC)
print(bcolors.OKBLUE+" \n LUTFEN bu dosyayı SUDO izni ile calistirdiginiza emin olunuz  \n"+bcolors.ENDC)

import os;
os.system("sudo apt-get install -y fswebcam")

print(bcolors.OKGREEN+" \n \n fswebcam kuruldu !\n"+bcolors.ENDC)

metin = """
#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M%S")
fswebcam -r 1280x720 --no-banner /home/pi/Desktop/$DATE.jpg
"""


os.getcwd()
VHostDosya = open("/home/pi/Desktop/tekFotoCek.sh", "w")
VHostDosya.write(metin)
VHostDosya.close();

os.system("sudo chmod +x /home/pi/Desktop/tekFotoCek.sh ")

print(bcolors.OKBLUE+" \n yeni kısayol dosyası masaüstünde olusturuldu ! \n \n"+bcolors.ENDC)
exit();
