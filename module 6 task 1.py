
from ftplib import FTP

""" def test_open_remote_FTP_server():
    ftp.connect("server url")
    """
#---------------------------------------------------------------------------    
# moving onto file opening function as the mock ftp server is not built yet
#---------------------------------------------------------------------------
""" def test_show_all_dict_names():
    ftp.nlst("lists all files in the ftp directory")
    """
#------------------------------------------------------
# moving on because ftp server is not set up yet
#------------------------------------------------------

#-----------------------------------------------------------------------------------------------------
# i will be using a mock file created from appedix example as the file generation has not been set up
#-----------------------------------------------------------------------------------------------------

def open_patient_file_and_save_data(patient):
  patient1 = open(patient, "r")
  return print(patient1.readable()), print(patient1.read()), patient1
   
open_patient_file_and_save_data("patient files/valid/MED_DATA_20230603140104.csv")

def test_for_valid_format(patient):
    patient2 = patient 
    str, numb ("seperates numbers and letters")
    century = numb(0:3)
    year = numb(3:5)
    month = numb(5:7)
    day = numb
    hour = numb
    minute = numb
    second = numb
    if century >= 21:
     return False
    if year >= 27:
      return False
    if month >= 13:
      return False
    if day >= 32:
      return False
    if hour >= 25:
      return False
    if minute > 61:
      return False
    if month > 61:
      return False