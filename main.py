import tkinter
import sys
import os
import patoolib
from unrar import rarfile
# from patool import 
# from pyunpack import Archive
from tkinter.filedialog import askopenfilename, askdirectory

DEST_FOLDER_PREFIX = "dez-"


def main():
  top = tkinter.Tk()
  top.withdraw()
  archivepath = ''
  if(len(sys.argv) == 1):
    archivepath = askopenfilename(title="Selecteaza arhiva")
  else:
    archivepath = sys.argv[1]
  folderpath = os.path.dirname(archivepath)
  filename='.'.join(os.path.basename(archivepath).split('.')[:-1])
  destinationPath = folderpath
  
  if(len(sys.argv) == 3):
    destinationPath = sys.argv[2]
  else:
    destinationPath = askdirectory(title="Selecteaza directorul unde se vor dezarhiva fisierele.", initialdir=destinationPath)
  
  destFilesPath = os.path.join(destinationPath, DEST_FOLDER_PREFIX + filename)
  if(not os.path.exists(destFilesPath)):
    os.makedirs(destFilesPath)
  patoolib.extract_archive(archivepath, outdir=destFilesPath)
  exit()


    # top.mainloop()


if __name__ == "__main__":
  main()
