import subprocess

class firewall:
    def addInbound(port, action="allow", protocol="TCP", direction="in") -> bool:
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

        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Failed to add rule Apache Custom Port {port}")
            return False
        except Exception as e:
            print(f"An unexpected error occured: {e}")
            return False

    def portForwarding(port, listenport):
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

        try:
            subprocess.run(command, check=True, capture_output=True, text=True)
            return True
        except Exception as e:
            print(f"An unexcepted error occured: {e}")
            return False