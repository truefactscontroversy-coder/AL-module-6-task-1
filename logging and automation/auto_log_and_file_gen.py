import logging
import requests
import random
import os
import csv
from datetime import datetime

def auto_log(log_message):
    api_url = "https://www.uuidtools.com/api/generate/v1"

    UUID_code = requests.get(api_url)
    uuid_code = str(UUID_code.json())

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(custom_attribute)s:%(message)s")
    file_handler = logging.FileHandler(r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1-1\File_for_logs.txt", mode='a')
    file_handler.setFormatter(formatter)

    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.custom_attribute = uuid_code
        return record

    logging.setLogRecordFactory(record_factory)

    

    logger.addHandler(file_handler)


    return logger.info(log_message)




def random_headers():
    headers = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]
    shuffled_headers = []
    new_headers = []
    for header in headers:
        new_headers.append(list(header))
    
    for index in new_headers:
        current_header = index
        indx = random.randrange(len(index))
        current_header.pop(indx)
        current_header = "".join(current_header)
        shuffled_headers.append(current_header)
    
    return shuffled_headers 

def correct_filename_generator():
    patient_data_name = ""
    start_date = "20230603140104"
    end_date = "20261231235959"
    start_date = datetime.strptime(start_date, "%Y%m%d%H%M%S")
    end_date = datetime.strptime(end_date, "%Y%m%d%H%M%S")
    random_date = start_date + (end_date - start_date) * random.random()
    random_date = random_date.strftime("%Y%m%d%H%M%S")
    patient_data_name = "MED_DATA_" + str(random_date) + ".csv"
    return patient_data_name

# random.randint(1, 10) will produce dups


def correct_file_generator():
    file_data = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]
    

    random_batchid = []
    while len(random_batchid) != 10:
        for numb in range(10):
            id = random.randint(1, 999)
            if id not in random_batchid:
                    random_batchid.append(id)
    
    
    random_timestamp = ""
    random_readings = []
    random_readings_row = []
        

    
        
         
    while len(random_readings) != 10:
        for numb in range(10):
            id = random.uniform(1, 9.9)
            if id not in random_readings:
                random_readings_row.append(id)
  
    
    

        
    return file_data
    
   
print(correct_file_generator())



#file_path_for_ftp_file_folder = r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\logging and automation\csv files for ftp"
"""mock_filename = correct_filename_generator()
file_path = os.path.join(file_path_for_ftp_file_folder, mock_filename)
    with open(file_path, mode="w") as folder:
        file_created = csv.writer(folder)
        file_created.writerow(file_data)"""
