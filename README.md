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

Notice: all source codes should be put into the same folder if you want to launch it normally. And if you use different ports for arduino, please change the settings at config.sh

--------------------------------------------------------------------------------
V1.01 NOTE
--------------------------------------------------------------------------------
1.Stability Upgrade (Bug fix): Timestamp string interpuration error risk. E.g. timestamp starting with "08" was mistakenly interpurated as Octal. This issue has been solved in this upgrade.
2.Log system is now made online.
	Desc:
	Table Name: "Log"
	Cols: MSG_Source | MSG_Type | Priority | ERR_ID  | MSG_Index | Stamp   | Date_Time
	Type: String     | String   | Integer  | Integer | String    | integer | Auto_Update_DateTime
	Description:
		MSG_Source could be:
		    Default "Unknown"
			ARDUINO_Board
			ARDUINO_IO
			Control_Service
			Web_Server Browser
			Version
			E.T.C.
		MSG_Type includes:
			Default "Unknown"
			Current_Version
			Version_Update
			Operation_Log
			Error_Log
			Env_Warning
			Msg
		Priority:
			0 -- Commom messages
			1 -- Automatic interpuration needed (This problem might can be solved by the system itself)
			2 -- Mannual interpuration needed (This problem cannot be automatically handeled)
			3 -- IMMEDIATE Mannual interpuation needed (E.g. Tempurature is too high/Serial not responding)
		ERR_ID:
			Default "0"
		    Each known Error have an unique ID. See the chart below for detailed list. The ID is for the control service to try to take corresponding actions to correct it.
		    If the message is not an error, its ID will be "0"
		Stamp:
			Default "0"
			If the message contains an error or a command from web server that needs to be taken care of, the value will be "1" until it is taken care of by control service or manually. (The control service can therefore search for logs whose stamp is 1, and take action on it, and finally change it back to 0)
		Date_Time:
			Auto_Update, intended for manual check.
```
mysql> desc Log;
+------------+--------------+------+-----+-------------------+-----------------------------+
| Field      | Type         | Null | Key | Default           | Extra                       |
+------------+--------------+------+-----+-------------------+-----------------------------+
| MSG_Source | varchar(20)  | NO   |     | Unknown           |                             |
| MSG_Type   | varchar(20)  | NO   |     | Unknown           |                             |
| Priority   | int(11)      | NO   |     | 0                 |                             |
| ERR_ID     | int(11)      | NO   |     | 0                 |                             |
| MSG_Index  | varchar(200) | YES  |     | NULL              |                             |
| Stamp      | int(11)      | NO   |     | 0                 |                             |
| Date_Time  | timestamp    | NO   | PRI | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP |
+------------+--------------+------+-----+-------------------+-----------------------------+
```
3.Version Control is now available:
	By introducing this feature, we do not need to delete the old version everytime we upgrade it. Source code of all versions are stored in the folder, and if we want to roll back, we need only to change the key hardcoded in config.sh. Upon the first running of a new version, a log will be automatically inserted to the log table, so we can keep track on version changes.

List_of_errors:
1 Unspecified Errors
