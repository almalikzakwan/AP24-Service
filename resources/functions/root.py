import os

class root:
    def path():
        cwd = os.getcwd()
        return f"{cwd.replace("\\","/")}/../../../Apache24"