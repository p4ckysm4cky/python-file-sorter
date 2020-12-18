import os
import shutil

#Function used for checking valid directory

def filepath_getter():
    filepath = input("Please enter where you would like the script to run: \n")
    if os.path.isdir(filepath) == True:
        return filepath
    else: 
        print("Please enter a correct path\n ")
        filepath_getter()
        
source = filepath_getter()
#os.chdir(source)
#os.mkdir("sorted")
sorted_source = os.path.join(source,"sorted")

if os.path.isdir(sorted_source) == True:
    pass
else:
    os.makedirs(sorted_source)






print(f"Starting to sort files to: \"{os.getcwd()}...\"")
print(" ")

i = 0
for root, dirs, files in os.walk(source):
    for filename in files:
        extension = os.path.splitext(filename)[1][1:]
        #print(f'{filename}, {extension}\n ')
        #print(f"loop {i}")
        if os.path.isdir(os.path.join(sorted_source, extension)) == False:
            os.makedirs(os.path.join(sorted_source, extension))
        #i += 1
        #print(filename)
        try:
            shutil.copy(os.path.join(root, filename), os.path.join(sorted_source, extension))
            i += 1
            print(f"{i}: \"{filename}\" successfully copied")
        except shutil.SameFileError:
            pass
        except:
            print("An error occurred")
        
