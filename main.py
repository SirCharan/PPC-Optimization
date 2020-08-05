# found totla of 50k keywords in bitcoin
# Found 8573 keywords in "Buy Bitcoin"
# Seperated 899 keywords in "buy bitcoin card"

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy
os.chdir(path)

#importing the file. Please add the file path correctly to pd.read_excel() function. Remeber to put C:/ instead of C:\

# print(os.listdir())
data=pd.read_excel('fulll bitcoin.xlsx')

cols={'Keyword','Volume','CPC (USD)','Competitive Density','Trend','Keyword Difficulty'}
dt=data[cols]
print(dt.head())
print('total number'+str(len(dt['Keyword'])))

dt.describe()

b=[]
keyword=str(input('Which keyword do you want to group by?'))
for i in range(len(dt['Keyword'])):
    if(dt['Keyword'][i].split('[')[0].count(keyword)):
        b.append(i)
# dtnew=dt.loc(b)
dt.to_excel('{}.xlsx'.format(keyword))

data=pd.read_excel('{}.xlsx'.format(keyword))
data.head()
cols={'Keyword','Volume','CPC (USD)','Competitive Density','Number of Results','Trend'}
dt=data[cols]
dt.head()
dta=dt[dt['Volume']==0]
print("Total entries in /buy Bitcoin card/\t"+str(len(dt['Keyword'])))
print("Entries with Less than 10 Volume/buy Bitcoin card/ \t"+str(len(dt[dt['Volume']==0]['Volume'])))
print("Entries with Less than 20 Volume/buy Bitcoin card/ \t"+str(len(dt[dt['Volume']<20]['Volume'])))
# print("Entries with Less than 20 Volume/buy Bitcoin card/ \t"+str(len(dt[dt['Volume']<30]['Volume'])))
print("Entries with Less than 30 Volume/buy Bitcoin card/ \t"+str(len(dt[dt['Volume']<40]['Volume'])))
print("Entries with more than 90 volume /bitcoin card/ volume\t"+str(len(dt[dt['Volume']>=90]['Volume'])))
dt[dt['Volume']>=90]


databest=pd.read_excel('full bitcoin.xlsx')
# databest.head()

datae=pd.read_excel('full bitcoin.xlsx')
# datae.head()

exchange=datae[datae['Volume']>100]
best=databest[databest['Volume']>100]
trade=datat[datat['Volume']>100]
number=data0[data0['Volume']>100]
can=datacan[datacan['Volume']>100]
can.head()
uk=datau[datau['Volume']>100]
uk.head()
cash=datac[datac['Volume']>100]
cash.head()
price=datap[datap['Volume']>100]
wallet=dataw[dataw['Volume']>100]
mine=datam[datam['Volume']>100]
buy=datab[datab['Volume']>100]
be.to_excel('exchange.xlsx')

os.chdir('C:/Users\HP\Desktop\bitcoin')

cols={'Keyword','Volume','Trend','Keyword Difficulty','Number of Results','Competitive Density','CPC (USD)'}

for file in os.listdir(): 
    print(file)
    a=pd.read_excel('{}'.format(file))
    a=a[cols]
    for j in range(len(a['Volume'])):
        c=[]
        for i in range(12):
            c.append(float(b.split(',')[i]))
        if (np.min(c)==c[11]):
            a.drop(a.index[j])
    d = pd.concat([d,a], axis=0, sort=False)
    print(a.head())

b=a['Trend'][0]

import numpy as numpy
c=[]
for i in range(12):
    c.append(float(b.split(',')[i]))
if (np.min(c)==c[11]):
    a.drop(a.index[j])

import numpy as np

frames = [ process_your_file(f) for f in os.listdir() ]
result = pd.concat(frames)

d=a
i=0
for j in range(len(d['Volume'])):
    i=i+1
    b=d['Trend'][i]



d=pd.read_excel('can.xlsx')
len(d['Volume'])
d.to_excel('draft.xlsx')
f=pd.read_excel('fulll bitcoin.xlsx')
os.chdir('C:/Users\HP\Desktop\bitcoin')

f=f[f['Volume']>300]

len(f['Volume'])

f=f[f['Number of Results']>0]

f.to_excel('draft1.xlsx')

silver=pd.read_excel('silver.xlsx')

silver=f[(f['Volume']<10000) & (f['Volume']>1000)]

len(f['Volume'])

gold=f

gold.to_excel('gold.xlsx')

bronze=f[f['Volume']<1000]

len(silver['Volume'])

bronze.to_excel('bronze.xlsx')
silver.to_excel('silver.xlsx')

silver.head()

vol=silver['Volume']
nvol=[]
for i in range(len(silver['Volume'])):
    a=(vol[i]-1000)/10000
    nvol.append(a)
print(nvol)
silver.insert(4,"Normalized Volume",nvol,True)

score=[]
for i in range(len(silver['Volume'])):
    score.append((nvol[i])*(5-cpc[i]))

np.max(score)

ascore=[]
for i in range(len(score)):
    ascore.append(score[i]*10/2.9281)

silver.insert(4,"Score",ascore,True)

dd=[]
kd=silver['Competitive Density']
cd=silver['Keyword Difficulty']
for i in range(len(score)):
    dd.append(kd[i]*cd[i])

dd

usd=silver['CPC (USD)']*.82

silver.drop(columns=['Number of Results'])

silver.sort_values(by=['Volume'],ascending=False)

silver.to_excel('Silverlist.xlsx')

f=pd.read_excel('Gold Final.xlsx')

vol=f['Volume']
nvol=[]
for i in range(len(f['Volume'])):
    a=(vol[i]-10000)/10000
    nvol.append(a)
print(nvol)
f.insert(4,"Score",nvol,True)

score=[]
for i in range(len(f['Volume'])):
    score.append((nvol[i])*(5-cpc[i]))
print(score)

cpc=f['CPC (GBP)']

f.head()

f.insert(3,"Score",score,True)

f.to_excel('Gold Final.xlsx')
