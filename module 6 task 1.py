

from ftplib import FTP
import ftplib
import ssl
import csv 
import os

def open_remote_FTP_server_and_download_files(host, port, username, passwd, directory, local):
    ftp = FTP()
    ftp.connect(host, port, None)
    ftp.login( username, passwd)
    ftp.cwd(directory)
    patient_files = ftp.nlst()
    downloaded_good_folder = "patient files/good files"
    downloaded_good_files = set(os.listdir(downloaded_good_folder))
    downloaded_bad_folder = "patient files/bad files"
    downloaded_bad_files = set(os.listdir(downloaded_bad_folder))
    filtered_patient_files = [file for file in patient_files if file not in (downloaded_good_files or downloaded_bad_files)]
    for files in filtered_patient_files:
        local_path = os.path.join(local, files)
        with open(local_path, "wb") as newfile:
            ftp.retrbinary(f"RETR {files}", newfile.write)
    ftp.quit()
    

    




#---------------------------------------------
# validation check for correct date format
#---------------------------------------------
def check_for_valid_format(patient):
    numb = ""
    for ch in patient:
        if ch.isdigit():          
            numb += ch
    century = numb[0:2]
    numbcentury = int(century)
    year = numb[2:4]
    numbyear = int(year)
    month = numb[4:6]
    numbmonth = int(month)
    day = numb[6:8]
    numbday = int(day)
    hour = numb[8:10]
    numbhour = int(hour)
    minute = numb[10:12]
    numbmin = int(minute)
    second = numb[12:14]
    numbsec = int(second)
    if numbcentury != 20:
     return False
    elif numbyear >= 27:
      return False
    elif numbmonth >= 13:
      return False
    elif numbday >= 32:
      return False
    elif numbhour >= 25:
      return False
    elif numbmin > 61:
      return False
    elif numbsec > 61:
      return False
    else:
      return True 



#----------------------------------------
# batch ID duplication check unit
#----------------------------------------


from collections import Counter

def check_for_dup_batch_ID(patient):
    extracted_batch_ID = []
    patient_data =  open(patient, newline="")
    extracted_batch_ID.append([row.split(",")[0] for row in patient_data])
    batch_id = tuple(extracted_batch_ID[0])
    batch_ID = Counter(batch_id)
    ID_amount_list = list(batch_ID.values())
    if any(id != 1 for id in ID_amount_list):
        return False
    else:
        return True   
#check_for_dup_batch_ID("patient files/valid/MED_DATA_20230603140104.csv")

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
   

#check_for_invalid_field_name("patient files/valid/valid data.csv")

def check_missing_column_row_and_invalid_entries(patient):
   row_of_patient_data = []
   is_row_12 = []
   patient_data = open(patient, newline="") 
   for row in patient_data:
       row_of_patient_data.append(row.split(","))
   for batches in row_of_patient_data:
       is_row_12.append(len(batches))
   for numb in row_of_patient_data:
       if len(numb) != 12:
          return False
       else:
          return True
                                  

#check_missing_column_row_and_invalid_entries("patient files/valid/MED_DATA_20230603140104.csv")

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
    patient_readings_valid_or_not_valid = [[float > 9.9 for float in subset ] for subset in patient_readings_float]
    if True in patient_readings_valid_or_not_valid: 
        return False
    else:
        return True
 
#check_for_valid_reading_values("patient files/not valid/2/MED_DATA_20230512140104(MED_DATA_20230512140104).csv")

def check_for_0_byte(file_import):
   file = file_import
   file_size = os.path.getsize(file)
   if file_size == 0:
      return False
   else:
      return True
   
#check_for_0_byte("patient files/valid/valid data(MED_DATA_20230603140104).csv")

#-------------------------------------
# moving on because i need assistence
#-------------------------------------
def test_check_for_malformed_file(file):
    patient_data = []
    length_of_patient_row = []
    file_opened = open(file, mode="r")
    patient_data.append(file_opened.readlines())
    return print(patient_data[0][3])
    """for sublist in patient_data:
        if , at sublist[0]
           return False
    for sublist in patient_data:
       if "" and '' in sublist:
          return False
    count_of_quotes = []
    for sub_element in patient_data:
        count_of_quotes.append(sub_element.count(" or '))
    if count_of_quotes / 2:
       return False
    elif count_of_quotes / 2 != 11:
        return False
    elif count_of_quotes == 0:
        return True 
        if "" in patient_data[0][1]: """

#test_check_for_malformed_file("patient files/not valid/4/MED_DATA_20230303140104.csv")

import shutil
def move_bad_files_unit(file):
    bad_file = file
    destination = r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\patient files\bad files"
    shutil.move(bad_file, destination)

def move_good_file_unit(file):
    good_file = file
    destination = r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\patient files\good files"
    shutil.move(good_file, destination)

#move_files_unit("patient files/valid/MED_DATA_20230603140104.csv", good_file)
def test_for_valid_file(patient_file):
    patient_file_unknow = check_for_dup_batch_ID(patient_file)
    if patient_file_unknow == True:
        patient_file_unknow = check_for_invalid_field_name(patient_file)
    if patient_file_unknow == True:
        patient_file_unknow = check_missing_column_row_and_invalid_entries(patient_file)
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





def test_file_for_true_or_false(file):
    patient_data = file
    patient_file_unknown = check_for_valid_format(patient_data)
    if patient_file_unknown == True:
        patient_known_data = test_for_valid_file (patient_data)
        if patient_known_data == True:
            move_good_file_unit(patient_data)
        else:
            move_bad_files_unit(patient_data)
    else:
        move_bad_files_unit(patient_data)
        
   

#
# integration unit for all units
#

from pathlib import Path
open_remote_FTP_server_and_download_files("127.0.0.1", 21, "FTP for school", "FTPforschool246","/FTPschool/files for ftp", "patient files\\unknown files")
unknown_file_folder = r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\patient files\unknown files"
os.chdir(unknown_file_folder)
downloaded_files = os.listdir()
for files in downloaded_files:
    test_file_for_true_or_false(files)

def add(a, b):
  a += b
  return a

print(add(5,5))