import os
import sys
from time import sleep

file_name = sys.argv[1]

print('waiting for file', file_name)

while not os.path.exists(file_name):
    sleep(0.1)
