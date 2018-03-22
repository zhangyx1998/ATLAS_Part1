#!/bin/bash
#Author:YuxuanZhang
C_DIR="$( cd "$( dirname "$0" )" && pwd )"
#echo $C_DIR
source "$C_DIR"/config.sh
TS_DT=`date "+%Y-%m-%d %H:%M:%S"`
#echo $TS_DT
TS_HS=`date -d "$TS_DT" +%s`
#echo $TS_HS
TS=$((TS_HS*1000+`date "+%N"`/1000000))
#echo $TS
AIO_timestamp="${AIO_timestamp} $TS"
AIO_Debug="--Debug"
python $C_DIR'/'$AIO_path $AIO_Debug $AIO_port $AIO_baudrate $AIO_timeout $AIO_timestamp $AIO_host $AIO_user $AIO_password $AIO_Database $AIO_Table $AIO_ErrorTable $AIO_ErrorFile $AIO_InputExpect
