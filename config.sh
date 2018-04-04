#!/bin/bash
#Author:Yuxuan Zhang

#-----------------------------------------------------
#------------------Global Arguments-------------------
#-----------------------------------------------------
Version="V1.01"
AIO_path='/Arduino_IO_Build.py'
CTL_path='Not_Specified'
#-----------------------------------------------------
#------------------ARDUINO_IO Arguments---------------
#-----------------------------------------------------
AIO_port='--port /dev/ttyACM1' #ARGS>1
AIO_baudrate='--baudrate 9600'  #ARGS>2
AIO_timeout='--timeout 1' #ARGS>3
AIO_timestamp='--timestamp' #ARGS>4 #Do not worry, the stamp will be given later
AIO_host='--host localhost' #ARGS>5
AIO_user='--user ArduinoIO' #ARGS>6
AIO_password='--password pxKr_AIO' #ARGS>7
AIO_Database='--Database ATLAS_Main' #ARGS>8
AIO_Table='--Table ARDUINO_IO' #ARGS>9
AIO_ErrorTable='--ErrorTable NA' #ARGS>10
AIO_ErrorFile='--ErrorFile AIO_Errors.txt' #ARGS>11
AIO_InputExpect='--InputExpect $T@Env_Temp$H@Env_Humidity$' #ARGS>12
AIO_Debug=' ' #ARGS>13
#-----------------------------------------------------
#------------------Other Arguments--------------------
#-----------------------------------------------------
