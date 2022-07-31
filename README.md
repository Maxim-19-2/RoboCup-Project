# RoboCup-Project
This repository is a group project submitted by Maxim Smoljar, Maximilian Block and Maximilian Pomplun for the course "RoboCup" taken in the summer semester in 2022.

# How to run the file
In order to run the test.py python 2.7 needs to be installed beforehand, otherwise this will not work. After having installed python 2.7 you can go ahead and download this repository and go to this directory in your console. In your console type:  
```
py -2.7 test.py
```
This should start our programm and make the robot follow the procedure.

Please note that the IP adress in line 6 may need to be changed! 

# procedure
Running the test.py is supposed to make the nao look and search for a red ball. After successfully recognizing a red ball, the nao will track it with his head and point at it with his right arm. If the robot cannot find a red ball, he will turn around and keep searching for it till he finds one.
