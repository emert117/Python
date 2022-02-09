
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print("Enter a number: ", end=' ')
    n = int(input().strip())
    if n % 2 == 1:
        print("odd")
    else:
        print("even")

    second_input = str(input())
    print(f"second input: {second_input}")