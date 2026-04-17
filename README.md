# AP24-Service Manager  

## Description  
Ap24-Service manager include start, stop, restart and stop Apache24 service.  
Also provide custom port every time we start the service configured in main.py. This make the server will use different port every time it start. Will be more secure i think. :')  

## Tools 
windows 
python  
bat / cmd

## Guide  
git clone / place this repo alongside with Apache24 folder (httpd-{version} folder)
```
git clone https://<username>:<token>@github.com/almalikzakwan/AP24-Service.git
cd Ap24-service
runas /<user>:Administrator <start>:<stop>:<status>:<restart>.bat
```  

Create **service_name.txt** and place your service name at root path like example below

```txt
Apacheservicename2466
```

## Info  
.bat file must be running in administrator mode.
This program built for learning and sharing only.

## License  
This project is under MIT License.
