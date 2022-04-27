#!/bin/bash
chown -R root:root serversetup
chmod 755 serversetup/opt/tingleauth/fetch_authorized_keys.py
dpkg-deb --build serversetup