from functions.root import root as r
from functions.file import files as f

class php:
    """ Create php configuration in Apache24 folder """
    def write() -> bool:
        root = r()
        path = f"{root.ApachePath()}/conf/php.conf"
        APachefile = f(path)

        fp = f"{root.AP24Path()}/config/php.conf"
        file = f(fp)
        php = file.read()

        string = f'''
LoadFile "{php}/php8ts.dll"
LoadModule php_module "{php}/php8apache2_4.dll"
AddType application/x-httpd-php .php
PHPIniDir "{php}/"
'''
        APachefile.write(string = string, mode="w")

        return True

