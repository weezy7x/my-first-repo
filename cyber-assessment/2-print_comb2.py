#!/usr/bin/python3
import sys
for i in range(100):
    sys.stdout.write("%02d" % i + (", " if i < 99 else "\n"))
