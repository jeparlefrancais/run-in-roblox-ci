import os
import sys
from time import sleep

file_name = sys.argv[1]

while not os.path.exists(file_name):
    sleep(0.1)
