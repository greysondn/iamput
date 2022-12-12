# is a mod config library
import pathlib

class Config():
    pass

class ConfigFile():
    pass

class ConfigFolder():
    def __init__(
                    self,
                    path:pathlib.Path = pathlib.Path(""),
                    backupPath:pathlib.Path = pathlib.Path("")
                ):
        self.path:pathlib.Path = path
        self.backupPath:pathlib.Path = backupPath
        self.files:list["ConfigFile"]
        
    def overwrite(self, other:"ConfigFolder"):
        """Overwrites all of other with self.

        Args:
            other (ConfigFolder): folder to overwrite
        """
        raise NotImplementedError()
    
    def mergeInto(self, other:"ConfigFolder"):
        """Merge self into other, overwriting files as needbe

        Args:
            other (ConfigFolder): other
        """
        raise NotImplementedError()