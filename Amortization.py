# Write a function in python that returns the initial 
# investment necessary for an annuity to run out 
# in M months at a monthly rate i and monthly withdrawal w 
# in dollars. Test with your own examples. 
# Check your examples with another computational 
# source besides your code.

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def calcPrincipal(months, interestRate, withdrawal):
    an = 0
    for i in range(0, months):
        an = (an + withdrawal)*(1/(1+interestRate))
    return an

def effInterestCalc(APR, compoundingPeriod):
    if compoundingPeriod == 'annually':
        N = 1
    elif compoundingPeriod == 'semi-annually':
        N = 2
    elif compoundingPeriod == 'quarterly':
        N = 4
    elif compoundingPeriod == 'monthly':
        N = 12
    elif compoundingPeriod == 'weekly':
        N = 52
    else:
        N = 365
    return ((1+(APR/N)/100)**N - 1)*100

def graphEffInterest(APR):
    compoundingPeriods = ['annually', 'semi-annually', 'quarterly', 'monthly', 'weekly', 'daily']
    effInterests = []
    for period in compoundingPeriods:
        effInterests.append(effInterestCalc(APR, period))
    plt.scatter(compoundingPeriods, effInterests)
    plt.show()

#an = C * (r)^n - (b/1-r)
def amortization(APR, principal, months):
    i = APR/12.0/100
    amortizationSchedule = []
    monthlyPayment = principal*((1-(1+i))/(1-(1+i)**months) + i)
    totalPaid = monthlyPayment * months
    interestPayment = []
    principalPayment = []
    sum = 0
    for j in range(0, months):
        interest = i*(principal - sum)
        principall = monthlyPayment - interest
        interestPayment.append(interest)
        principalPayment.append(principall)
        sum += principalPayment[j]
    amortizationSchedule.append(interestPayment)
    amortizationSchedule.append(principalPayment)
    y = pd.DataFrame(amortizationSchedule)
    y
    return monthlyPayment, amortizationSchedule, totalPaid

def amortizationGraph(amortizationSchedule):
    N = len(amortizationSchedule[0])
    width = 1
    ind = np.arange(N)
    p1 = plt.bar(ind, amortizationSchedule[0], width, color='r')
    p2 = plt.bar(ind, amortizationSchedule[1], width, color='g',bottom=amortizationSchedule[0])
    plt.show()
#print(calcPrincipal(240, .01, 1000))
#print(effInterestCalc(20, 'daily'))
#graphEffInterest(12)
payment, schedule, total = amortization(6.0, 30000, 60)
amortizationGraph(schedule)