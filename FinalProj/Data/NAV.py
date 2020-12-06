import numpy as np
import matplotlib.pyplot as plt
class Nav:
    def __init__(self,initial_value):
        self.symbol=''
        self.day=0
        self.initial_value=initial_value
        self.cash=initial_value
        self.nav=initial_value
        self.stockquant=0
        self.stockprice=0
        self.stockvalue=0
        # record the trading history
        self.tradinghist=[]
        self.pricehist=[]
        self.navhist=[]

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
                self.tradinghist.append(signal)
                self.pricehist.append(price)
                self.navhist.append(self.nav)

        # Buy
        elif signal==0:
            # have 0 stock
            if self.stockquant==0:
                self.nav = self.cash
                self.stockprice = price
                self.stockquant = int(self.cash/self.stockprice)
                self.stockvalue = self.stockquant*self.stockprice
                self.cash -= self.stockvalue
                self.tradinghist.append(signal)
                self.pricehist.append(price)
                self.navhist.append(self.nav)
        else:
            self.stockprice = price
            self.stockvalue = self.stockquant * self.stockprice
            self.nav=self.cash+self.stockvalue
            self.tradinghist.append(signal)
            self.pricehist.append(price)
            self.navhist.append(self.nav)



# if __name__ == '__main__':
#     portofolio=Nav(1000)
#     symbol='TSLA'
#     stockprice=np.asarray([1,2,3,4,5,6,7,8])
#     signal=np.asarray([1,2,1,0,2,0,2,0])
#     for i in range(signal.shape[0]):
#         portofolio.invest(symbol,signal[i],stockprice[i])
#         print(portofolio.nav)

# use stock['close'] as the stock price; y_predict is the prediction for X_test, it is the signal for trading
def Generate_nav(fund,StockPriceDic,symbol,y_predict):
    price = StockPriceDic[symbol]
    teststart=price.shape[0]-y_predict.shape[0]
    stockprice = price[teststart:price.shape[0]]
    if stockprice.shape==y_predict.shape:
        portofolio = Nav(fund)
        for i in range(stockprice.shape[0]):
            portofolio.invest(symbol,y_predict[i],stockprice[i])

        print(portofolio.navhist)
        plt.plot(portofolio.nav)
        plt.title('Net Asset Value')
        plt.ylabel('Dollar')
        plt.xlabel('Day')
        plt.legend(['Value'], loc='upper left')
        plt.show()
        return portofolio.navhist

    else:
        print("Prediction length error! Check generate_nav()")
