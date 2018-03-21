#!/usr/bin/env python
##
## Read serial data and record temperature data.
## Save output to ROOT file as well as plain text.
##

import sys
import argparse
import serial
import time
import signal
import MySQLdb
from array import array
from datetime import datetime

Debug=False

err_file_route=''
err_table=''
err_level=['MESSAGE','EXCEPTION','ERROR(L1)','ERROR(L2)','ERROR(L3)','BREAKDOWN']

class data_unit:
  flag=''
  val=0.0
  table_name=''
  def flag_def(self,def_flag):
    self.flag=def_flag
  def find_table_name(self,InputExpect_str):
    p_str=InputExpect_str.find('$'+self.flag+'@')
    if (self.flag!='' and p_str!=-1): 
      Target_str=InputExpect_str[p_str+len(self.flag)+2:]
      Target_str=Target_str[:Target_str.find('$')]
      self.table_name=Target_str

def report_MSG(error_level,error_string):
  if(err_file_route!=''): 
    try:
      err_out = open(err_file_route, 'a')
    except:
      err_out = open(err_file_route, 'w')
    err_out.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+' '+err_level[error_level]+' '+error_string+'\n')
    err_out.close()
  #if(err_table!=''):
    #not an online feature 

def fetch_data(Port, baudrate, time_out, timestamp, Host, User, Password, Database, Table, InputExpect):
  #Start Database Connection
  if Debug: db = MySQLdb.connect(Host, User, Password)
  else:
    try:
      if Debug: print('Connecting to Database using Host:'+Host+' User:'+User+' Password:'+Password)
      db = MySQLdb.connect(Host, User, Password)
    except:
      report_MSG(3,"ERROR:Data_Base_Connection_Failed");
      sys.exit(1)
  #Start Serial Connection
  if Debug: serial_port = serial.Serial(Port, baudrate, timeout=time_out)
  else:
    try:
      serial_port = serial.Serial(Port, baudrate, timeout=time_out)
    except serial.serialutil.SerialException:
      report_MSG(3,'ERROR:Serial_Port '+Port+' Not_Responding;');
      sys.exit(1)
  #Fetch RAW
  serial_port.writelines("<DATA>")
  sleep(0.05)
  RAW_Data_str=serial_port.readline()
  #Pick out error messages
  if RAW_Data_str.count('#')%2==1:
    report_MSG(2,'ERROR:INVALID_Serial_INPUT:'+RAW_Data_str)
    sys.exit(1)
  while(RAW_Data_str.find('#')!=-1):
    err_str=RAW_Data_str[RAW_Data_str.find('#')+1:]
    err_str=err_str[:err_str.find('#')]
    report_MSG(2,err_str)
    temp_str=RAW_Data_str[:RAW_Data_str.find('#')]
    RAW_Data_str=RAW_Data_str[RAW_Data_str.find('#')+1:]
    RAW_Data_str=RAW_Data_str[RAW_Data_str.find('#')+1:]
    RAW_Data_str=temp_str+RAW_Data_str
  #Pick out values
  #if ()




    
if __name__ == '__main__':
    
  parser = argparse.ArgumentParser(description='Read serial data and record temperature data.', usage='%(prog)s [options]', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  parser.add_argument('--port',           default='/dev/ttyACM1',   help='input serial port')
  parser.add_argument('--baudrate',       type=int,             default=9600,   help='baud rate')
  parser.add_argument('--timeout',        type=float,           default=0.8,    help='timeout for serial reading [s]')
  parser.add_argument('--timestamp',      type=float,           default=0,      help='timestamp')
  parser.add_argument('--host',           default='localhost',  help='Database Host')  
  parser.add_argument('--user',           default='ArduinoIO', help='Database username')
  parser.add_argument('--password',       default='pxKr_AIO',   help='Database password')
  parser.add_argument('--Database',       default='ATLAS_Main', help='Name of Database')
  parser.add_argument('--Table',          default='ARDUINO_IO', help='Name of Target Table')
  parser.add_argument('--ErrorTable',     default='NA',         help='Target Error Table')
  parser.add_argument('--ErrorFile',      default='AIO_Errors.txt',      help='Target Error TXT file')
  parser.add_argument('--InputExpect',    default='$T@Env_Temp$H@Env_Humidity$',help='Sign of datatype and corresponding column name')
  parser.add_argument('--Debug',          default=False,        action='store_true', help='Do not print to screen.')
  
  args = parser.parse_args(sys.argv[1:])
  Debug=args.Debug
  err_file_route=args.ErrorFile
  err_table=args.ErrorTable
  time.time() if args.timestamp==0 else args.timestamp;
  fetch_data(args.port, args.baudrate, float(args.timeout), args.timestamp, args.host, args.user, args.password, args.Database, args.Table, args.InputExpect)
  sys.exit(0)
  
