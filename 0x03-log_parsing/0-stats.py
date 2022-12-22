#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics:"""
import sys
Status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}
count= 0
size= 0

for input in sys.stdin:
    ListInput = input.split(' ')
    if len(ListInput) > 2:
        Thestatus = ListInput[-2]
        f_size = int(ListInput[-1])
        if Thestatus in Status:
            Status[Thestatus] += 1
    size += f_size
    count += 1
    if count == 10:
        print("File size: {:d}".format(size))
        for key, value in sorted(Status.items()):
            if  value != 0:
                print("{}: {:d}".format(key, value))
        count = 0
   
print("File size: {:d}".format(size))
for key, value in sorted(Status.items()):
    if  value != 0:
        print("{}: {:d}".format(key, value))   