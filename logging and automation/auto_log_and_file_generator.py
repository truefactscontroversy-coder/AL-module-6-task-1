import logging
import requests
import random



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



def correct_file_generator():
    file = ["batch_id", "timestamp", "reading1", "reading2", "reading3", "reading4", "reading5", "reading6", "reading7", "reading8", "reading9", "reading10"]