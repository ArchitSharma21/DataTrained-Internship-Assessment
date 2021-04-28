# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 11:21:49 2021

@author: Dell
"""

import math 

def udf_factorial(n):
    factorial = 1;
    for i in range(2, n+1):
        factorial = factorial * i
    return factorial

lambda_factorial = lambda n : math.factorial(n)

def main():
    print("Choose the method for calculating factorial \n 1) User Defined Function \n 2) Lambda Function")
    a = int(input())
    print("Give number for which you want to calculate factorial")
    n = int(input())
    if a == 1:
        print("The factorial of "+str(n)+" is "+str(udf_factorial(n)))
    elif a == 2:
        print("The factorial of "+str(n)+" is "+str(lambda_factorial(n)))
    else:
        print("Invalid option")
    
        
main()
