ATLAS_Part1 _By Yuxuan Zhang

This project, generally speaking, is intended for monitoring the experiment environment (specifically:temperature and hunidity in a closed environment), and make the environment data available though internet.

We use an Arduino board with one (or more) HIH-6130 sensor attached on it, to upload data to a linux PC. The arduino source code Arduino_IO_board.ino and the python source code Arduino_IO_Build.py are available in this folder.

To run the project, you need MySQL/Mariadb ready on your computer, and setup a database named "ATLAS_Main". Also, refer to SQL_Desc.txt for detailed command on how to setup specific tables, and how to GRANT usage to the python code.

Finally, to make everything run automatically, insert the path of launch.sh to the crontab in Linux system using following commands:
```
crontab -e #You will see the vi interface after pressing "Enter"
press key "i"
insert:"* * * * * [path]/launch.sh"
press "esc"
put in ":wq", "Enter"
```
All Done!

Notice: all source codes should be put into the same folder if you want to launch it normally.
