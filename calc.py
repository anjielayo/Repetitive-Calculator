# -*- coding: utf-8 -*-
"""
Created on Fri May 14 14:43:52 2021

@author: Anjolaoluwa
"""

"""Creating a simple repetitive calculator"""
while True:
    op=input("Enter the operation: +,-,/,*: ")
    if op =="+":
        n=float(input("Enter the first number: "))
        ns=float(input("Enter the next number: "))
        n=n+ns
        print(n)
        q=input("Continue?(Y/N): ").lower()
        if q=="y":
            continue
        else:
            break
    elif op=="-":
        n=float(input("Enter the first number: "))
        ns=float(input("Enter the next number: "))
        n=n-ns
        print(n)
        q=input("Continue?(Y/N): ").lower()
        if q=="y":
            continue
        else:
            break
    elif op=="*":
        n=float(input("Enter the first number: "))
        ns=float(input("Enter the next number: "))
        n=n*ns
        print(n)
        q=input("Continue?(Y/N): ").lower()
        if q=="y":
            continue
        else:
            break
    elif op=="/":
        n=float(input("Enter the first number: "))
        ns=float(input("Enter the next number: "))
        n=n/ns
        print(n)
        q=input("Continue?(Y/N): ").lower()
        if q=="y":
            continue
        else:
            break