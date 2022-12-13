# is a mod config library
import os
import pathlib
import shutil

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
        self.files:list["ConfigFile"]
        
    def delete(self):
        """Deletes self. You were warned.
        """
        # destroy self
        shutil.rmtree(self.path)
        
    def overwrite(self, other:"ConfigFolder"):
        """Overwrites all of other with self.

        Basically, deletes, then writes into the folder.

        Args:
            other (ConfigFolder): folder to overwrite
        """
        # before we break anything
        raise NotImplementedError()
    
        # we start by just deleting the other
        other.delete()
        
        # build list of our files and folders
        fDirs = []
        fFiles = []
        
        for (root, dirs, files) in os.walk(self.path):
            fDirs = fDirs + dirs
            
            for f in files:
                fFiles.append(root + "\\" + f)
        
        # recreate directory tree
        for dir in fDirs:
            os.makedirs(
                        str(other.path) + "\\" + dir,
                        exist_ok= True
                )
        
        # todo: WOOPS
    
    def mergeInto(self, other:"ConfigFolder"):
        """Merge self into other, overwriting files as needbe

        Args:
            other (ConfigFolder): other
        """
        raise NotImplementedError()