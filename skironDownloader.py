import subprocess
# OR USE CRONJOBS 
import time
from datetime import date


def wgetFunction(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE, 
        stderr = subprocess.PIPE,
        text = True, 
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass


# Textual month, day and our custom year
today = date.today()
date = today.strftime("%d%m%y")

links=[]
links.append('https://openskiron.org/gribs_skiron/Aegean_SKIRON_'+ date +'.grb.bz2')
links.append('https://openskiron.org/gribs_skiron/Crete_SKIRON_'+ date +'.grb.bz2')
links.append('https://openskiron.org/gribs_skiron/Cyprus_SKIRON_'+ date +'.grb.bz2')
links.append('https://openskiron.org/gribs_skiron/Ionian_SKIRON_'+ date +'.grb.bz2')

with open("SkironLinks.txt", "w") as f:
    for link in links:
        f.write(str(link) +"\n")

while(True): 
    for url in links:
        # wget.download(url)
        wgetFunction("wget --timestamping " + url, verbose = True)
        # wget("wget --timestamping -i " + SkironLinks.txt, verbose = True)
    time.sleep(60*60*3) 

