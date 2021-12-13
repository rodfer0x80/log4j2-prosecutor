#!/bin/bash
cd http-server && node index.js 2>&1 &
sleep 2
cd ldap-server && node index.js 2>&1 & 
