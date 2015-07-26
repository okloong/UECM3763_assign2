from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import pandas as pd
import pylab as p

#get data from yahoo
start = dt(2012, 5, 1)
end = dt(2015, 5, 1)
genting = DR("3182.KL", 'yahoo',start,end)
klse = DR("^KLSE",'yahoo',start,end)

#find and plot the 5-day moving average
G5DMA = pd.rolling_mean(genting['Close'],5)
p.ylabel('5-day MA')
p.title('GENTING 5-day MA')
G5DMA.plot()
p.show()

#calculate the correlation between genting and FTSEKLCI
data = ["3182.KL","^KLSE"]
dldata = DR(data,'yahoo',start,end)['Close']

correlation=dldata.corr()
print('Correlation= \n',correlation)