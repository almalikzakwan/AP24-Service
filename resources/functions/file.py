class files:
    """
    class for read and write file.

    read(path: str)
    write(path: str)
    """
    def __init__(self, path: str) -> str:
        """ init default path value """
        self.path = path

    def read(self, mode:str = "r"):
        """ read a file. """
        file = open(self.path, mode)
        value = file.read()
        file.close()
        self.close(file)

        return value
    
    def write(self, string: str, mode:str ="a") -> bool:
        """ write into file. """
        file = open(self.path, mode)
        file.write(string)
        self.close(file)

        return True
    
    def readlines(self, mode:str ="r") -> list:
        """ read all lines in file """
        file = open(self.path, mode)
        return file.readlines()

    def close(self, file) -> bool:
        """ close file after execution """
        file.close()
        return True


