

from ftplib import FTP
import ftplib
import csv
import os
from datetime import datetime
import socket
from collections import Counter
import shutil
from pathlib import Path

# --------------------------------------------------------------------------------
# opens ftp server, checks for new/unseen file, and downloads all new files
# --------------------------------------------------------------------------------


def open_remote_FTP_server_and_download_files():
    ftp = FTP()
    user_data = []
    inputs = []

    while True:
        try:
            print("please input host number and port number. "
                  "In this order seperated by a (,) Example: 127.0.0.1, 26."
                 )
            inputs.extend(input().split(","))
            for items in inputs:
                user_data.append(items.strip(' "'))
            while True:
                try:
                    port = user_data.pop(1)
                    user_data.insert(1, int(port))
                    break
                except ValueError:
                    print("Error either you did not separate the host number "
                          "and the port number by a (,) "
                          "or you only input one" \
                          " number. please input two numbers serparated by a " \
                          "comma (,) . Example: 127.0.0.1, 26."
                         )
                    user_data = []
                    inputs = input().split(",")
                    print(inputs)
                    for items in inputs:
                        user_data.append(items.strip(' "'))
                except IndexError:
                    print("Error either you did not separate the host number "
                          "and the port number by a (,) "
                          "or you only input one " \
                          "number. please input two numbers serperated by a " \
                          "comma (,) . Example: 127.0.0.1, 26."
                          )
                    user_data = []
                    inputs = input().split(",")
                    print(inputs)
                    for items in inputs:
                        user_data.append(items.strip(' "'))
            port = user_data.pop(1)
            user_data.insert(1, int(port))
            port = user_data.pop(1)
            user_data.insert(1, int(port))
            ftp.connect(user_data[0], user_data[1], None)
            print("connected to server")
            break
        except socket.gaierror:
            print("host number or port number is incorrect please reenter " \
                  "host number and port number.")
            user_data = []
            inputs = input().split(",")
            for items in inputs:
                user_data.append(items.strip(' "'))
            port = user_data.pop(1)
            user_data.insert(1, int(port))

    print("")

    print("please enter FTP username and password. "
          "In this order seperated by a (,) Example: username234, password123 "
         )
    inputs.extend(input().split(","))
    for items in inputs[2:]:
        user_data.append(items.strip())
    while True:
        try:
            ftp.login(user_data[2], user_data[3])
            print("login succssessful")
            break
        except ftplib.error_perm:
            print(
                "username or password is incorrect " \
                "please reenter username and password"
                 )
            del inputs[2:]
            del user_data[2:]
            inputs.extend(input().split(","))
            for items in inputs[2:]:
                user_data.append(items.strip())
        except IndexError:
            print("Error either you did not separate " \
                  "the username and the password by a (,) "
                  "or you only input one. please input " \
                  "two numbers serparated by a comma (,). "
                  "Example: username234, password123 "
                 )
            del inputs[2:]
            del user_data[2:]
            inputs.extend(input().split(","))
            for items in inputs[2:4]:
                user_data.append(items.strip())

    print("")

    print("please enter directory name of folder in FTP "
          "that you would like to download files from"
          )
    inputs.append(input())
    user_data.append(inputs[4].strip())
    while True:
        try:
            ftp.cwd(user_data[4])
            print("succsessfully located folder in the FTP server")
            break
        except ftplib.error_perm:
            print("incorrect or invalid file path entered " \
                  "please reenter directory path"
                  )
            del inputs[4:]
            del user_data[4:]
            inputs.extend(input().split(","))
            user_data.append(inputs[4].strip())

    print("")

    patient_files = ftp.nlst()
    print("To scan for unseen files, " \
          "you will need enter the file paths to the folders containing "
          "the previously downloaded files or the empty folders "
          "were you would like the valid and invalid files to be stored"
          )

    print("")
    print("please enter file path for the valid files")
    downloaded_good_folder = input().strip(' "')
    while True:
        try:
            downloaded_good_files = set(os.listdir(downloaded_good_folder))
            print("path valid!")
            break
        except FileNotFoundError as e:
            print(f"Error {e} please reenter the filepath")
            downloaded_good_folder = input().strip(' "')
        except OSError as e:
            print(f"Error {e} please reenter the filepath")
            downloaded_good_folder = input().strip(' "')

    print("please enter file path for the invalid files")
    downloaded_bad_folder = input().strip(' "')
    while True:
        try:
            if downloaded_bad_folder == downloaded_good_folder:
                while True:
                    print("same file path entered. "
                          "if you do not enter a different path"
                          " validation checks will be perform " \
                          "but all files will be put in one folder."
                          " please enter a new file path"
                          )
                    downloaded_bad_folder = input().strip(' "')
                    if downloaded_bad_folder != downloaded_good_folder:
                        break
            downloaded_bad_files = set(os.listdir(downloaded_bad_folder))
            print("path valid!")
            break
        except FileNotFoundError as e:
            print(f"Error {e} please reenter the filepath")
            downloaded_bad_folder = input().strip(' "')
        except OSError as e:
            print(f"Error {e} please reenter the filepath")
            downloaded_bad_folder = input().strip(' "')

    filtered_patient_files = [
        file for file in patient_files if file not in downloaded_bad_files]
    filtered_patient_file = [
        file for file in filtered_patient_files \
        if file not in downloaded_good_files
        ]
    if not filtered_patient_file:
        print("No unseen files in folder")
        return
    else:
        print("files scan successfully, unknown files identified")

    print("please input local file path to " \
          "download all unknown files, for sorting"
          )

    while True:
        try:
            inputs.extend(input().split(","))
            user_data.append(inputs[5].strip(' "'))
            if user_data[5] == downloaded_good_folder:
                while True:
                    print("same file path entered. "
                          "if you do not enter a different path"
                          " the sytem will not have a " \
                          "place to temperaraly store files"
                          " please enter a new file path"
                          )
                    del inputs[5:]
                    del user_data[5:]
                    inputs.extend(input().split(","))
                    user_data.append(inputs[5].strip(' "'))
                    if user_data[5] != downloaded_good_folder:
                        break
            elif user_data[5] == downloaded_bad_folder:
                while True:
                    print("same file path entered. "
                          "if you do not enter a different path"
                          " the sytem will not have a " \
                          "place to temperaraly store files"
                          " please enter a new file path"
                          )
                    del inputs[5:]
                    del user_data[5:]
                    inputs.extend(input().split(","))
                    user_data.append(inputs[5].strip(' "'))
                    if user_data[5] != downloaded_bad_folder:
                        break
            elif user_data[5] == "":
                while True:
                    print("no file path given. please enter a new file path")
                    del inputs[5:]
                    del user_data[5:]
                    inputs.extend(input().split(","))
                    user_data.append(inputs[5].strip(' "'))
                    if user_data[5] != downloaded_bad_folder:
                        break
            path = Path(user_data[5]).resolve(strict=True)
            break
        except FileNotFoundError:
            print("local file path incorrect or invalid " \
                  "please reenter file path"
                  )
            del inputs[5:]
            del user_data[5:]
        except OSError:
            print("local file path incorrect or " \
                  "invalid please reenter file path"
                  )
            del inputs[5:]
            del user_data[5:]

    for files in filtered_patient_file:
        local_path = os.path.join(user_data[5], files)
        with open(local_path, "wb") as newfile:
            ftp.retrbinary(f"RETR {files}", newfile.write)
    ftp.quit()
    print("successfully finished downloading files from FTP server")
    return downloaded_good_folder, downloaded_bad_folder, user_data[5]


