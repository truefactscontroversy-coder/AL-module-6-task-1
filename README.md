welcome to the readme file for this file validing program

This programs is designed to
1. download file from an FTP server
2. sort downloaded files to ensure that data is valid 


Once the docker contianer is built the program will prompt you to 
input host number and port number (you will need to enter these two with a comma more instructions will appear on the screen)
once connected the program will prompt you to 
input the username and password for the FTP server (this also needs to be entered seperated by a (,))
then the program will ask for three folder paths in this order 
1. folder to store files with valid data
2. folder to store files with invalid data
3. folder to store files downloaded form FTP 
note: these folder need to be the same ones mounted in the beginning 

in order for the container to properly run you will need to uses the docker command provided below

docker run -it --rm -v "add your own file path:/placeholder foldername/foldername" -v "add your own file path:/placeholder foldername/foldername" -v "add your own file path:/placeholder foldername/foldername" python-module_6_task_1.py:v1

"docker run -it" this starts the container 

"--rm" this remove the contianer after the program finishes running this ensures there is no error when the program ends

"-v" this tell docker to mount the file 

":" this is vital to tell docker to create a path within the container, without it the file paths will not have anywhere to go inside the docker

"/placeholder foldername" this is the main folder inside the docker that will hold all the other folders (i.e. /foldername)

"/foldername" this is the path for each specific folder, for example is the first mounted file path is for vaild data then i would name the folder "/vaild_data"



