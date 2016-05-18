#!/bin/python3

import sys

def getNumberOfThrees(n):
    noOfThrees=0
    originalNumber=n
    while(n >2):
        reducedDigits=n-5
        if(reducedDigits%3 == 0):
            noOfThrees=originalNumber-reducedDigits
            break
        n=reducedDigits
    return noOfThrees

def makeNumber(noOfFives,noOfThrees):
    
    numberString='';
    for i in range(noOfFives):
        numberString+='5'
        
    for i in range(noOfThrees):
        numberString+='3'
        
    return numberString  

def getLargestDecentNumber(n):
    if(n%3==0):
        decentNumber=makeNumber(n,0)
    else:
        noOfThrees=getNumberOfThrees(n)
        if(noOfThrees==0):
            decentNumber=-1
        else:
            decentNumber=makeNumber(n-noOfThrees,noOfThrees)
            
    return decentNumber