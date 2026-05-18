import os
import fnmatch, re
from functions.config import config
from functions.file import files as f
from functions.php import php
from functions.random import randoms
from functions.firewall import firewall
from functions.replace import replace as r
from functions.root import root
import traceback

class kickoff:
    def init():
        try:
            conf = config()
            confs = conf.developments()
            cfpp = conf.path('/config/ports.conf')
            portsf = f(cfpp)
            rports = portsf.readlines()

            for i, path in enumerate(confs):
                fn = os.path.basename(path)
                ports = [item for item in rports if fn in item][0].strip()
                port = re.search(r"\{(.*?)}",ports)
                for item in port.group(1).strip().split(","):
                    oprt, type = item.strip().split(":")
                    nprt = randoms.randint(4430, 65535)
                    #todo: port, type, path , read and write into developement config
                    #todo: multiple port forwarding, firewall inbound rule.
                    rports[i] = rports[i].replace(str(oprt),str(nprt))
                    reps = portsf.writelines(rports)
                    if reps is not True:
                        print("[Warning] New port cannot been change in config/ports.conf")
                    else:
                        rfp = conf.path(f"/storage/recent.{type}.port")
                        rfile = f(rfp)
                        rfile.write(f"{str(nprt)}\n")

                    r.string(path, str(oprt), str(nprt))
                    

                    
                            

        except Exception as e:
            print(f"[ERROR] {traceback.print_exc()}")
                 

                    