import os
from functions.config import config
from functions.file import files as f
from functions.php import php
from functions.random import randoms
from functions.firewall import firewall
from functions.replace import replace as r
from functions.root import root

class kickoff:
    def init():
        confs = config.path()
        for cf in confs:
            print(cf)
