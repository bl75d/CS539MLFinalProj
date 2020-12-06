import numpy as np
class NAV:
    def __init__(self,initial_value):
        self.symbol=''
        self.day=0
        self.initial_value=initial_value
        self.cash=initial_value
        self.nav=initial_value
        self.stockquant=0
        self.stockprice=0
        self.stockvalue=0

    def invest(self,symbol,signal,price):
        self.day+=1
        self.symbol=symbol
        # sell
        if signal==0:
            # have stock
            if self.stockquant>0:
                self.stockprice=price
                self.cash +=self.stockquant*self.stockprice
                self.stockquant=0
                self.stockvalue=0
                self.nav=self.cash
        # Buy
        elif signal==2:
            # have 0 stock
            if self.stockquant==0:
                self.nav = self.cash
                self.stockprice = price
                self.stockquant = int(self.cash/self.stockprice)
                self.stockvalue = self.stockquant*self.stockprice
                self.cash -= self.stockvalue


# if __name__ == '__main__':
#     portofolio=NAV(100)
#     symbol='TSLA'
#     stockprice=np.asarray([1,2,3,4,5,6,7,8])
#     signal=np.asarray([2,2,1,2,1,2,1,0])
#     for i in range(signal.shape[0]):
#         portofolio.invest(symbol,signal[i],stockprice[i])
#         print(portofolio.nav)