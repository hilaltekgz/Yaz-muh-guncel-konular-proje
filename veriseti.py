import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import datetime
df = pd.read_csv(r'C:\Users\hlltk\OneDrive\Masaüstü\uzaktanegitim\güncel konulae\proje_dataset\kentsel\Kocaeli.csv',encoding='UTF-8',index_col='date',parse_dates=True)
del df['KabinSicakligi ( °C )']
# print ("Rows     : " ,df.shape[0])
# print ("Columns  : " ,df.shape[1])
# print ("\nFeatures : \n" ,df.columns.tolist())
# print ("\nMissing values :  ", df['RuzgarHizi ( m/s )'].isnull().sum())
# print ("\nUnique values :  \n",df.nunique())

So2 = df['SO2 ( µg/m³ )'].interpolate(method='cubic')
Pm10 = df['PM10 ( µg/m³ )'].interpolate(method='cubic')
Pm10debi = df['PM10Debi ( m³/saat )'].interpolate(method='linear')
No2 = df['NO2 ( µg/m³ )'].interpolate(method='linear')
NoX = df['NOX ( µg/m³ )'].interpolate(method='linear')
No = df['NO ( µg/m³ )'].interpolate(method='linear')
O3 = df['O3 ( µg/m³ )'].interpolate(method='linear')
havaSicakligi = df['HavaSicakligi ( °C )'].interpolate(method='linear')
rüzgarhizi = df['RuzgarHizi ( m/s )'].interpolate(method='linear')
bagilNem = df['BagilNem ( % )'].interpolate(method='cubic')
Pm25debi = df['PM25Debi ( m³/saat )'].interpolate(method='linear')
pm25 = df['PM25 ( µg/m³ )'].interpolate(method='linear')

data = pd.DataFrame({'SO2 ( µg/m³ )' : So2,'PM10 ( µg/m³ )':Pm10,'PM10Debi ( m³/saat )':Pm10debi,'NO2 ( µg/m³ )':No2,'NOX ( µg/m³ )':NoX,'NO ( µg/m³ )':No,'O3 ( µg/m³ )':O3,'HavaSicakligi ( °C )':havaSicakligi,'RuzgarHizi ( m/s )':rüzgarhizi,'BagilNem ( % )':bagilNem,'PM25Debi ( m³/saat )':Pm25debi,'PM25 ( µg/m³ )':pm25})
print(data)
print ("Rows     : " ,data.shape[0])
print ("Columns  : " ,data.shape[1])
print ("\nFeatures : \n" ,data.columns.tolist())
print ("\nMissing values :  ", data.isnull().sum())
print ("\nUnique values :  \n",data.nunique())
#data.to_csv('yeniveriseti.csv')

