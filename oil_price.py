import fix_yahoo_finance as yf
import pdb
# data = yf.download("CLF18.NYM", start="2017-12-17", end="2017-12-18")
data = yf.download("CLF18.NYM")

crude_oil = yf.download("CLJ14.NYM")
heating_oil = yf.download("HOH14.NYM")

heating_oil = yf.download("HOH14.NYM")
CVX = yf.download("CVX")

CVX['Close'][-1]
pdb.set_trace()

if data['Close'][-1]:
    print('\n')
    print(data['Close'][-1])
else:
    print('no price')
