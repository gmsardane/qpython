import os


def renameFiles():
    
  file_list = os.list(r"C:\Users") #list files in the dir
  os.getcwd() #get current working dir
  os.chdir(r"C:\Users") #change dir
  
  for files in file_list
    print "Renaming ", file, " to ", file.translate(None,"0123456789")
    os.rename(file,file.translate(None,"0123456789"))
    
    

renameFiles()
