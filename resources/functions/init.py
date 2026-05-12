import os
from functions.config import config
from functions.file import files as f
from functions.php import php
from functions.random import randoms
from functions.firewall import firewall
from functions.replace import replace as r

class init:
    def init():
        pts = ["default","ssl"]
        for pt in pts:
            # make file path string
            fp = f"../storage/recent.{pt}.port"

            # init file class
            file = f(fp)

            # Validate file existence. else will get recent configured port.
            if not os.path.isfile(fp):
                print(f"[ERROR] File '{fp}' does not exists. Creating '{fp}' with default port...")
                op = "80" if pt == "default" else "443"
                file.write(op)
                print(f"[INFO] '{fp}' file successfully create.")
            else:
                op = file.read()

            # get a random number
            np = randoms.randint(4430, 65536)
            # save random port into file
            file.write(str(np))

            # file or directory that need to change custom port
            # this is my directory that need to change port in Apache24
            # my example for developments was conf/extra/developments, change your path instead in config/development.conf.
            confs = config.path()

            for cf in confs:
                # check if path is file or directory
                if not os.path.isfile(cf):
                    for fn in os.listdir(cf):
                        cfp = os.path.join(cf, fn)
                        if os.path.isdir(cfp):
                            continue
                        r(cfp, op, np)
                else:
                    r(cf, op, np)

            # add firewall rile to allow custom port to be access
            firewall.addInbound(np)
            # port forwarding default and ssl into new custom
            firewall.portForwarding(np, 80 if pt == "default" else 443)

        #configure php
        php.write()