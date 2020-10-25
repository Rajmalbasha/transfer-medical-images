import os
import pandas as pd 
import sys
status_filename_with_location = "transfer-images-s1b5/Sample_Image"

if(os.path.isfile(status_filename_with_location)):
    image_list = pd.read_csv(status_filename_with_location)
else:
    print("No csv file with that name at the given location")
    print("Create a new csv file if file not present and re-run the program with that file name")
    print("Else re-run the program with correct location and file name")
    exit()

def add_filename_to_csv(fileName):
    #image_list = pd.read_csv(status_filename_with_location)
    new_row = {'FileName': fileName, 'Status':'Pending for diagnosis'}
    image_list = image_list.append(new_row,ignore_index = True)
    image_list.to_csv(status_filename_with_location, index=False)

def check_for_new_imgfiles(path):
    files_list = os.listdir(path)
    current_image_list = image_list['FileName'].values.tolist()
    print(current_image_list)
    for i in files_list:
        split_str = i.split(".")
        if(split_str[1]=="img"):
            if(i not in current_image_list):
                add_filename_to_csv(i)


def show_all_img_with_status():
    print(image_list)



def update_file_status(fileName, status):
    update_string = "Diagnosed"
    if(status != "yes"):
        update_string = "Pending for Diagnosis"
    image_list.loc[image_list['FileName'] == fileName, ('Status')] = update_string
    image_list.to_csv(status_filename_with_location, index=False)


def update_status():
    
    show_all_img_with_status()
    imageName = input("Type the name of the file you want to select: ")
    inputStr = input("Is this image diagnosed (yes/no)? ")
    if(input == "yes"):
        update_file_status(imageName , inputStr)
    else:
        update_file_status(imageName , inputStr)

def menu(path):
    while 1:
        
        choice = input("press 1 to update and any key other than 1 to exit the application : ")
        if (choice == "1") :
            check_for_new_imgfiles(path)
            update_status()
        else:
            break


if __name__ == "__main__":

     
     path = str(input("Enter the path where .img files are created/present: "))
     isExist = os.path.exists(path)
     if (isExist):
         menu(path)
     else:
         print("Path Doesn't exists. Please re-enter the correct path!!!")