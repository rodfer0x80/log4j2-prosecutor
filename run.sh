#!/bin/bash
cd http-server && node index.js &
sleep 2
cd ldap-server && node index.js 
