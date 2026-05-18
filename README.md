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

Create this config files and place your file name in the folder like example below,

**_AP24-Service/config/service.conf_**
```txt
Apacheservicename2466
```

**_AP24-Service/config/database.conf_**
```txt
MySQLServiceName123
```

**_AP24-Service/config/php.conf_**
```txt
Z:/PHP/php-8.3.30-Win32-vs16-x64
```

**_AP24-Service/config/development.conf_**
```txt
# developments folder from Apache24 root path
conf/extra/developments
```

**_AP24-Service/config/ports.conf_**
```txt
httpd.conf {80:default}
httpd-ssl.conf {443:ssl}
httpd-vhosts.conf {80:default,443:ssl}
```

**_Apache24/config/php.conf_**
```txt
LoadFile "Z:/PHP/php-8.3.30-Win32-vs16-x64/php8ts.dll"
LoadModule php_module "Z:/PHP/php-8.3.30-Win32-vs16-x64/php8apache2_4.dll"
AddType application/x-httpd-php .php
PHPIniDir "Z:/PHP/php-8.3.30-Win32-vs16-x64/"
```
and add _Include conf/php.conf_ in bottom file httpd.conf in your Apache24 folder.

example available in config folder.

## Info  
.bat file must be running in administrator mode.
This program built for learning and sharing only.

## License  
This project is under MIT License.
