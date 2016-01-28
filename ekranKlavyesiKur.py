class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
print(bcolors.FAIL+" \n LUTFEN yeniSite.py dosyasini SUDO izni ile calistirdiginiza emin olunuz  \n"+bcolors.ENDC)
print(bcolors.OKBLUE+" \n LUTFEN yeniSite.py dosyasini SUDO izni ile calistirdiginiza emin olunuz  \n"+bcolors.ENDC)

os.system("sudo apt-get install -y matchbox-keyboard")

print(bcolors.OKGREEN+" matchbox-keyboard kuruldu !\n"+bcolors.ENDC)

metin = """
#!/bin/bash
matchbox-keyboard
"""

import os;
os.getcwd()
VHostDosya = open("/home/pi/Desktop/klavye_calistir.conf", "x")
VHostDosya.write(metin)
VHostDosya.close();

print(bcolors.OKBLUE+"yeni kısayol dosyası masaüstünde olusturuldu !\n"+bcolors.ENDC)
