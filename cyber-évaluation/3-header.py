#!/usr/bin/env python3
import sys
name = sys.argv[1] if len(sys.argv) > 1 else "Header"
width = len(name) + 4
print("*" * (width + 2))
print(f"* {name} *")
print("*" * (width + 2))
