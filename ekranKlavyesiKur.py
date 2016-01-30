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
os.system("sudo apt-get update")
os.system("sudo apt-get install -y matchbox-keyboard")

print(bcolors.OKGREEN+" \n \n matchbox-keyboard kuruldu !\n"+bcolors.ENDC)

metin = """
#!/bin/bash
matchbox-keyboard
"""


os.getcwd()
VHostDosya = open("/home/pi/Desktop/klavye_calistir.sh", "w")
VHostDosya.write(metin)
VHostDosya.close();

os.system("sudo chmod +x /home/pi/Desktop/klavye_calistir.sh ")

print(bcolors.OKBLUE+" \n yeni kısayol dosyası masaüstünde olusturuldu ! \n \n"+bcolors.ENDC)
exit();
