from functions.root import root as r
from functions.file import files as f

class config:
    def path():
        """
        file that need to change port
        change with your folder instead (my example was conf/extra/developments folder) 
        """
        dp = f"../../config/development.conf"
        files = f(dp)
        developments = files.read(dp)

        r = r()
        path = r.path()
        return [
            f"{path}/conf/httpd.conf",
            f"{path}/conf/extra/httpd-ssl.conf",
            f"{path}/conf/extra/httpd-vhosts.conf", 
            f"{developments}"
        ]