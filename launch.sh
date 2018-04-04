#!/bin/bash
#Author:YuxuanZhang
C_DIR="$( cd "$( dirname "$0" )" && pwd )"
#echo $C_DIR
source "$C_DIR"/config.sh
TS_SC=(`date +%s`)
TS_MS=(`date "+%N"`/1000000)
TS_MS=${TS_SC#0}
TS=$[$TS_SC*1000+TS_MS]
#echo $TS
AIO_timestamp="${AIO_timestamp} ${TS}"
#echo $AIO_timestamp
python $C_DIR'/'$AIO_path'_'$Version'.py' $AIO_Debug $AIO_port $AIO_baudrate $AIO_timeout $AIO_timestamp $AIO_host $AIO_user $AIO_password $AIO_Database $AIO_Table $AIO_LogTable $AIO_LogFile $AIO_InputExpect $1
