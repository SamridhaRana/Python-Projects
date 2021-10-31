# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:11:10 2020

@author: jonathanreaban17
"""


import tkinter
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

import  matplotlib.pyplot as plt



def func():
    a = float(entry1.get())
    c = float(entry2.get())
    t = float(entry3.get())
    Ta = float(entry4.get())
    I0 = float(entry5.get())
    d = float(entry6.get())
    G = float(entry7.get())
    EX = float(entry8.get())
    IM0 = float(entry9.get())
    mpm = float(entry10.get())
    
    MD0 = float(entry11.get())
    e = float(entry12.get())
    f = float(entry13.get())
    I = float(entry14.get())
    MBn = float(entry15.get())
    DL0 = float(entry16.get())
    slopeDL = float(entry17.get())
    ID = float(entry18.get())
    cd = float(entry19.get())
    rD = float(entry20.get())
    erd = float(entry21.get())
   
   
   
    Y = [5500,6000,6111.73,6500,6700,6800,6900,7000,7100,7200,7300,7400,7500]
    investmentsavings = [29.58333,21.25,19.387804,12.916667,9.583333,7.916667,6.25,4.583333,2.916667,1.25,-0.416667,-2.083333,-3.75]
    liquidity = [-40.92466614,-24.67466614,-21.0433845,-8.424666138,-1.924666138,1.325333862,4.575333862,7.825333862,11.07533386,14.32533386,17.57533386,20.82533386,24.07533386]
   
# =============================================================================
#     MD0 = 450
#     e = 0.65
#     f = -20
#     I = 804
#     MBn = 2000
#     DL0 = 100
#     slopeDL = -5
#     ID = 5
#     cd = .45 #{C/D}
#     rD = .07
#     erd = .0014
# =============================================================================
   
    P = 1.153020335
    Pprime = 1.1530203
   
    a1 = 800
    c1 = 0.7
    t1 = 0
    Ta1 = 600
    I01 = 1200
    d1 = -24
    G1 = 1200
    EX1 = 700
    IM01 = 200
    mpm1 = .1
   
    interLM = (MD0 - ((1+cd)*(MBn+DL0+slopeDL*ID)/(rD+cd+erd)) + I*P)/(-1*f)
    slopeLM = e/(-1*f)
    interLMPprime = (MD0 - ((1+cd)*(MBn+DL0+slopeDL*ID)/(rD+cd+erd)) + I*Pprime)/(-1*f)
   
    interIS = (a - (c-mpm)*Ta+I0+G+EX-IM0)/d * -1
    slopeIS = (1-(c-mpm)*(1-t))/d
   
    Ystar = (interLM-interIS)/(slopeIS-slopeLM)
    Ms = ((1+cd)*(MBn + DL0 + slopeDL * ID )/(rD+cd+erd))
    rstar = interLM + slopeLM * Ystar
    BD = (G-Ta-(t*Ystar))
    Ip = I0 + (d * rstar)
   
   
    rISprime = []
    rLMprime = []
    for i in range(len(Y)):
        rISprime.append(interIS + slopeIS * Y[i])
        rLMprime.append(interLM + slopeLM * Y[i])
       
    #print(rISprime)
    #print(rLMprime)
   
    fig = plt.figure()
    plot1 = fig.add_subplot(111)
    #plot1.add_axes([0,0,1,1])
    plot1.set_xlabel('Real Income')
    plot1.set_ylabel('Real Interest Rate')
    plot1.set_title('ISLM model')
    plot1.scatter(Y,investmentsavings,color = 'r')
    plot1.scatter(Y,liquidity,color = 'b')
    plot1.scatter(Y,rISprime,color = 'g')
    plot1.scatter(Y,rLMprime,color = 'y')
    plot1.plot(Y,investmentsavings)
    plot1.plot(Y,liquidity)
    plot1.plot(Y,rISprime)
    plot1.plot(Y,rLMprime)

    #plt.show()
   
 
 
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
 
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().grid(row = 16, column = 0, columnspan = 4)
 
    # creating the Matplotlib toolbar

    #toolbar = NavigationToolbar2Tk(canvas, window)
    #toolbar.update()
 
    # placing the toolbar on the Tkinter window
    #canvas.get_tk_widget().grid(row=16, column = 0, columnspan = 4)
   
   

window = tkinter.Tk()
# to rename the title of the window
window.title("ISLM MODEL")
# pack is used to show the object in the window
#label = tkinter.Label(window, text = "Welcome to ISLM model ").grid(row=1, column = 0)

#top_frame = tkinter.Frame(window).pack()
#btn2 = tkinter.Button(top_frame, text = "Calculate", fg = "green").pack()

btn_convert = tkinter.Button(
    master=window,
    text="Build Plot",
    command=func,
    bg = 'palegreen'
)
btn_convert.grid(row=15, column = 1)


label = tkinter.Label(text = "Written By: Rana", bg = 'palegreen').grid(row=3, column = 0, columnspan = 4)

label1 = tkinter.Label(text = "Autonomous Consumer Spending:").grid(row=4, column = 0)
entry1 = tkinter.Entry()
entry1.grid(row=4, column = 1)
entry1.insert(0,800)

label2 = tkinter.Label(text = "Marginal Propensity to Consume:").grid(row=5, column = 0)
entry2 = tkinter.Entry()
entry2.grid(row=5, column = 1)
entry2.insert(0,0.7)

label3 = tkinter.Label(text = "Rate of Income Tax:").grid(row=6, column = 0)
entry3 = tkinter.Entry()
entry3.grid(row=6, column = 1)
entry3.insert(0,0)

label4 = tkinter.Label(text = "Autonomous Taxes:").grid(row=7, column = 0)
entry4 = tkinter.Entry()
entry4.grid(row=7, column = 1)
entry4.insert(0,600)

label5 = tkinter.Label(text = "Autonomous IP").grid(row=8, column = 0)
entry5 = tkinter.Entry()
entry5.grid(row=8, column = 1)
entry5.insert(0,1200)

label6 = tkinter.Label(text = "delta IP/delta r:").grid(row=9, column = 0)
entry6 = tkinter.Entry()
entry6.grid(row=9, column = 1)
entry6.insert(0,-24)

label7 = tkinter.Label(text = "Government Spending:").grid(row=10, column = 0)
entry7 = tkinter.Entry()
entry7.grid(row=10, column = 1)
entry7.insert(0,1200)

label8 = tkinter.Label(text = "EX:").grid(row=11, column = 0)
entry8 = tkinter.Entry()
entry8.grid(row=11, column = 1)
entry8.insert(0,700)

label9 = tkinter.Label(text = "Autonomous Import Spending:").grid(row=12, column = 0)
entry9 = tkinter.Entry()
entry9.grid(row=12, column = 1)
entry9.insert(0,200)

label10 = tkinter.Label(text = "Marginal Propensity Import:").grid(row=13, column = 0)
entry10 = tkinter.Entry()
entry10.grid(row=13, column = 1)
entry10.insert(0,.1)

label11 = tkinter.Label(text = "MD0:").grid(row=4, column = 2)
entry11 = tkinter.Entry()
entry11.grid(row=4, column = 3)
entry11.insert(0,450)

label12 = tkinter.Label(text = "e:").grid(row=5, column = 2)
entry12 = tkinter.Entry()
entry12.grid(row=5, column = 3)
entry12.insert(0,0.65)

label13 = tkinter.Label(text = "-f:").grid(row=6, column = 2)
entry13 = tkinter.Entry()
entry13.grid(row=6, column = 3)
entry13.insert(0,-20)

label14 = tkinter.Label(text = "I:").grid(row=7, column = 2)
entry14 = tkinter.Entry()
entry14.grid(row=7, column = 3)
entry14.insert(0,804)

label15 = tkinter.Label(text = "MBn").grid(row=8, column = 2)
entry15 = tkinter.Entry()
entry15.grid(row=8, column = 3)
entry15.insert(0,2000)

label16 = tkinter.Label(text = "DL0:").grid(row=9, column = 2)
entry16 = tkinter.Entry()
entry16.grid(row=9, column = 3)
entry16.insert(0,100)

label17 = tkinter.Label(text = "Slope DL:").grid(row=10, column = 2)
entry17 = tkinter.Entry()
entry17.grid(row=10, column =3)
entry17.insert(0,-5)

label18 = tkinter.Label(text = "ID:").grid(row=11, column = 2)
entry18 = tkinter.Entry()
entry18.grid(row=11, column = 3)
entry18.insert(0,5)

label19 = tkinter.Label(text = "{C/D}:").grid(row=12, column = 2)
entry19 = tkinter.Entry()
entry19.grid(row=12, column = 3)
entry19.insert(0,0.45)

label20 = tkinter.Label(text = "rD:").grid(row=13, column = 2)
entry20 = tkinter.Entry()
entry20.grid(row=13, column = 3)
entry20.insert(0,0.07)

label21 = tkinter.Label(text = "{ER/D}:").grid(row=14, column = 2)
entry21 = tkinter.Entry()
entry21.grid(row=14, column = 3)
entry21.insert(0,0.0014)

window.mainloop()