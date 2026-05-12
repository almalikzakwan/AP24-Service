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

Create this 4 config files and place your file name in the folder like example below,

**_service.conf_**
```txt
Apacheservicename2466
```

**_database.conf_**
```txt
MySQLServiceName123
```

**_php.conf_**
```txt
Z:/PHP/php-8.3.30-Win32-vs16-x64
```

**_development.conf_**
```txt
# developments folder from Apache24 root path
Apache24/conf/extra/developments
```

example available in config folder.

## Info  
.bat file must be running in administrator mode.
This program built for learning and sharing only.

## License  
This project is under MIT License.
