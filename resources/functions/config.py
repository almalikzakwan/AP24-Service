from functions.root import root as r
from functions.file import files as f

class config:
    def path(dp: str = "../../config/development.conf") -> tuple:
        """
        file that need to change port
        change with your folder instead (my example was conf/extra/developments folder) 
        """
        files = f(dp)
        developments = files.read()

        path = r.path()
        return [
            f"{path}/conf/httpd.conf",
            f"{path}/conf/extra/httpd-ssl.conf",
            f"{path}/conf/extra/httpd-vhosts.conf", 
            f"{path}/{developments}"
        ]