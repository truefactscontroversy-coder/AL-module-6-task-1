
from ftplib import FTP

""" 
def test_open_remote_FTP_server():
    ftp.connect("server url")
"""
#---------------------------------------------------------------------------    
# moving onto file opening function as the mock ftp server is not built yet
#---------------------------------------------------------------------------
""" 
def test_show_all_dict_names():
ftp.nlst("lists all files in the ftp directory")
"""
#------------------------------------------------------
# moving on because ftp server is not set up yet
#------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
""" 
open file unit
i will be using a mock file created from appedix example as the file generation has not been set up
"""
#-----------------------------------------------------------------------------------------------------
def open_patient_file_and_save_data(patient):
  patient1 = open(patient, "r")
  return print(type(patient1)), print(patient1.read()), patient1
   
# open_patient_file_and_save_data("patient files/valid/MED_DATA_20230603140104.csv")

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
    second = numb[12:]
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
      return print(True) 
# patient = check_for_valid_format("patient files/valid/MED_DATA_20230603140104.csv")

#----------------------------------------
# batch ID duplication check unit
#----------------------------------------

import csv 
from collections import Counter

def check_for_dup_batch_ID(patient):
    extracted_batch_ID = []
    patient_data = open(patient, newline="")
    extracted_batch_ID.append([row.split(",")[0] for row in patient_data])
    batch_id = tuple(extracted_batch_ID[0])
    batch_ID = Counter(batch_id)
    ID_amount_list = list(batch_ID.values())
    if any(id != 1 for id in ID_amount_list):
        return print(False)
    else:
        return print(True)   
#check_for_dup_batch_ID("patient files/not valid/1/MED_DATA_120603189004.csv")

def check_for_invalid_field_name(patient):
   column_names = open(patient, "r")
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
         return print(False)
   elif ( total_columns != 12 ):
       return False 
   elif first_row[0] != "batch_id" or first_row[1] != "timestamp":
        return print(False)
   elif readings_count != 10:
        return print(False)
   else:
      return print(True)
   

#check_for_invalid_field_name("patient files/valid/valid data.csv")

def check_missing_column_row_and_invalid_entries(patient):
   row_of_patient_data = []
   patient_data = open(patient, newline="") 
   for row in patient_data:
       row_of_patient_data.append(row.split(","))
   for batch in row_of_patient_data:
       if len(batch) != 12:
          return print(False)
       else:
          return print(True)
                                  

#check_missing_column_row_and_invalid_entries("patient files/not valid/1/MED_DATA_120603189004.csv")

def check_for_valid_reading_values(patient):
    extracted_patient_readings = []
    patient_data = open(patient, newline="")
    extracted_patient_readings.append([readings.split(",")[2:] for readings in patient_data])
    patient_readings = extracted_patient_readings[0]
    patient_readings = patient_readings[1:]
    patient_readings_len = [len(subset)for subset in patient_readings]
    if 10 not in patient_readings_len:
        return print(False)
    try: 
       patient_readings_float = [[float(readings) for readings in sublist] for sublist in patient_readings]
    except ValueError:
       return print(False)
    patient_readings_valid_or_not_valid = [[float > 9.9 for float in subset ] for subset in patient_readings_float]
    if True in patient_readings_valid_or_not_valid: 
        return print(False)
    else:
        return print(True)
 
#check_for_valid_reading_values("patient files/not valid/2/MED_DATA_20230512140104(MED_DATA_20230512140104).csv")
import os
def check_for_0_byte(file_import):
   file = file_import
   file_size = os.path.getsize(file)
   if file_size == 0:
      return print(False)
   else:
      return print(True)
   
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

good_file = True
bad_file = False
#test_check_for_malformed_file("patient files/not valid/4/MED_DATA_20230303140104.csv")
import shutil
def move_files_unit(file, true_or_false):
   if true_or_false == True:
       good_file = file
       destination = "patient files/good files"
       shutil.move(good_file, destination)
   else:
       bad_file = file
       destination = "patient files/bad files"
       shutil.move(bad_file, destination)

move_files_unit("patient files/valid/MED_DATA_20230603140104.csv", good_file)