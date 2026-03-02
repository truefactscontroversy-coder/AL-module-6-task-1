
import logging
import requests
import random
import os
import csv
from datetime import datetime

#------------------------------------------------
#auto log unit to log results of tests
#------------------------------------------------

#print("please input file for logging test results")
#file_log_path = input()
def auto_log(log_message):
    api_url = "https://www.uuidtools.com/api/generate/v1"

    UUID_code = requests.get(api_url)
    uuid_code = str(UUID_code.json())

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(custom_attribute)s:%(message)s")
    file_handler = logging.FileHandler(file_log_path, mode='a')
    file_handler.setFormatter(formatter)

    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.custom_attribute = uuid_code
        return record

    logging.setLogRecordFactory(record_factory)

    

    logger.addHandler(file_handler)


    return logger.info(log_message)


#--------------------------------------------------------
# unit for creating random invalid headers to put in csv files
#--------------------------------------------------------

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

#------------------------------------------------
# unit for generating random invalid empty files
#------------------------------------------------

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

#------------------------------------------------
# unit for generating random invalid batch ids
#------------------------------------------------

def invalid_batchid_generator():
    numb_of_rows = random.randint(1, 20)
    random_id = []
    for x in range(numb_of_rows):
        random_id.append(random.randint(1, 999))
    index_for_dup = random.randrange(len(random_id))
    dup_id = random_id[index_for_dup]
    index = random.randrange(len(random_id))
    random_id.insert(index,dup_id)
    return random_id

#------------------------------------------------
# unit for generating correct random empty files
#------------------------------------------------

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
    

#----------------------------------------------------------------
# unit for generating correct random data for rows in csv files
#----------------------------------------------------------------


def correct_row_data():
    random_timestamp = ""
    random_readings = []
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


#----------------------------------------------------------------------------------------
# integration of all correct geneator units to generate correctly formatted csv files
#----------------------------------------------------------------------------------------
print("please input file path to store correct files")
filepth_for_correctfiles = input()
def correct_file_generator():
    print("correct file")
    file_data = [["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]]
    

    random_batchid = []
    while len(random_batchid) != 10:
        for numb in range(10):
            id = random.randint(1, 999)
            if id not in random_batchid:
                random_batchid.append(id)
    
    
    

    
    
    while random_batchid:
        data = correct_row_data()
        data.insert(0, random_batchid.pop(0))
        file_data.append(list(data))


    file_path_for_ftp_file_folder = filepth_for_correctfiles
    mock_filename = correct_filename_generator()
    file_path = os.path.join(file_path_for_ftp_file_folder, mock_filename)
    with open(file_path, mode="w", newline="") as folder:
        file_created = csv.writer(folder)
        file_created.writerows(list(file_data))
    return file_data, "correct file"
    



#---------------------------------------------------------------------
# unit for generating invalid data for rows of in csv file
#---------------------------------------------------------------------

def malformed_row_data():
    random_timestamp = ""
    random_readings = []
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
        random_readings.append(id)
    

    for items in random_readings:
        readings = random_readings.pop(0)
        random_readings.append(str(readings))
    
    def random_commas():
        indx = random.randrange(len(random_readings))
        element = random_readings.pop(indx)
        element += "'"
        random_readings.insert(indx, element)
    
    indx = random.randint(1, 5)
    for x in range(indx):
        random_commas()
    
    data_for_row.append(random_timestamp)
    data_for_row.extend(random_readings)
    return data_for_row



#--------------------------------------------------------------------------
# integration of all invalid generator units to generate invalid files
#--------------------------------------------------------------------------
print("please input file path to store invalid files")
filepath_for_invalid_files = input()
def invalid_file_generator():
    accidental_correct_file = []
    filename = []
    invalid_filename = invalid_filename_generator()
    correct_filename = correct_filename_generator()
    filename.append(correct_filename)
    filename.append(invalid_filename)
    indx = random.randrange(2)
    file_name = filename[indx]
    accidental_correct_file.append(indx)
    

    def correct_batchid():
        random_batchid = []
        while len(random_batchid) != 10:
            for numb in range(10):
                id = random.randint(1, 999)
                if id not in random_batchid:
                    random_batchid.append(id)
            return random_batchid


    
    batch_ids = []
    correct_batch_id = correct_batchid()
    invalid_batchid = invalid_batchid_generator()
    batch_ids.append(correct_batch_id)
    batch_ids.append(invalid_batchid)
    indx = random.randrange(2)
    batchid = batch_ids[indx]
    batch_ids.append(indx)
   
   
    headers = []
    invalid_headers = random_invalid_headers()
    correct_headers = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]
    headers.append(correct_headers)
    headers.append(invalid_headers)
    indx = random.randrange(2)
    header = headers[indx]
    accidental_correct_file.append(indx)

    file_data = []
    file_data.append(header)

    def invalid_row_data():
        row_data = []  
        for date in range(1):
            start_date = "010101"
            end_date = "235959"
            start_date = datetime.strptime(start_date, "%H%M%S")
            end_date = datetime.strptime(end_date, "%H%M%S")
            random_date = start_date + (end_date - start_date) * random.random()
            random_date = random_date.strftime("%H:%M:%S")
            random_timestamp = str(random_date)
            row_data.append(random_timestamp)
        


        reading_numb = random.randint(1,3)
        for x in range(reading_numb):
            readings_amount = random.randint(1,20)
            for x in range(readings_amount):
                id = random.uniform(1, 20)
                row_data.append(id)

        return row_data
    

    data_for_rows = [correct_row_data, invalid_row_data, malformed_row_data]
    indx = random.randrange(3)
    data = data_for_rows[indx]
    accidental_correct_file.append(indx)
    accidental_correct_file_total_numb = 0

    for numb in accidental_correct_file:
        accidental_correct_file_total_numb += numb

    
    for x in range(len(batchid)):
        row_info = data()
        row_info.insert(0, batchid.pop(0))
        file_data.append(row_info)

    file_path_for_ftp_invalid_files = filepath_for_invalid_files

    file_path = os.path.join(file_path_for_ftp_invalid_files, file_name)
    with open(file_path, mode="w", newline="") as folder:
        file_created = csv.writer(folder)
        file_created.writerows(list(file_data))

    if accidental_correct_file_total_numb == 0:

        return "correct file"
    else:

        return "invalid file"


#---------------------------------------------------------------------
# unit for generating empty files 
#---------------------------------------------------------------------
def empty_file_generator():
    filename = []
    invalid_filename = invalid_filename_generator()
    correct_filename = correct_filename_generator()
    filename.append(invalid_filename)
    filename.append(correct_filename)
    indx = random.randrange(2)
    file_name = filename[indx]
    file_path_for_ftp_invalid_file = filepath_for_invalid_files

    file_path = os.path.join(file_path_for_ftp_invalid_file, file_name)
    with open(file_path, mode="w", newline="") as folder:
        pass

    return "empty file"



#---------------------------------------------------------------------------------------------
# integration of all units to generate either a correct file, a empty file or a invalid file
#---------------------------------------------------------------------------------------------
def random_file_gen():
    random_numb = random.randint(1, 10)
    file = ""
    if random_numb == (3):
        file = empty_file_generator()
        return (f"{file} successfully generated")
    elif random_numb == (2 or 5 or 8 or 6):
        file = correct_file_generator()
        return (f"{file} successfully generated")
    else:
        file = invalid_file_generator()
        return (f"{file} successfully generated")

print("please input how many random files you would like generated")
number_of_files = int(input())
for numb in range(number_of_files):
    random_file_gen()
print(f"{number_of_files} successfully generated")