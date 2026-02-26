


from ftplib import FTP
import ftplib
import ssl
import csv 
import os
from datetime import datetime


def open_remote_FTP_server_and_download_files(host, port, username, passwd, directory, local):
    ftp = FTP()
    try:
        ftp.connect(host, port, None)
    except AttributeError:
        print("host number or port number is incorrect")
    try:
        ftp.login( username, passwd)
    except AttributeError:
        print("username or password is incorrect")
    ftp.cwd(directory)
    patient_files = ftp.nlst()
    downloaded_good_folder = r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\patient files\good files"
    downloaded_good_files = set(os.listdir(downloaded_good_folder))
    downloaded_bad_folder = r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\patient files\bad files"
    downloaded_bad_files = set(os.listdir(downloaded_bad_folder))
    filtered_patient_files = [file for file in patient_files if file not in (downloaded_good_files or downloaded_bad_files)]
    for files in filtered_patient_files:
        local_path = os.path.join(local, files)
        with open(local_path, "wb") as newfile:
            ftp.retrbinary(f"RETR {files}", newfile.write)
    ftp.quit()
    print("finished downloading files from FTP server")

    



#---------------------------------------------
# validation check for correct date format
#---------------------------------------------
def check_for_valid_format(patient):
    date_numb = patient.split("_")
    date_numb = date_numb.pop(2)
    try:
        numb = ""
        for ch in date_numb:
            if ch.isdigit():          
                numb += ch
        date = datetime.strptime(numb, "%Y%m%d%H%M%S")
    except ValueError:
        return False
    else:
        return True







    


#----------------------------------------
# batch ID duplication check unit
#----------------------------------------


from collections import Counter

def check_for_dup_batch_ID(patient):
    extracted_batch_ID = []
    patient_data = open(patient, newline="")
    extracted_batch_ID.append([row.split(",")[0] for row in patient_data])
    batch_id = tuple(extracted_batch_ID[0])
    batch_ID = Counter(batch_id)
    ID_amount_list = list(batch_ID.values())
    if any(id != 1 for id in ID_amount_list):
        return False
    else:
        return True   



def check_for_invalid_field_name(patient):
   column_names = open(patient)
   first_column = column_names.readline()
   first_row = first_column.split(",")
   readings = first_row[2:]
   readings_sorted = ";".join(readings)
   readings_sorted = readings_sorted.strip("\n")
   readings_list = ["reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]
   reading_rejoined = ";".join(readings_list)
   readings_count = len(readings)
   total_columns = len(first_row)
   if readings_sorted != reading_rejoined:
         return False
   elif ( total_columns != 12 ):
       return False 
   elif first_row[0] != "batch_id" or first_row[1] != "timestamp":
        return False
   elif readings_count != 10:
        return False
   else:
      return True
   



def check_missing_column_row_and_invalid_entries(patient):
   row_of_patient_data = []
   is_row_12 = []
   is_true_or_false = []
   with open(patient, mode="r", newline="") as files:
       data = csv.reader(files)
       for row in data:
           row_of_patient_data.append(row)

   
   
   for batches in row_of_patient_data:
        is_row_12.append(len(batches))

   for numb in is_row_12:
        if numb != 12:
            is_true_or_false.append(False)
        else:
            is_true_or_false.append(True)
    
   if False in is_true_or_false:
       return False
   else:
       return True

def check_for_valid_reading_values(patient):
    extracted_patient_readings = []
    patient_data = open(patient, newline="")
    extracted_patient_readings.append([readings.split(",")[2:] for readings in patient_data])
    patient_readings = extracted_patient_readings[0]
    patient_readings = patient_readings[1:]
    patient_readings_len = [len(subset)for subset in patient_readings]
    if 10 not in patient_readings_len:
        return False
    try: 
       patient_readings_float = [[float(readings) for readings in sublist] for sublist in patient_readings]
    except ValueError:
       return False
    else:
        patient_readings_valid_or_not_valid = [[float > 9.9 for float in subset ] for subset in patient_readings_float]
        if True in patient_readings_valid_or_not_valid: 
            return False
        else:
            return True




def check_for_0_byte(file_import):
   file = file_import
   file_size = os.path.getsize(file)
   if file_size == 0:
      return False
   else:
      return True
   



import shutil
def move_bad_files_unit(file, bad_folder_path):
    bad_file = file
    destination = bad_folder_path
    shutil.move(bad_file, destination)

def move_good_file_unit(file, good_folder_path):
    good_file = file
    destination = good_folder_path
    shutil.move(good_file, destination)


def test_for_valid_file(patient_file):
    patient_file_unknow = check_for_dup_batch_ID(patient_file)
    if patient_file_unknow == True:
        patient_file_unknow = check_for_invalid_field_name(patient_file)
    if patient_file_unknow == True:
        patient_file_unknow = check_missing_column_row_and_invalid_entries(patient_file)
    if patient_file_unknow == True:
        patient_file_unknow = check_for_valid_reading_values(patient_file)
    if patient_file_unknow == True:
        patient_file_unknow = check_for_0_byte(patient_file)
    if patient_file_unknow == True:
        return True
    else:
        return False





def test_file_for_true_or_false(file, good_folder, bad_folder):
    patient_data = file
    patient_file_unknown = check_for_valid_format(patient_data)
    if patient_file_unknown == True:
        patient_known_data = test_for_valid_file (patient_data)
        if patient_known_data == True:
            move_good_file_unit(patient_data, good_folder)
            print("file is valid")
        else:
            move_bad_files_unit(patient_data, bad_folder)
            print("file is not valid")
    else:
        move_bad_files_unit(patient_data, bad_folder)
        print("file is not valid")
   

#
# integration unit for all units
#

from pathlib import Path
def access_ftp_and_dowload_files():
    user_inputs = []
    print("please input host number, port number in this order")
    inputs = input().split(",")
    print("please enter FTP username and password")
    inputs.extend(input().split(","))
    print("please enter directory name and placeholder folder to download files")
    inputs.extend(input().split(","))
    for items in inputs:
            user_inputs.append(items.strip())
    port = user_inputs.pop(1)
    user_inputs.insert(1,int(port))
    open_remote_FTP_server_and_download_files(user_inputs[0], user_inputs[1], user_inputs[2], user_inputs[3], user_inputs[4], user_inputs[5])
    unknown_file_folder = user_inputs[5]
    os.chdir(unknown_file_folder)
    downloaded_files = os.listdir()
    file_number = 1
    print("please enter file path for good files")
    goodfolder = input()
    print("please enter file path for bad files")
    badfolder = input()
    for files in downloaded_files:
        test_file_for_true_or_false(files, goodfolder, badfolder)
        print(f"preformed validation check on file {file_number} and moved file to good file folder or bad file folder")
        file_number += 1

    print("finished validation checks and downloading files")


access_ftp_and_dowload_files()


def open_file(file):
    with open(file, mode="r") as file_lines:
        print(file_lines.readlines())



