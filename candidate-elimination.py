# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 11:59:15 2019

@author: Soumaya
"""
# # Candidate Elimination Algorithm:
# ##Algorithm:
# 1. G <- manually general hypothesis in H
# 2. S <- manually specific hypothesis in H
# 3. For each training example d,do
#   i.  If d is a positive example then:
#       a. Remove from G any hypothesis inconsistent with d
#       b. For each hypothesis s in S that is not consistent with d
#           a. Remove s from S
#           b. Add to S all minimal generalizations h of s such that h is consistent with d , and some member of G is more general than h
#           c. Remove from S any hypothesis that is more general than another hypothesis in S
#   ii. else if d is a negative example:
#       a. Remove from S any hypothesis inconsistent with d
#       b. For each hypothesis g in G that is not consistent with d
#           a. Remove g from G
#           b. Add to G all minimal specializations h of g such that h is consistent with d , and some member of S is more specific than h .
#           c. Remove from G any hypothesis that is less general than another hypothesis in G
# #
import csv
a = []
with open('candidate.csv', 'r') as trainData:
    for row in csv.reader(trainData):
        a.append(row)
        print(row)
n=len(a[0])-1

print("\n The initial value of hypothesis: ")
s = ['0'] * n
g = ['?'] * n
print ("\n The most specific hypothesis S0 :",s)
print (" \n The most general hypothesis G0 :",g)

s=a[0][:-1]
temp=[]
print("\n Candidate Elimination algorithm\n")

for i in range(len(a)):
    if a[i][n]=="yes":
        for j in range(n):
            if a[i][j]!=s[j]:
                s[j]='?'
        for j in range(n):
            for k in range(len(temp)-1):  #Use len(temp)-1 for manufacture.csv
                if temp[k][j]!='?' and temp[k][j]!=s[j]:
                    del temp[k] 
        
    if a[i][n]=="no": 
        for j in range(n):
             if s[j]!=a[i][j] and s[j]!='?': 
                 g[j]=s[j]
                 if g not in temp:
                  temp.append(g) 
                 g= ['?']*n

    print("\n For Training Example No :{0} the hypothesis is S{0} ".format(i+1),s)
    if (len(temp)==0):
            print(" For Training Example No :{0} the hypothesis is G{0} ".format(i+1),g)
    else:
            print(" For Training Example No :{0} the hypothesis is G{0}".format(i+1),temp)
