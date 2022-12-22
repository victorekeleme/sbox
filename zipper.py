import os
import shutil
import time
from destroy import delete


def zipper(ranPath,done):
    fmt = 'zip'
    fTitle = os.listdir(ranPath)[0] # gets the name of the file present in the directory
    fPath = ranPath+'/'+fTitle # merges the path and the filename
    fTitleOut = fTitle.replace(" ", "_")
    fPathOut = ranPath+'/'+fTitleOut # merges the path and the filename for output
    

    print(fPath)
    try:
        if done and os.path.isdir(fPath):            
            shutil.make_archive(f"{fPathOut}", f"{fmt}", f"{fPath}") # Creates a zip of the directory
            time.sleep(1)
            delete(fPath) # fires the delete function
        elif done and (os.path.isfile(fPath) or os.path.islink(fPath)):
            print("Its a file")
        else:
            print("There might be a problem with the source file.")
    except Exception as e:
        print(e)
        print("There might be a problem with the source file.")

    return fPath

