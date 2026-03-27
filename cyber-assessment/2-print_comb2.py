#!/usr/bin/python3
result = ""
for i in range(100):
    if i < 99:
        result += str(i).zfill(2) + ", "
    else:
        result += str(i).zfill(2)
print(result)
