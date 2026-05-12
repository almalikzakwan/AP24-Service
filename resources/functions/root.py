import os

class root:
    def __init__(self):
        self.cwd = os.getcwd()

    def ApachePath(self):
        return f"{self.cwd.replace("\\","/")}/../../Apache24"
    
    def AP24Path(self):
        return f"{self.cwd.replace("\\","/")}/../"