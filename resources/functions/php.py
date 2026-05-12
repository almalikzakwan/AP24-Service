from functions.root import root as r
from functions.file import files as f

class php:
    """ Create php configuration in Apache24 folder """
    def write(self) -> bool:
        root = r()
        path = f"{root.path()}/conf/php.conf"
        file = f(path)
        string = self.string()
        file.write(string)

        return True

    """ Create php config string base on php path """
    def string(self) -> str:
        fp = f"../../config/php.conf"
        file = f(fp)
        php = file.read()
        
        return f'''
LoadFile "{php}/php8ts.dll"
LoadModule php_module "{php}/php8apache2_4.dll"
AddType application/x-httpd-php .php
PHPIniDir "{php}/"
'''

