#!/bin/bash
JAVAFILE=$1
JAVAMAIN="Main.java"
if [ -z $JAVAFILE ]; then
	echo "Usage: ./java-single-compile.sh <Main.java>" &&\
		exit
else
	cat $JAVAFILE > $JAVAMAIN
		export PATH="/usr/local/opt/openjdk/bin:$PATH" &&\
		CPPFLAGS="-I/usr/local/opt/openjdk/include" &&\
		javac $JAVAMAIN &&\
		rm -f $JAVAMAIN
fi
