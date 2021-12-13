#!/bin/bash
export PATH="/usr/local/opt/openjdk/bin:$PATH" &&\
	CPPFLAGS="-I/usr/local/opt/openjdk/include" &&\
	cd log4j-client &&\
	gradle jar &&\
	java -Dcom.sun.jndi.ldap.object.trustURLCodebase=true -jar build/libs/log4j-client-1.0-SNAPSHOT.jar
