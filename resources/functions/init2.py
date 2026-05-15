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
            utext = re.sub(r'[\t\[\]\n]', '', str(port))
            ctext = re.sub(r'[,\d]','',utext).strip()
            cport = re.findall(r'\d+',port)
            conf_ports[f"{ctext}"] = f"{cport}"

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
                oprts = ast.literal_eval(conf_ports[fn])
                #todo: save port with filename and replace port in config file
                print(oprts)
                for oprt in oprts:
                    print(oprt)
                    nprt = randoms.randint(4430, 65535)
                    rs = r.line(cfpp, i, str(oprt), str(nprt))
                    if rs != True:
                        print(f"[INFO] Port cannot being change. An Error Occured. File: {cfpp}, Line: {i}")
                    # file.write()

                    