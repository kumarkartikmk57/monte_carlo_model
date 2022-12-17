import numpy as np

class option:
    def __init__(self,S0,E,T,rf,sigma,iteration):
        self.S0 = S0
        self.E = E
        self.T = T
        self.rf = rf
        self.sigma = sigma
        self.iteration = iteration

    def call_option(self):
        #payoff function is max(0,S-E)

        #we have 2 columns,first with 0s and the second with payoff
        option_data = np.zeros([self.iteration,2])
        rand = np.random.normal(0,1,[1,self.iteration])
        stock_price = self.S0*np.exp(self.T*(self.rf-0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        #print(option_data)
        #print(rand)
        #print("\n The stock price is \n")
        #print(stock_price)
        #calculating S-E
        option_data[:,1] = stock_price - self.E
        #print("\n\n\n\n\n The S-E value is \n")
        #print(option_data)
        avg = np.sum(np.amax(option_data,axis=1))/float(self.iteration)
        #print("\n\n\n\n the average value is \n")
        #print(avg)
        #calulation of discount factor
        dis = np.exp(-1.0*self.rf*self.T)*avg
        #print("\n\n\n\n the discount value is \n")
        print("The call option is ",dis)
        return dis


    def put_option(self):
        #payoff function is max(0,S-R)

        #we have 2 columns,first with 0s and the second with payoff
        #print("\n\n\n\n\n\n\n THE PUT OPTIONS")
        option_data = np.zeros([self.iteration,2])
        rand = np.random.normal(0,1,[1,self.iteration])
        stock_price = self.S0*np.exp(self.T*(self.rf-0.5*self.sigma**2)+self.sigma*np.sqrt(self.T)*rand)
        #print(option_data)
        #print(rand)
        #print("\n The stock price is \n")
        #print(stock_price)
        #calculating S-E
        option_data[:,1] = self.E - stock_price
        #print("\n\n\n\n\n The S-E value is \n")
        #print(option_data)
        avg = np.sum(np.amax(option_data,axis=1))/float(self.iteration)
        #print("\n\n\n\n the average value is \n")
        #print(avg)
        #calulation of discount factor
        dis = np.exp(-1.0*self.rf*self.T)*avg
        #print("\n\n\n\n the discount value is \n")
        print("The put option is ",dis)
        return dis


if __name__ == '__main__':
    opt = option(100,100,1,0.05,0.2,1000)
    opt.call_option()
    opt.put_option()