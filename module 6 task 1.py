
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
  return print(patient1.readable())

open_patient_file_and_save_data("patient files/valid/MED_DATA_20230603140104.csv")
