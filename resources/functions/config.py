from functions.root import root as r
from functions.file import files as f

class config:
    """ return path of config files """
    def __init__(self):
        self.rt = r()
        self.AP24Path = self.rt.AP24Path()

    def developments(self, dp: str = "config/development.conf") -> tuple:
        """
        file that need to change port
        change with your folder instead (my example was conf/extra/developments folder) 
        """
        files = f(f"{self.AP24Path}/{dp}")
        developments = files.read()

        APPath = self.rt.ApachePath()
        return [
            f"{APPath}/conf/httpd.conf",
            f"{APPath}/conf/extra/httpd-ssl.conf",
            f"{APPath}/conf/extra/httpd-vhosts.conf", 
            f"{APPath}/{developments}"
        ]
    
    def ports(self, dp:str = "config/ports.conf"):
        """ return config/ports.conf """
        return f"{self.AP24Path}/{dp}"