# AP24-Service Manager  

## Description  
Ap24-Service manager include start, stop, restart and stop Apache24 service.  
Also provide custom port every time we start the service configured in main.py. This make the server will use different port every time it start. Will be more secure i think. :')  

## Tools  
python  
bat / cmd  

## Guide  
```
git clone https://<username>:<token>@github.com/almalikzakwan/AP24-Service.git
cd Ap24-service
runas /<user>:Administrator <start>:<stop>:<status>:<restart>.bat
```  

Create **service_name.txt** and place your Apache service name. Also change filepath in start.bat, status.bat and stop.bat .    

Create and place your config file path in **conf_file.py** as example below:  
```python
def file_path():
    return [
        "E:/Apache/httpd-2.4.66-260223-Win64-VS18/Apache24/conf/httpd.conf",
        "E:/Apache/httpd-2.4.66-260223-Win64-VS18/Apache24/conf/extra/httpd-ssl.conf",
        "E:/Apache/httpd-2.4.66-260223-Win64-VS18/Apache24/conf/extra/httpd-vhosts.conf",
        "E:/Apache/httpd-2.4.66-260223-Win64-VS18/Apache24/conf/extra/developments"
    ]
```

## Info  
.bat file must be running in administrator mode.
This program built for learning and sharing only.

## License  
This project is under MIT License.
