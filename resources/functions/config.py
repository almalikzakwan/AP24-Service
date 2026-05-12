from functions.root import root as r
from functions.file import files as f

class config:
    def path(dp: str = "config/development.conf") -> tuple:
        """
        file that need to change port
        change with your folder instead (my example was conf/extra/developments folder) 
        """
        rt = r()
        AP24Path = rt.AP24Path()
        files = f(f"{AP24Path}/{dp}")
        developments = files.read()

        APPath = rt.ApachePath()
        return [
            f"{APPath}/conf/httpd.conf",
            f"{APPath}/conf/extra/httpd-ssl.conf",
            f"{APPath}/conf/extra/httpd-vhosts.conf", 
            f"{APPath}/{developments}"
        ]