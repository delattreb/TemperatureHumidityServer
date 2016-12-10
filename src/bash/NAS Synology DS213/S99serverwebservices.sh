#!/bin/sh
#
# S99serverwebservice - Lancement
# Copier dans /usr/syno/etc.defaults/rc.sysv/
#
PATH=/bin:/usr/bin

case $1 in
start)
cd /volume1/web/TemperatureHumidityServer
python3.5 runserverwebservices.sh
exit 0
;;
stop)
exit 0
;;
*)
esac

