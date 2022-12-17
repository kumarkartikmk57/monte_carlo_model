import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

num_of_simulation = 100000

def monte(S0,mu,sigma,N=1000):
    result = []
    for i in range(num_of_simulation):
        price = [S0]
        for j in range(N):
            stock_price = price[-1] * np.exp((mu - 0.5 * sigma**2)+sigma*np.random.normal())
            price.append(stock_price)

        result.append(price)
    simulation_data = pd.DataFrame(result)
    simulation_data = simulation_data.T
    simulation_data['mean'] = simulation_data.mean(axis=1)
    fv = simulation_data['mean'].tail(1)
    print(simulation_data)
    print("Prediction of future stock price is ",fv)
    #simulation_data.plot()
    #plt.show()

monte(50,0.002,0.01)
