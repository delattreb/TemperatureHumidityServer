#!/bin/sh
# Synology DSM bootup script
# Configured Variables:
PYTHON_EXEC="/volume1/@appstore/py3k/usr/local/bin/python3.5"
SCRIPT_EXEC="/volume1/web/temperaturehumidityserver/runserverwebservices.py"

# Begin script
case "$1" in
start)
  PATH=$PATH:/volume1/web/temperaturehumidityserver/
  printf "%-30s" "Starting script"
  ${PYTHON_EXEC} ${SCRIPT_EXEC} &
  printf "[%4s]\n" "done"
 ;;
stop)
  printf "%-30s" "Stopping script"
  printf "[%4s]\n" "done"
  ;;
*)
  echo "Usage: $0 {start|stop}"
  exit 1
esac

exit 0