# ---------------------------------------------
# unit to check for valid date in csv filename
# ---------------------------------------------
def check_for_valid_format(patient):
    date_numb = patient.split("_")
    date_numb = date_numb.pop(2)
    try:
        numb = ""
        for ch in date_numb:
            if ch.isdigit():
                numb += ch
        date = datetime.strptime(numb, "%Y%m%d%H%M%S")
    except ValueError:
        return False
    else:
        return True


# ----------------------------------------
# unit to check for dup batch ID
# ----------------------------------------


def check_for_dup_batch_ID(patient):
    extracted_batch_ID = []
    patient_data = open(patient, newline="")
    extracted_batch_ID.append([row.split(",")[0] for row in patient_data])
    batch_id = tuple(extracted_batch_ID[0])
    batch_ID = Counter(batch_id)
    ID_amount_list = list(batch_ID.values())
    if any(id != 1 for id in ID_amount_list):
        return False
    else:
        return True

# ---------------------------------------------
# unit to check for invalid header in csv file
# ---------------------------------------------


def check_for_invalid_field_name(patient):
    column_names = open(patient)
    first_column = column_names.readline()
    first_row = first_column.split(",")
    readings = first_row[2:]
    readings_sorted = ";".join(readings)
    readings_sorted = readings_sorted.strip("\n")
    readings_list = ["reading1", "reading2", "reading3", "reading4",
                     "reading5", "reading6", "reading7", 
                     "reading8", "reading9", "reading10"
                     ]
    reading_rejoined = ";".join(readings_list)
    readings_count = len(readings)
    total_columns = len(first_row)
    if readings_sorted != reading_rejoined:
        return False
    elif (total_columns != 12):
        return False
    elif first_row[0] != "batch_id" or first_row[1] != "timestamp":
        return False
    elif readings_count != 10:
        return False
    else:
        return True


