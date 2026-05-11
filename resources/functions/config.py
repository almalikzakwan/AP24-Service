from functions.root import root as r

class config:
    def path():
        """
        file that need to change port
        change with your folder instead (my example was conf/extra/developments folder) 
        """
        r = r()
        path = r.path()
        return [
            f"{path}/conf/httpd.conf",
            f"{path}/conf/extra/httpd-ssl.conf",
            f"{path}/conf/extra/httpd-vhosts.conf", 
            f"{path}/conf/extra/developments" # example of my developments folder, change your's instead.
        ]