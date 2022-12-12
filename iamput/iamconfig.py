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