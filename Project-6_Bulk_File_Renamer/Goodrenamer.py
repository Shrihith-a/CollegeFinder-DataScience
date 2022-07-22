import os

def renamer():
    shri = 0 #initiate/iterate over files lists
    path = 'C:\\Users\\Shrih\\OneDrive\\Documents\\Courses\\College_Finder\\Projects\\Project-6_Bulk_File_Renamer\\img\\'
    for filename in os.listdir(path):
        names = f"image {shri}.jpg"
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        shri= shri + 1
    
if __name__ == "__main__":
    renamer()
