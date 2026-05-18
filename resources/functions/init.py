import os
import fnmatch, re
from functions.config import config
from functions.file import files as f
from functions.php import php
from functions.random import randoms
from functions.firewall import firewall
from functions.replace import replace as r
import traceback

class kickoff:
    """ initialization for main kickoff """
    def init():
        try:
            conf = config()
            confs = conf.developments()
            cfpp = conf.path('/config/ports.conf')
            portsf = f(cfpp)
            rports = portsf.readlines()
            dnprt = randoms.randint(4430, 65535)
            snprt = randoms.randint(4430, 65535)
            fwll = firewall()
            for i, path in enumerate(confs):
                fn = os.path.basename(path)
                ports = [item for item in rports if fn in item][0].strip()
                port = re.search(r"\{(.*?)}",ports)
                for item in port.group(1).strip().split(","):
                    oprt, type = item.strip().split(":")
                    nprt = dnprt if type == "default" else snprt
                    rports[i] = rports[i].replace(str(oprt),str(nprt))
                    reps = portsf.writelines(rports)
                    if reps is not True:
                        print("[Warning] New port cannot been change in config/ports.conf")
                    else:
                        rfp = conf.path(f"/storage/recent.{type}.port")
                        rfile = f(rfp)
                        rfile.write(f"{str(nprt)}\n")

                    r.string(path, str(oprt), str(nprt))
                    
                    fwll.addInbound(port = nprt)
                    if i == 0 or i == 1:
                        fwll.portForwarding(nprt, 80 if type == "default" else 443)

            php.write()

        except Exception as e:
            print(f"[ERROR] {traceback.print_exc()}")
                 

                    