# ---------------------------------------------
# unit to check for missing cells in csv file
# ---------------------------------------------

def check_missing_column_row_and_invalid_entries(patient):
    row_of_patient_data = []
    is_row_12 = []
    is_true_or_false = []
    with open(patient, mode="r", newline="") as files:
        data = csv.reader(files)
        for row in data:
            row_of_patient_data.append(row)

    for batches in row_of_patient_data:
        is_row_12.append(len(batches))

    for numb in is_row_12:
        if numb != 12:
            is_true_or_false.append(False)
        else:
            is_true_or_false.append(True)

    if False in is_true_or_false:
        return False
    else:
        return True


# --------------------------------------------------------------
# unit to check for readings larger than 9.9 and amount of \
# reading more than 10
# --------------------------------------------------------------

def check_for_valid_reading_values(patient):
    extracted_patient_readings = []
    patient_data = open(patient, newline="")
    extracted_patient_readings.append(
        [readings.split(",")[2:] for readings in patient_data])
    patient_readings = extracted_patient_readings[0]
    patient_readings = patient_readings[1:]
    patient_readings_len = [len(subset)for subset in patient_readings]
    if 10 not in patient_readings_len:
        return False
    try:
        patient_readings_float = [
            [float(readings) for readings in sublist] for sublist in patient_readings]
    except ValueError:
        return False
    else:
        patient_readings_valid_or_not_valid = [
            [float > 9.9 for float in subset] for subset in patient_readings_float]
        if True in patient_readings_valid_or_not_valid:
            return False
        else:
            return True


# ---------------------------------------------
# unit to check if the file is 0 bytes
# ---------------------------------------------

def check_for_0_byte(file_import):
    file = file_import
    file_size = os.path.getsize(file)
    if file_size == 0:
        return False
    else:
        return True


# ---------------------------------------------------------------------------------
# units to move file from local file to valid file folder or invalid file folder
# ---------------------------------------------------------------------------------

def move_bad_files_unit(file, bad_folder_path):
    bad_file = file
    destination = bad_folder_path
    shutil.move(bad_file, destination)


def move_good_file_unit(file, good_folder_path):
    good_file = file
    destination = good_folder_path
    shutil.move(good_file, destination)

# ----------------------------------------------------------------------------------
# integration of all internal validation check unit to ensure csv file is valid
# ----------------------------------------------------------------------------------


def test_for_valid_file(patient_file):
    patient_file_unknow = check_for_dup_batch_ID(patient_file)
    if patient_file_unknow == True:
        patient_file_unknow = check_for_invalid_field_name(patient_file)
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


# ---------------------------------------------
# integration of all validation checks
# ---------------------------------------------

def test_file_for_true_or_false(file, good_folder, bad_folder):
    patient_data = file
    patient_file_unknown = check_for_valid_format(patient_data)
    if patient_file_unknown == True:
        patient_known_data = test_for_valid_file(patient_data)
        if patient_known_data == True:
            move_good_file_unit(patient_data, good_folder)
            print("file is valid")
        else:
            move_bad_files_unit(patient_data, bad_folder)
            print("file is not valid")
    else:
        move_bad_files_unit(patient_data, bad_folder)
        print("file is not valid")

# ---------------------------------------------
# integration of all units
# ---------------------------------------------


def access_ftp_and_dowload_files():

    file_paths = open_remote_FTP_server_and_download_files()
    if not file_paths:
        print("No files to download, please restart process")
        return
    else:
        file_paths = list(file_paths)
        unknown_file_folder = file_paths[2]
        os.chdir(unknown_file_folder)
        downloaded_files = os.listdir()
        file_number = 1
        goodfolder = file_paths[0]
        badfolder = file_paths[1]
        for files in downloaded_files:
            test_file_for_true_or_false(files, goodfolder, badfolder)
            print(f"preformed validation check on file {file_number}"
                  " and moved file to good file folder or bad file folder")
            file_number += 1

        print("finished validation checks and downloading files")
