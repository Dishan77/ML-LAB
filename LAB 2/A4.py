import pandas as pd
import numpy as np

IRCTCdf = pd.read_csv('IRCTCdata.csv', usecols=['Date','Month','Day','Price','Open','High','Low','Volume','Chg%'])
mean = IRCTCdf[['Price']].mean(axis=1)
print('IRCTC data\n',IRCTCdf,'\n')
print('Mean of Price: ',mean,'\n')