yenidata = pd.read_csv(r'C:\Users\hlltk\PycharmProjects\guncel\yeniveriseti.csv')
# # print(yenidata)
# # print ("Rows     : " ,yenidata.shape[0])
# # print ("Columns  : " ,yenidata.shape[1])
# # print ("\nFeatures : \n" ,yenidata.columns.tolist())
# # print ("\nMissing values :  ", yenidata.isnull().sum())
# # print ("\nUnique values :  \n",yenidata.nunique())
# import datetime
dates = [datetime.datetime.strptime(ts, "%Y-%m-%d") for ts in yenidata['date']]
dates.sort()
sorteddates = [datetime.datetime.strftime(ts, "%Y-%m-%d") for ts in dates]
yenidata['date'] = pd.DataFrame({'date':sorteddates})
yenidata['Year'], yenidata['Month'],  yenidata['Day'] = yenidata['date'].str.split('-').str
yenidata.head(10)
# dategroup=yenidata.groupby('Month').mean()
# print(yenidata.isnull().sum())
# fig, ax = plt.subplots(figsize=(15,7))
# ax.xaxis.set(ticks=range(0,13)) # Manually set x-ticks
# dategroup['PM10 ( µg/m³ )'].plot(x=yenidata.Month)
# dategroup['PM10Debi ( m³/saat )'].plot(x=yenidata.Month)
# dategroup['SO2 ( µg/m³ )'].plot(x=yenidata.Month)
# dategroup['NO2 ( µg/m³ )'].plot(x=yenidata.Month)
# dategroup['NOX ( µg/m³ )'].plot(x=yenidata.Month)
# dategroup['NO ( µg/m³ )'].plot(x=yenidata.Month)
# dategroup['O3 ( µg/m³ )'].plot(x=yenidata.Month)
# dategroup['HavaSicakligi ( °C )'].plot(x=yenidata.Month)
# dategroup['RuzgarHizi ( m/s )'].plot(x=yenidata.Month)
# dategroup['PM25 ( µg/m³ )'].plot(x=yenidata.Month)
# dategroup['PM25Debi ( m³/saat )'].plot(x=yenidata.Month)
#
# plt.legend(['PM10 ( µg/m³ )','PM10Debi ( m³/saat )','SO2 ( µg/m³ )','NO2 ( µg/m³ )','NOX ( µg/m³ )','NO ( µg/m³ )','O3 ( µg/m³ )','HavaSicakligi ( °C )','RuzgarHizi ( m/s )','PM25 ( µg/m³ )','PM25Debi ( m³/saat )'])
# plt.title('Parametrelerin Aylara göre dağılımları')
# plt.show()
#
#
# ############################################################################################################3
#
# dategroup=yenidata.groupby('Year').mean()
# print(yenidata.isnull().sum())
# fig, ax = plt.subplots(figsize=(15,7))
# ax.xaxis.set(ticks=range(0,13)) # Manually set x-ticks
# dategroup['PM10 ( µg/m³ )'].plot(x=yenidata.Year)
# dategroup['PM10Debi ( m³/saat )'].plot(x=yenidata.Year)
# dategroup['SO2 ( µg/m³ )'].plot(x=yenidata.Year)
# dategroup['NO2 ( µg/m³ )'].plot(x=yenidata.Year)
# dategroup['NOX ( µg/m³ )'].plot(x=yenidata.Year)
# dategroup['NO ( µg/m³ )'].plot(x=yenidata.Year)
# dategroup['O3 ( µg/m³ )'].plot(x=yenidata.Year)
# dategroup['HavaSicakligi ( °C )'].plot(x=yenidata.Year)
# dategroup['RuzgarHizi ( m/s )'].plot(x=yenidata.Year)
# dategroup['PM25 ( µg/m³ )'].plot(x=yenidata.Year)
# dategroup['PM25Debi ( m³/saat )'].plot(x=yenidata.Year)
#
# plt.legend(['PM10 ( µg/m³ )','PM10Debi ( m³/saat )','SO2 ( µg/m³ )','NO2 ( µg/m³ )','NOX ( µg/m³ )','NO ( µg/m³ )','O3 ( µg/m³ )','HavaSicakligi ( °C )','RuzgarHizi ( m/s )','PM25 ( µg/m³ )','PM25Debi ( m³/saat )'])
# plt.title('Parametrelerin Yıllara göre dağılımları')
# plt.show()
# ################################################################################################################3
# dategroup=yenidata.groupby('Day').mean()
# print(yenidata.isnull().sum())
# fig, ax = plt.subplots(figsize=(15,7))
# ax.xaxis.set(ticks=range(0,13)) # Manually set x-ticks
# dategroup['PM10 ( µg/m³ )'].plot(x=yenidata.Day)
# dategroup['PM10Debi ( m³/saat )'].plot(x=yenidata.Day)
# dategroup['SO2 ( µg/m³ )'].plot(x=yenidata.Day)
# dategroup['NO2 ( µg/m³ )'].plot(x=yenidata.Day)y
# dategroup['NOX ( µg/m³ )'].plot(x=yenidata.Day)
# dategroup['NO ( µg/m³ )'].plot(x=yenidata.Day)
# dategroup['O3 ( µg/m³ )'].plot(x=yenidata.Day)
# dategroup['HavaSicakligi ( °C )'].plot(x=yenidata.Day)
# dategroup['RuzgarHizi ( m/s )'].plot(x=yenidata.Day)
# dategroup['PM25 ( µg/m³ )'].plot(x=yenidata.Day)
# dategroup['PM25Debi ( m³/saat )'].plot(x=yenidata.Day)
#
# plt.legend(['PM10 ( µg/m³ )','PM10Debi ( m³/saat )','SO2 ( µg/m³ )','NO2 ( µg/m³ )','NOX ( µg/m³ )','NO ( µg/m³ )','O3 ( µg/m³ )','HavaSicakligi ( °C )','RuzgarHizi ( m/s )','PM25 ( µg/m³ )','PM25Debi ( m³/saat )'])
# plt.title('Parametrelerin Günlere göre dağılımları')
# plt.show()

