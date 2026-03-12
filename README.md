welcome to the readme file for this file validing program

This programs is designed to
1. download file from an FTP server
2. sort downloaded files to ensure that data is valid 

In order to run the container properly you need to build the contianer with this command
placeholder
this will download all dependencies and mount the folders you will need to store the file

Once the docker contianer is built the program will prompt you to 
input host number and port number (you will need to enter these two with a comma more instructions will appear on the screen)
once connected the program will prompt you to 
input the username and password for the FTP server (this also needs to be entered seperated by a (,))
then the program will ask for three folder paths in this order 
1. folder to store files with valid data
2. folder to store files with invalid data
3. folder to store files downloaded form FTP 
note: these folder need to be the same ones mounted in the beginning 

please create a file labeled requirments.txt and then paste these requirements inside

pytest
flask
requests

the name of the file should be "requirments.txt"

the only thing in the file should be these lines each seperated by a line breake
pytest
flask
requests
