#!/bin/sh

# script to get code from github (even as I write this it sounds dumb)

echo "Starting get script"
echo "exit on failure"
set -e

# change to home directory
cd ~/.

# the script requires the name of the script to download and install
if [ $# = 0 ]
then
        echo "Run using the following command:"
        echo " "
        echo " sudo sh get.sh script_name"
        echo " "
        echo " The script requires the name of the script to download and install"
        echo " ERROR: exiting"
        exit 1
fi

# $1 is script_name
# exit status of last command executed $?

# download code from github
echo "Get script"
wget "https://raw.githubusercontent.com/dumbo25/smart-doorbell/master/$1.py"
echo "...change permissions"
chmod +x $1.py
echo "...move script to correct directory"
mv $1.py /usr/local/bin/.

echo "/nGet service"
wget "https://raw.githubusercontent.com/dumbo25/smart-doorbell/master/$1.service"
echo "...change owner of service"
chown root:root $1.service
echo "...move service to correct directory"
mv $1.service /lib/systemd/system/.

echo "/nStart the service running"
echo "...Reload daemon"
systemctl daemon-reload
echo "...enable the service"
systemctl enable $1.service
echo "...check if service is enabled"
systemctl list-unit-files | grep enabled | grep $1
echo "...start the service"     # check if the service is enabled
systemctl start $1.service
echo "...check if the service is running"
systemctl | grep running | grep $1

echo "/nCheck if there are any issues with the service"
journalctl -u $1.service

echo "/nSuccess - exiting"
