# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 13:09:29 2020

@author: Samridha and Reaban
"""
import numpy as np
from scipy.stats import norm
import time

def europeanOption(So,K,T,s,r,option_type,M):
   
    d1 =( np.log(So/K) + (r + ((s**2)/2))*T)/(s * np.sqrt(T))
    d2 = d1-(s*np.sqrt(T))
   
    if option_type == "call":
        call = So * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
        return call
    elif option_type == "put":
        put = K * np.exp(-r * T) * norm.cdf(-d2)-So * norm.cdf(-d1)
        return put


def monte_carlo(S0, K, T, M, s, r, option_type):
  dt = T/M
  S = [S0]
  for i in range(1, M):
    S.append(S[-1]*(1 + r*dt + s*np.random.standard_normal()*np.sqrt(dt)))
  payoff = -1
  if option_type == 'call':
    payoff = np.exp(-1*r*T)*max(S[-1]-K, 0)
  elif option_type == 'put':
    payoff = np.exp(-1*r*T)*max(K-S[-1], 0)
  else:
    print( 'Try again BIATCH')

  return S, payoff



def calc_ave(S0, K, T, M, s, r, option_type, W):
  sum = 0
  for i in range(0, W):
    a,b = monte_carlo(20, 20, 1, M, .25, .05, option_type)
    sum += b
  return (sum/W)



import matplotlib.pyplot as plt
def graph(S0, K, T, M, s, r,option_type):
  x = []
  for i in range(0, M):
    x.append(i)
  for i in range(0, 5):
    y, v = monte_carlo(S0, K,T, M, s, r,option_type)
    plt.plot(x, y)
    print(y)
  plt.show()
graph(20,20, 1, 365, .25, .05,'put')


def graph_option_value_M_Varies(S0, K, T, M, s, r, option_type, W):
    exact_val_list = []
    walk_val_list = []
    m_list = []
    for i in range(200, 20001, 200):
        exact_val = europeanOption(S0,K,T,s,r,option_type,i)
        exact_val_list.append(exact_val)
        walk_val_list.append(calc_ave(S0, K, T, i, s, r, option_type, W))
        m_list.append(i)
    plt.plot(m_list, exact_val_list, color = 'r')
    plt.plot(m_list, walk_val_list, color = 'g')
    plt.show()

#graph_option_value_M_Varies(20,20, 1, 365, .25, .05,'put', 1000)



def plot_time_for_M():
    m_list = []
    time_list = []
    for i in range(200, 20000, 200):
        timeStart = time.time()
        calc_ave(20, 20, 1, i, .25, .05,'call', 100)
        timeEnd = time.time()
        m_list.append(i)
        time_list.append(timeEnd-timeStart)
    plt.plot(m_list, time_list)
    plt.show()
#plot_time_for_M()
   
def plot_time_for_W():
    m_list = []
    time_list = []
    for i in range(200, 20000, 200):
        timeStart = time.time()
        calc_ave(20, 20, 1, 365, .25, .05,'call', i)
        timeEnd = time.time()
        m_list.append(i)
        time_list.append(timeEnd-timeStart)
    plt.plot(m_list, time_list)
    plt.show()
#plot_time_for_W()


   
def graph_option_value_W_Varies(S0, K, T, M, s, r, option_type, W):
    exact_val_list = []
    walk_val_list = []
    m_list = []
    for i in range(100, 10000, 100):
        exact_val = europeanOption(S0,K,T,s,r,option_type,M)
        exact_val_list.append(exact_val)
        walk_val_list.append(calc_ave(S0, K, T, M, s, r, option_type, i))
        m_list.append(i)
    plt.plot(m_list, exact_val_list, color = 'r')
    plt.plot(m_list, walk_val_list, color = 'g')
    plt.show()

#graph_option_value_W_Varies(20,20, 1, 500, .25, .05,'call', 1000)