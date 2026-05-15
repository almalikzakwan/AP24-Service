import os
import re
from functions.config import config
from functions.file import files as f
from functions.php import php
from functions.random import randoms
from functions.firewall import firewall
from functions.replace import replace as r
from functions.root import root
import ast

class kickoff:
    def init():
        conf = config()

        cfpp = conf.ports()
        portsf = f(cfpp)
        ports = portsf.readlines()
        conf_ports = {}
        for port in ports:
            ctext = re.sub(r"\{.*?\}|\s+","",port)
            cport = re.search(r'\{(.*?)\}', port)
            iprts = {}
            for item in cport.group(1).strip().split(","):
                key, value = item.strip().split(":")
                iprts[key] = value

            conf_ports[ctext] = iprts
        
        confs = conf.developments()
        #todo:  oldport, read, replace and write
        rt = root()
        for i, cf in enumerate(confs):
            # developements folder
            if not os.path.isfile(cf):
                for fn in os.listdir(cf):
                    cfp = os.path.join(cf, fn)
                    if os.path.isdir(cfp):
                        continue
                    fi = f(cfp)
                    value = fi.read()

                    # print(value)
            else:
                fn = os.path.basename(cf)
                oprts = conf_ports[fn]
                # oprts = {'80': 'default', '443': 'ssl'}
                for oprt, type in oprts.items():
                    nprt = randoms.randint(4430, 65535)
                    ports[i] = ports[i].replace(str(oprt),str(nprt))
                    print(ports[i])
                    reps = portsf.writelines(ports)
                    if reps != True:
                        print(f"[INFO] Port cannot being change. An Error Occured. File: {cfpp}, Line: {i}")
                #todo: save recent port into storage/recent.[default/ssl].port
                #todo: multiple port forwarding, firewall inbound rule. 

                    