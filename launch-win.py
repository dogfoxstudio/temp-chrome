import string
import random
import os
import subprocess
from string import Template

from sys import argv

def launch(name):
    settings = open('./profiles/'+name+'/settings.txt', "r")
    settings.readline()
    useragent = settings.readline()[:-2]
    proxy = settings.readline()
    settings.close()
    print("UserAgent:"+useragent)
    print("proxy: "+proxy)
    subprocess.run([
        "chrome-win/chrome", \
        "--user-data-dir="+'./profiles/'+name,\
        "--load-extension=../extensions/ext1,../extensions/ext2,../extensions/ext3,../extensions/ext4",\
        "--proxy-server="+proxy,\
        "--user-agent="+useragent, \
        "google.com"
    ]) 
    
greetings_template = Template("""
<!DOCTYPE html>
<html>
<head>

<title>
Профиль ${profilename}</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Прокси:${prx}, UserAgent:${UA}">

</head>
<body>
<h1>Это профиль ${profilename}</h1>
<h1>Используется прокси ${prx}</h1>
<h1>и UserAgent ${UA}</h1>
</body>
</html>
""")

def createprofile(name):
    #создание каталога профиля
    if not os.path.exists('./profiles/'+name):
        os.makedirs('./profiles/'+name)
    #создание файла настроек
    settings = open('./profiles/'+name+'/settings.txt', "w")
    settings.write(name+"\n")
    #выбор UserAgent
    useragent = random.choice(open('useragents.txt').readlines())
    settings.write(useragent)
    #выбор прокси
    proxy = random.choice(open('proxies.txt').readlines())
    settings.write(proxy)
    with open("proxies.txt", "r") as prx:
        lines = prx.readlines()
    with open("proxies.txt", "w") as prx:
        for line in lines:
            if proxy not in line:
                prx.write(line)
    #выбор часового пояса
        #потом доделаю
    settings.close()
    #создание файла запуска
    launcher = open("./launchers/profile_"+name+".bat", "w")
    launcher.write("cd .. \n")
    launcher.write("python ./launch.py "+name)
    launcher.close()
    #создание окна
    greet = open('./profiles/'+name+'/greetings.html', "w")
    greet.write(greetings_template.safe_substitute( prx=proxy,profilename=name,UA=useragent
        ))
    

if len(argv) >1:
    profilename = argv[1]
else:
    profilename = "".join(random.choice(string.ascii_letters) for x in range(6))

profiles = os.listdir('./profiles/')

if profilename in profiles:
    print("Profile " + profilename + " exists")
    print("Launching ...")
    launch(profilename)
else:
    print("Creating new profile: "+profilename)
    createprofile(profilename)
    print("Launching ...")
    launch(profilename)
    
