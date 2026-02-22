
import logging
import requests





def automated_logging(log_message):
    api_url = "uuid generator"

    UUID_code = requests.get(api_url)
    uuid_code = str(UUID_code.json())

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(module)s:%(custom_attribute)s:%(message)s")
    file_handler = logging.FileHandler("target file")
    file_handler.setFormatter(formatter)

    old_factory = logging.getLogRecordFactory()

    def record_factory(*args, **kwargs):
        record = old_factory(*args, **kwargs)
        record.custom_attribute = uuid_code
        return record

    logging.setLogRecordFactory(record_factory)


    uuid_logger = logging.FileHandler(uuid_code)

    logger.addHandler(uuid_logger)

    logger.addHandler(file_handler)


    return logger.info(log_message)
 
automated_logging(test_function)