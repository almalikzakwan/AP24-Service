import os
import subprocess
import random

#recent default port file
recent_default_port_path = "recent.default.port"
# get latest configured random default port.
ordp = open(recent_default_port_path,"r")
default_old_port = ordp.read()
ordp.close()
#get new default random port
default_random_port = random.randrange(80,8000,1)
# save random default port into file.
rdp = open(recent_default_port_path,"w")
rdp.write(str(default_random_port))

# recent ssl port file
recent_ssl_port_path = "recent.ssl.port"
# get latest configured random ssl port.
orsp = open(recent_ssl_port_path,"r")
ssl_old_port = orsp.read()
orsp.close()
# get random ssl port.
ssl_random_port = random.randrange(443,6000,1)
# save random ssl port into file.
rsp = open(recent_ssl_port_path,"w")
rsp.write(str(ssl_random_port))

def setup_default_port(file_path, new_port, old_port, vhosts_port_line):
    # read config file D:\Project\Apache\Apache24\conf\extra\httpd-vhosts.conf.
    o = open(file_path, "r")
    lines = o.readlines()
    o.close()

    lines[vhosts_port_line - 1] = lines[vhosts_port_line - 1].replace(str(old_port),str(new_port))
    with open(file_path, "w") as vhosts_file:
        vhosts_file.writelines(lines)

def add_windows_firewall_rule(port, action="allow", protocol="TCP", direction="in"):
    """
    Adds an inbound firewall rule to the Windows Firewall.
    """
    command = [
        "netsh",
        "advfirewall",
        "firewall",
        "add",
        "rule",
        f"name=Apache2D Port {port}",
        f"dir={direction}",
        f"action={action}",
        f"protocol={protocol}",
        f"localport={port}"
    ]

    try:
        subprocess.run(command, check=True, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to add rule Apache2D Port {port}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

def port_forwarding(port, listenport):
    """
    port forwarding for default and ssl port
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
    except Exception as e:
        print(f"An unexcepted error occured: {e}")

def write_to_files(port, op, port_lines):
    """
    Rewrite port number in developments folder
    """
    devs_path = "D:/Project/Apache/Apache24/conf/extra/developments/"
    
    # Validate folder path
    if not os.path.exists(devs_path):
        print(f"[WARN] Folder developments does not found")
        return 
    
    # check if developemtn isn ot directory
    if not os.path.isdir(devs_path):
        print(f"[WARN] Folder developments is not a directory")
        return

    # foreach write random port for all files in development folder.
    for filename in os.listdir(devs_path):
        file_path = os.path.join(devs_path, filename)
        if os.path.isdir(file_path):
            continue
        o = open(file_path, "r")
        lines = o.readlines()
        o.close()
        
        try:
            lines[port_lines -1] = lines[port_lines - 1].replace(str(op),str(port))
            with open(file_path, "w") as f:
                f.writelines(lines)
        except (OSError, IOError) as e:
            print(f"Error on writing port in {file_path}: {e}")

# configuration for httpd.conf and httpd-ssl.conf
httpd_file_path = "D:/Project/Apache/Apache24/conf/httpd.conf"
httpd_lines = [60, 239]
for httpd_line in httpd_lines:
    setup_default_port(httpd_file_path, default_random_port, default_old_port, httpd_line)

httpd_ssl_file_path = "D:/Project/Apache/Apache24/conf/extra/httpd-ssl.conf"
httpd_ssl_lines = [36, 121, 125]
for httpd_ssl_line in httpd_ssl_lines:
    setup_default_port(httpd_ssl_file_path, ssl_random_port, ssl_old_port, httpd_ssl_line)

# configuration for default localhost: httpd-vhosts.conf
default_file_path = "D:/Project/Apache/Apache24/conf/extra/httpd-vhosts.conf"
setup_default_port(default_file_path, default_random_port, default_old_port, 25)
setup_default_port(default_file_path, ssl_random_port, ssl_old_port, 36)

# configuration for development config
write_to_files(default_random_port, default_old_port, 6)
write_to_files(ssl_random_port, ssl_old_port, 17)

# windows configuration for default_port
add_windows_firewall_rule(default_random_port)
port_forwarding(default_random_port, 80)
# windows configuration for ssl_random_port  
add_windows_firewall_rule(ssl_random_port)
port_forwarding(ssl_random_port, 443)

print("[PY INFO] DONE!")



