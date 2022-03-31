#shouln't need this anymore
from __future__ import print_function

with open('angles_list.txt') as f:
    list = f.read().split('\n')
list = list[:-1] #remove empty element ' ' that is accidently created

print (list)

int_list = map(float, list)

print (int_list)