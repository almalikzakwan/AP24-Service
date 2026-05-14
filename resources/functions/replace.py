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
            print(f"File Error: {e}")
            return False