################################################

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
colormap = plt.cm.RdBu
plt.figure(figsize=(10,8))
plt.title('aa', y=1.05, size=16)

mask = np.zeros_like(yenidata.corr())
mask[np.triu_indices_from(mask)] = True

svm = sns.heatmap(yenidata.corr(), mask=mask, linewidths=0.1,vmax=1.0,
            square=True, cmap=colormap, linecolor='white', annot=True)
plt.show()

from statsmodels.tsa.stattools import acf, pacf
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf



# Calculate ACF and PACF upto 50 lags
# acf_50 = acf(df.value, nlags=50)
# pacf_50 = pacf(df.value, nlags=50)

# Draw Plot
# fig, axes = plt.subplots(1,2,figsize=(16,3), dpi= 100)
# plot_acf(yenidata.value.tolist(), lags=50, ax=axes[0])
# plot_pacf(yenidata.value.tolist(), lags=50, ax=axes[1])
#
# plt.show()

############################################
import seaborn as sns
from tkinter import *

#'Bir veri kümesinin ortalaması (ortalama), veri kümesindeki tüm sayılar eklenerek ve ardından kümedeki değer sayısına bölünerek bulunur. Bir veri kümesi en azdan en büyüğe sıralandığında ortanca orta değerdir. Mod, bir veri kümesinde en sık meydana gelen sayıdır. Oluşturan Sal Khan .'
dategroup=yenidata.groupby('Year').mean()
params = ['SO2 ( µg/m³ )','PM10 ( µg/m³ )','PM10Debi ( m³/saat )','NO2 ( µg/m³ )','NOX ( µg/m³ )','NO ( µg/m³ )','O3 ( µg/m³ )','HavaSicakligi ( °C )','RuzgarHizi ( m/s )','BagilNem ( % )',
          'PM25Debi ( m³/saat )','PM25 ( µg/m³ )']
print('mediannn',np.median(yenidata['PM25Debi ( m³/saat )']))
for i in params:

    print('{} ortalama değeri : {}'.format(i,dategroup.mean(i)))
size =[]
from collections import Counter
from scipy import stats
print('\n\n')
for i in params:
    a = stats.mode(yenidata[i])
    size.append(a)
    print('{} Mode değeri : {}'.format(i,stats.mode(yenidata[i])))
print('\n\n')
# for i in params:
#     print('{} Median değeri : {}'.format(i,np.median(yenidata[i])))


labels='SO2 ( µg/m³ )','PM10 ( µg/m³ )','PM10Debi ( m³/saat )','NO2 ( µg/m³ )','NOX ( µg/m³ )','NO ( µg/m³ )','O3 ( µg/m³ )','HavaSicakligi ( °C )','RuzgarHizi ( m/s )','PM25Debi ( m³/saat )','PM25 ( µg/m³ )'
sizes=[10.645233,60.232472,0.831973,10.109872,15.375221,4.60064,50.434765,9.688164,1.59747,0.713696,25.710493]
colors=['gold','green','red','blue','pink','blue','purple','orange','black','white','brown']
explode=(0,0,0,0,0,0,0,0,0,0,0)

plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=300)
plt.legend(labels,loc='best')
plt.axis('equal')
plt.show()