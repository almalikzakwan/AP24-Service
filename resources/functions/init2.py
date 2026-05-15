import os
import fnmatch, re
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
        confs = conf.developments()
        cfpp = conf.path('config/ports.conf')
        portsf = f(cfpp)
        ports = portsf.readlines()
        conf_ports = {}
        for i, port in enumerate(ports):
            filename = re.sub(r"\{.*?\}|\s+","",port)
            cpath = [item for item in confs if filename in item][0]
            value = re.search(r'\{(.*?)\}', port)
            for item in value.group(1).strip().split(","):
                key, type = item.strip().split(":")
                #todo: port, type, path , read and write into developement config
                #todo: multiple port forwarding, firewall inbound rule.
                nprt = randoms.randint(4430, 65535)
                ports[i] = ports[i].replace(str(key),str(nprt))
                reps = portsf.writelines(ports)
                if reps is not True:
                    print("[Warning] New port cannot been changed.")
                else:
                    rfp = conf.path(f"storage/recent.{type}.port")
                    rfile = f(rfp)
                    rfile.write(f"\n{str(nprt)}")
                    
                 

                    