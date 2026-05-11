# AP24-Service Manager  

## Description  
Ap24-Service manager include start, stop, restart and stop Apache24 service.  
The main function of this project is to ensure Apache will start hornies with different port.

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
Create this 2 files and place your service name in config folder like example below

**service.conf**
```txt
Apacheservicename2466
```

**database.conf**
```txt
MySQLServiceName123
```

## Info  
.bat file must be running in administrator mode.
This program built for learning and sharing only.

## License  
This project is under MIT License.
