import os
import shutil

def delete(fPath):
    """path could either be relative or absolute. """
    # check if file or directory exists
    if os.path.isfile(fPath) or os.path.islink(fPath):
        # remove file
        os.remove(fPath)
    elif os.path.isdir(fPath):
        # remove directory and all its content
        shutil.rmtree(fPath)
    else:
        raise ValueError(f"Path {fPath} is not a file or dir.")
    
    return "Delete Complete"