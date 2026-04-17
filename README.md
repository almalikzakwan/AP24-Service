# AP24-Service Manager  

## Description  
Ap24-Service manager include start, stop, restart and stop Apache24 service.  
Also provide custom port every time we start the service configured in main.py. This make the server will use different port every time it start. Will be more secure i think. :')  

## Tools  
python  
bat / cmd  

## Guide  
git clone / place this repo along side with Apache24 folder (httpd-{version} folder)
```
git clone https://<username>:<token>@github.com/almalikzakwan/AP24-Service.git
cd Ap24-service
runas /<user>:Administrator <start>:<stop>:<status>:<restart>.bat
```  

Create **service_name.txt** and place your service name there like example below

```txt
Apacheservicename2466
```

Create and place your config file path in **conf_file.py** as example below:  
```python
import os

def file_path():
    cwd = os.getcwd()
    path = f"{cwd.replace("\\","/")}/../Apache24"

    return [
        f"{path}/conf/httpd.conf",
        f"{path}/conf/extra/httpd-ssl.conf",
        f"{path}/conf/extra/httpd-vhosts.conf",
        f"{path}/conf/extra/developments"
    ]
```

## Info  
.bat file must be running in administrator mode.
This program built for learning and sharing only.

## License  
This project is under MIT License.
