from ExcelCalc import *
import matplotlib.pyplot as plt
import numpy as np
#function to plot values in the upper side of the bar
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
#First Graph
diaxorismosy=np.arange(0,25000000,2500000)
label=[2011,2012,2013,2014] # what it will be shown in x axis
x_cord=[1,2,3,4] #where the label will be put
height_cord=[TouristsPerYear[0],TouristsPerYear[1],TouristsPerYear[2],TouristsPerYear[3]] # values on y axis
GraphBars=plt.bar(x_cord,height_cord,tick_label=label,width=0.5,color=["red","green","orange","blue"])
plt.xlabel("Years")
plt.ylabel("Tourists")
plt.yticks(diaxorismosy,['0','2.5m','5m','7.5m','10m','12.5m','15m','17.5m','20m','22.5m','25m'])
plt.title("Tourists Per Year")
for i in range(len(x_cord)):
    plt.text(x_cord[i]-0.2,TouristsPerYear[i],str(TouristsPerYear[i]),)


#Second Graph
xwres=["France","Germany","UK","Italy","Russia"]
index=np.arange(4)
timesgiay=[0,300000,600000,900000,1200000,1500000,1800000,2100000,2400000,2700000,3500000]
width=0.18
France = [value2011[0],value2012[0],value2013[0],value2014[0]]
Germany = [value2011[1],value2012[1],value2013[1],value2014[1]]
Uk = [value2011[2],value2012[2],value2013[2],value2014[2]]
Italy = [value2011[3],value2012[3],value2013[3],value2014[3]]
Russia =[value2011[4],value2012[4],value2013[4],value2014[4]]
fig, ax=plt.subplots()
bar_France = ax.bar(index ,France,width,label="France")
bar_Germany = ax.bar(index - 1*width,Germany,width,label="Germany")
bar_Uk = ax.bar(index -2*width,Uk,width,label="Uk")
bar_Italy = ax.bar(index + width,Italy,width,label="Italy")
bar_Russia =ax.bar(index + 2*width,Russia,width,label="Russia")
ax.set_xticks(index)
ax.set_xticklabels([2011,2012,2013,2014])
ax.set_yticks(timesgiay)
ax.set_yticklabels(["0","300k","600k","900k","1.2m","1.5m","1.8m","2.1m","2.4m","2.7m","3.5m"])
plt.ylabel("Tourists visited Greece")
autolabel(bar_France)
autolabel(bar_Germany)
autolabel(bar_Uk)
autolabel(bar_Italy)
autolabel(bar_Russia)
ax.legend()
plt.title("Top Countries Per Years")


#Third Graph
index=np.arange(4)
width=0.20
valuesfory=[0,2000000,4000000,6000000,8000000,10000000,12000000,14000000,16000000]
fig,ax=plt.subplots()
bar_2011=ax.bar(index,TransportArray[0],width,label="2011")
bar_2012=ax.bar(index+width,TransportArray[1],width,label="2012")
bar_2013=ax.bar(index+2*width,TransportArray[2],width,label="2013")
bar_2014=ax.bar(index+3*width,TransportArray[3],width,label="2014")
ax.set_xticks(index)
ax.set_xticklabels(["aerodromikos","sidirodromikos","thallasios","odikos"])
ax.set_yticks(valuesfory)
ax.set_yticklabels(["0","2m","4m","6m","8m","10m","12m","14m","16m"])
plt.ylabel("Tourists Transported")
autolabel(bar_2011)
autolabel(bar_2012)
autolabel(bar_2013)
autolabel(bar_2014)
ax.legend()
plt.title("Transport Values Per Years")

#Fourth Graph
index=np.arange(4)
width=0.20
valuesfory=[0,2000000,4000000,6000000,8000000,10000000,12000000,14000000,16000000]
fig,ax=plt.subplots()
bar_2011=ax.bar(index,trimina[0],width,label="2011")
autolabel(bar_2011)
bar_2012=ax.bar(index+width,trimina[1],width,label="2012")
autolabel(bar_2012)
bar_2013=ax.bar(index+2*width,trimina[2],width,label="2013")
autolabel(bar_2013)
bar_2014=ax.bar(index+3*width,trimina[3],width,label="2014")
autolabel(bar_2014)
ax.set_xticks(index)
ax.set_xticklabels(["1o trimino","2o trimino","3o trimino","4o trimino"])
ax.set_yticks(valuesfory)
ax.set_yticklabels(["0","2m","4m","6m","8m","10m","12m","14m","16m"])
plt.ylabel("Tourists Visited")
ax.legend()
plt.title("Tourists visited per 3-month period")
plt.show()