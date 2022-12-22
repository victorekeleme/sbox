import subprocess
import sys
import json
import os
import shutil
import time
from pathGen import ranPath
from zipper import zipper
import re
import concurrent.futures


#magnet_link = ["magnet:?xt=urn:btih:0A62A7B53706DC91589763FBA8CD431C4371FE53&dn=160+Excel+Exercises+With+Solutions+And+Comments+-+Excel+Workbook&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.open-internet.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2850%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2720%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2810%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2890%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.fatkhoala.org%3A13790%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce", "magnet:?xt=urn:btih:0A62A7B53706DC91589763FBA8CD431C4371FE53&dn=160+Excel+Exercises+With+Solutions+And+Comments+-+Excel+Workbook&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Fopen.stealth.si%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.open-internet.nl%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2850%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2720%2Fannounce&tr=udp%3A%2F%2F9.rarbg.me%3A2810%2Fannounce&tr=udp%3A%2F%2F9.rarbg.to%3A2890%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce&tr=udp%3A%2F%2Ftracker.fatkhoala.org%3A13790%2Fannounce&tr=udp%3A%2F%2Ftracker.opentrackr.org%3A1337%2Fannounce&tr=http%3A%2F%2Ftracker.openbittorrent.com%3A80%2Fannounce&tr=udp%3A%2F%2Fopentracker.i2p.rocks%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.internetwarriors.net%3A1337%2Fannounce&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969%2Fannounce&tr=udp%3A%2F%2Fcoppersurfer.tk%3A6969%2Fannounce&tr=udp%3A%2F%2Ftracker.zer0day.to%3A1337%2Fannounce"]




#magnet_link = str(input("Enter magnet link: "))

# Gets the title of the download
def get_title(magnet_link):
    if str(magnet_link)[:15] != "magnet:?xt=urn:":
        return "Invalid magnet link try again"
    else:
        cmd= []
        #cmd.append("screen")
        #cmd.append("-dm")
        cmd.append("webtorrent")
        cmd.append("info")
        cmd.append(magnet_link)
        try:
            if sys.platform.startswith('linux'):
                fname = json.loads(subprocess.check_output(cmd))['name'] # Gets the name of the file
                return fname
        except Exception as e:
            print(e)


async def handler(magnet_link):
    dtitle = get_title(magnet_link)
    rPath = ranPath()
    done = False

    cmd=[]
    #cmd.append("screen")
    #cmd.append("-dm")
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    cmd.append("-o")
    cmd.append(rPath)
    #cmd.append(">>")
    #cmd.append("~/dev/null")
    try:
        if sys.platform.startswith('linux'):
            print("downloading...please wait")         
            subprocess.call(cmd) #Downloads the file
            done = True
            zipper(rPath,done)
    except Exception as e:
        print(e)
        done = False
    
    link=str(os.listdir(rPath)[0])
    fPath = str(rPath+'/'+link) 

    return f"{fPath}"


#with concurrent.futures.ThreadPoolExecutor() as executor:
#    executor.map(handler, magnet_link)

