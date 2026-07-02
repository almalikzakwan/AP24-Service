import os
import re
from functions.root import root as r
from functions.file import files as f

class config:
    """ return path of config files """
    def __init__(self):
        self.rt = r()
        self.ApachePath = self.rt.ApachePath()
        self.AP24Path = self.rt.AP24Path()
    
    def developments(self, dp: str = "/config/development.conf") -> tuple:
        """
        file that need to change port
        change with your folder instead (my example was conf/extra/developments folder) 
        """
        
        APPath = self.ApachePath
        path = [
            f"{APPath}/conf/httpd.conf",
            f"{APPath}/conf/extra/httpd-ssl.conf",
            f"{APPath}/conf/extra/httpd-vhosts.conf",
        ]
        files = f(self.path(dp))
        developments = files.read()
        rank = 2
        for fn in os.listdir(f"{APPath}/{developments}"):
            rank += 1
            cfp = os.path.join(f"{APPath}/{developments}", fn).replace("\\","/")
            path.append(cfp)
            pathlength = len(path)
            confports = self.path("/config/ports.conf")
            cfiles = f(confports)
            lines = cfiles.readlines()
            if pathlength > len(lines):
                string = re.sub(r"httpd-vhosts.conf", fn, lines[2])
                reps = cfiles.write(f"{string}")
                if reps is not True:
                    print(f"Config name cannot be added into ports.conf -> Config: {fn}")
        
        return path
    
    #fix: must be duplicated code. clean needed
    def path(self, dp:str):
        """ return path from given path """
        return f"{self.AP24Path}/{dp}"