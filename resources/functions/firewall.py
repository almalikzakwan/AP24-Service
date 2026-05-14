import subprocess

class firewall:
    """
    Class to use network shell windows 11
    """
    def addInbound(self, port:str, action:str="allow", protocol:str="TCP", direction:str="in") -> bool:
        """
        Adds an inbound firewall rule to the Windows Firewall.
        If not add, windows will not allow custom port to be access.
        """
        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "add",
            "rule",
            f"name=Apache Custom Port {port}",
            f"dir={direction}",
            f"action={action}",
            f"protocol={protocol}",
            f"localport={port}"
        ]
        self.run(command, port)

    def portForwarding(self, port:str, listenport:str) -> bool:
        """
        port forwarding for default and ssl port
        forwarding 80 and 443 into custom port.
        port = {new port}, listenport = 80/443
        """
        command = [
            "netsh",
            "interface",
            "portproxy",
            "add",
            "v4tov4",
            f"listenport={listenport}",
            "listenaddress=0.0.0.0",
            f"connectport={port}",
            "connectaddress=127.0.0.1"
        ]
        self.run(command, port)
        
    def delInbound(self, port:str) -> bool:
        """ 
        delete inbound firewall rules. only took 5 latest port to remove.
        """
        command = [
            "netsh",
            "advfirewall",
            "firewall",
            "delete",
            "rule",
            f"name=Apache Apache Custom Port {port}"
        ]

        self.run(command, port)
        
    def run(self, command:str = [], port:int = 80) -> bool:
        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to delete rule Apache Custom Port {port}")
            return False
        except Exception as e:
            print(f"An unexpected error occured: {e}")
            return False