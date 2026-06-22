import os
import  shutil
source_folder=r"C:\Users\ABC\Downloads"
file_cat={"Documents":[".pdf",".docx",".txt",".csv",".xlsx",".zip","ipynb",".pptx"],
          "Images":[".jpg",".gif",".png"],
          "videos":[".mp3",".mp4"]}
def organize_folder(folder):
    for filename in os.listdir(folder):  #provide a list of file names
        file_path=os.path.join(folder,filename)  #join the path of folder and the filename
        if os.path.isfile(file_path):   #returns true if the path is of file and false for folder
            ext=os.path.splitext(filename)[1].lower()  #picks the extension part
            print(ext)
            for category,extensions in file_cat.items():
                if ext in extensions:
                    category_folder = os.path.join(folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))  #shutil.move(source,destination)
                    break

organize_folder(source_folder)
