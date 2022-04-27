#!/bin/bash
/usr/bin/apt update -q -y >> /var/log/apt/automaticupdates.log
/usr/bin/apt upgrade -q -y tingle-server-setup >> /var/log/apt/automaticupdates.log