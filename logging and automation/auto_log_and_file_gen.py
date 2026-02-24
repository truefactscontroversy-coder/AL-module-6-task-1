
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
    file_handler = logging.FileHandler(r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\logging and automation\file_logs.txt", mode='a')
    file_handler.setFormatter(formatter)

    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.custom_attribute = uuid_code
        return record

    logging.setLogRecordFactory(record_factory)

    

    logger.addHandler(file_handler)


    return logger.info(log_message)




def random_invalid_headers():
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

def invalid_filename_generator():
    patient_data_name = ""
    start_date = "01202701010101"
    end_date = "23209059123159"
    start_date = datetime.strptime(start_date, "%H%Y%M%m%d%S")
    end_date = datetime.strptime(end_date, "%H%Y%M%m%d%S")
    random_date = start_date + (end_date - start_date) * random.random()
    random_date = random_date.strftime("%H%Y%M%m%d%S")
    patient_data_name = "MED_DATA_" + str(random_date) + ".csv"
    return patient_data_name



def invalid_batchid_generator():
    numb_of_rows = random.randint(range)
    random_id = []
    for x in range(numb_of_rows):
        random_id.append(random.randint(range))
    index_for_dup = random.randrange(len(index in random_id))
    dup_id = random_id[index_for_dup]
    index = random.randrange(len(index in random_id))
    random_id.insert(index)
    return random_id

print(invalid_batchid_generator())





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
    file_data = [["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]]
    

    random_batchid = []
    while len(random_batchid) != 10:
        for numb in range(10):
            id = random.randint(1, 999)
            if id not in random_batchid:
                random_batchid.append(id)
    
    
    random_timestamp = ""
    random_readings = []

    def row_data():
        data_for_row = []    
        for date in range(1):
            start_date = "010101"
            end_date = "235959"
            start_date = datetime.strptime(start_date, "%H%M%S")
            end_date = datetime.strptime(end_date, "%H%M%S")
            random_date = start_date + (end_date - start_date) * random.random()
            random_date = random_date.strftime("%H:%M:%S")
            random_timestamp = str(random_date)
    
    
         
        while len(random_readings) != 10:
            id = round(random.uniform(1, 9.9), 3)
            if id not in random_readings:
                random_readings.append(id)
        
        data_for_row.append(random_timestamp)
        data_for_row.extend(random_readings)
        return data_for_row
    
    while random_batchid:
        data = row_data()
        data.insert(0, random_batchid.pop(0))
        file_data.append(list(data))


    file_path_for_ftp_file_folder = r"C:\Users\ajlxs\OneDrive\Documents\coding project 2.0\AL-module-6-task-1\logging and automation\csv files for ftp\correct files"
    mock_filename = correct_filename_generator()
    file_path = os.path.join(file_path_for_ftp_file_folder, mock_filename)
    with open(file_path, mode="w", newline="") as folder:
        file_created = csv.writer(folder)
        file_created.writerows(list(file_data))
    
    return file_data

