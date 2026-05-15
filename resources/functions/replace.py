import os
from functions.file import files as f

class replace:
    def string(fp: str, ols: str, nes:str) -> bool:
        """ Reads file and replace old string with the new one """
        # Validate file existence
        if not os.path.isfile(fp):
            print(f"Error: File '{fp}' does not exists.")
            return False

        try: 
            # init file instance
            file = f(fp)
            content = file.read()
            upc = content.replace(str(ols),str(nes))
            fn = os.path.basename(fp)

            if upc != content:
                file.write(string = upc, mode="w")
            else:
                print(f"No '{ols}' found in {fn}.")

            print(f"[INFO] Replaced all '{ols}' with '{nes}' in {fn}")

            return True

        except (OSError, IOError) as e:
            print(f"Replace File Error: {e}")
            return False
        
    def line(fp: str, line:int ,ols: str, nes: str):
        """ replace string in file line"""
        # initiate file classing
        file = f(fp)
        readlines = file.readlines()
        text = readlines[line].replace(ols, nes)
        print(text)
        readlines[line] = text

        return True
    
