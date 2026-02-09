
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
  return print(patient1.readable()), print(patient1.read()), patient1
   
open_patient_file_and_save_data("patient files/valid/MED_DATA_20230603140104.csv")

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
patient = check_for_valid_format("patient files/valid/MED_DATA_20230603140104.csv")

#----------------------------------------
# duplication check unit
#----------------------------------------
import csv 
from collections import Counter

def test_for_dup_batch_ID(patient):
    column_name = ("isolated column")
    extracted_batch_ID = []
    open("patientfile") as valuepair:
    patient_data = read("patientfile")
    for inter_over_row in patient_data:
        extracted_batch_ID.append({def col: def row, creating valuepairs})
        batch_ID = extracted_batch_ID.get("isolated column")
    batch_ID_dic = Counter(batch_ID)
    batch_ID_final_test = list(batch_ID_dic.value)) 
    for ID in batch_ID_final_test:
        if ID > 1:
        return False
    else:
        return True