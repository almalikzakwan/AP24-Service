from functions.root import root as r
from functions.file import file as f

class php:
    def __init__(self):
        pass
    
    """ Create php configuration in Apache24 folder """
    def write(self):
        root = r()
        path = f"{root.path()}/conf/php.conf"
        file = f(path)
        string = self.string
        file.write(string)

    """ Create php config string base on php path """
    def string(self):
        fp = f"../../config/php.conf"
        file = f(fp)
        php = file.read()
        
        return f'''
LoadFile "{php}/php8ts.dll"
LoadModule php_module "{php}/php8apache2_4.dll"
AddType application/x-httpd-php .php
PHPIniDir "{php}/"
'''

