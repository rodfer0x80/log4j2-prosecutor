#!/usr/bin/python3

from .pwn import Pwn

if __name__== '__main__':
    domain = "127.0.0.1:3001"
    try:
        with open("exploit_configs.txt", 'r') as fp:
            data = fp.read().split("\n")
    except IOError:
        stderr.write("Error reading exploit configurations")
        exit(0)
    url = data[1][4:]
    data = data[4:]
    params = list()
    for line in data:
        params.append(line.split()[0])

    exploit = Pwn(url, domain, params)

