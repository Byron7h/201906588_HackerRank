#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    n = int(input().strip())  
    prueba = n%2 
  
    if prueba == 0:
    
        if n>1 and n<6:
            print("Not Weird")

        elif n>5 and n<21:
            print("Weird")

        else:
            print("Not Weird")

    else:
        print("Weird")