#!/usr/bin/env python
# coding: utf-8

## CALL OPTION PLOT K = 80 ##
import numpy as np
import matplotlib.pyplot as plt

# Define the strike price and premium
K = 80
premium = 5

# Generate the stock price range from 0 to 150 at intervals of 1
S = np.arange(0, 151, 1)

# Calculate the profit/loss for the option holder
payoff = np.maximum(S - K, 0) - premium

# Plot the graph of profit/loss against stock price
plt.plot(S, payoff)
plt.xlabel('Stock Price')
plt.ylabel('Profit/Loss')
plt.title('Long Call Option Payoff')
plt.grid()

# Set the x-axis range to include the strike price
plt.xlim(0, 150)


#add a line at x=0
plt.axhline(y=0, linestyle ="--", color="black")
plt.scatter([80+premium], [0], color='red', marker='o')

# Set the y-axis range to include the premium
plt.ylim(-10, 100)


plt.show()


### LONG CALL OPTION WITH LOWER STRIKE K = 60 ###


import numpy as np
import matplotlib.pyplot as plt

# Define the strike price and premium
K = 60
premium = 10

# Generate the stock price range from 0 to 150 at intervals of 1
S = np.arange(0, 151, 1)

# Calculate the profit/loss for the option holder
payoff = np.maximum(S - K, 0) - premium

# Plot the graph of profit/loss against stock price
plt.plot(S, payoff)
plt.xlabel('Stock Price')
plt.ylabel('Profit/Loss')
plt.title('Call Option Payoff')
plt.grid()

# Set the x-axis range to include the strike price
plt.xlim(0, 150)


#add a line at x=0
plt.axhline(y=0, linestyle ="--", color="black")
plt.scatter([60+premium], [0], color='red', marker='o')


# Set the y-axis range to include the premium
plt.ylim(-20, 100)


plt.show()


##LONG PUT OPTION WITH K = 80###


import numpy as np
import matplotlib.pyplot as plt

# Define the strike price and premium
K = 80
premium = 5

# Generate the stock price range from 0 to 150 at intervals of 1
S = np.arange(0, 151, 1)

# Calculate the profit/loss for the option holder
payoff = np.maximum(K - S, 0) - premium

# Plot the graph of profit/loss against stock price
plt.plot(S, payoff)
plt.xlabel('Stock Price')
plt.ylabel('Profit/Loss')
plt.title('Put Option Payoff')
plt.grid()

# Set the x-axis range to include the strike price
plt.xlim(0, 150)


#add a line at x=0
plt.axhline(y=0, linestyle ="--", color="black")
plt.scatter([K-premium], [0], color='red', marker='o')


# Set the y-axis range to include the premium
plt.ylim(-20, 100)


plt.show()


###LONG PUT OPTION WITH K=100###


import numpy as np
import matplotlib.pyplot as plt

# Define the strike price and premium
K = 100
premium = 10

# Generate the stock price range from 0 to 150 at intervals of 1
S = np.arange(0, 151, 1)

# Calculate the profit/loss for the option holder
payoff = np.maximum(K - S, 0) - premium

# Plot the graph of profit/loss against stock price
plt.plot(S, payoff)
plt.xlabel('Stock Price')
plt.ylabel('Profit/Loss')
plt.title('Put Option Payoff')
plt.grid()

# Set the x-axis range to include the strike price
plt.xlim(0, 150)


#add a line at x=0
plt.axhline(y=0, linestyle ="--", color="black")
plt.scatter([K-premium], [0], color='red', marker='o')


# Set the y-axis range to include the premium
plt.ylim(-20, 100)


plt.show()



### RELATIONSHIP BETWEEN LONG CALL OPTION PRICE AND STRIKE ####
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes(s, k, t, r, sigma):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    call = s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    return call

s = 60 # stock price
t = 1 # time to maturity (in years)
r = 0.03 # risk-free interest rate
sigma = 0.2 # volatility

strike_prices = np.arange(1, 121, 5)
option_prices = [black_scholes(s, k, t, r, sigma) for k in strike_prices]

plt.plot(strike_prices, option_prices)
plt.xlabel("Strike Price K")
plt.ylabel("Call option Price")
plt.title("Call Option Price vs. Strike Price")


plt.show()



### RELATIONSHIP BETWEEN LONG CALL OPTION PRICE VS VOLA ####
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes(s, k, t, r, sigma):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    call = s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    return call

s = 60 # stock price
k = 60
t = 1 # time to maturity (in years)
r = 0.03 # risk-free interest rate

# vola_percentage = np.arange(0.1, 0.6, 0.01)
option_prices = [black_scholes(s, k, t, r, sigma) for sigma in vola_percentage]

plt.plot(vola_percentage, option_prices)
plt.xlabel("Volatility")
plt.ylabel("Call option price")
plt.title("Call option Price vs. Volatility")
plt.show()



### RELATIONSHIP BETWEEN LONG Call OPTION PRICE VS TIME ####
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes(s, k, t, r, sigma):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    call = s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    return call

s = 60 # stock price
k = 60 # time to maturity (in years)
r = 0.03 # risk-free interest rate
sigma = 0.2

time = np.arange(0.1, 2, 0.01)
option_prices = [black_scholes(s, k, t, r, sigma) for t in time]

plt.plot(time, option_prices)
plt.xlabel("Time to maturity")
plt.ylabel("Call option price")
plt.title("Call option Price vs. Time")
plt.show()



# In[114]:


## RELANTIONSHIP BETWEEN LONG CALL OPTION VS  INTEREST RATES##
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes(s, k, t, r, sigma):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    call = s * norm.cdf(d1) - k * np.exp(-r * t) * norm.cdf(d2)
    return call

s = 50 # stock price
k = 50 # strike price
t = 1 # time to maturity (in years)
sigma = 0.2 # volatility

interest_rates = np.arange(0.01, 0.06, 0.01)
option_prices = [black_scholes(s, k, t, r, sigma) for r in interest_rates]

plt.plot(interest_rates, option_prices)
plt.xlabel("Interest Rates")
plt.ylabel("Call Option Price")
plt.title("Call Option Price vs. Interest Rates")
plt.show()


###RELANTIONSHIP BETWEEN LONG PUT OPTION VS STRIKE PRICE###
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes(s, k, t, r, sigma):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    put = k * np.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)
    return put

s = 60 # stock price
t = 1 # time to maturity (in years)
r = 0.03 # risk-free interest rate
sigma = 0.2 # volatility

strike_prices = np.arange(1, 121, 5)
option_prices = [black_scholes(s, k, t, r, sigma) for k in strike_prices]

plt.plot(strike_prices, option_prices)
plt.xlabel("Strike Price")
plt.ylabel("Put option Price")
plt.title("Long Put Option Price vs. Strike Price")
plt.show()



### RELANTIONSHIP BETWEEN LONG PUT OPTION VS VOLATILITY###
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes(s, k, t, r, sigma):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    put = k * np.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)
    return put

s = 60 # stock price
t = 1 # time to maturity (in years)
r = 0.03 # risk-free interest rate
k = 60 # volatility

vola = np.arange(0.1, 0.6, 0.01)
option_prices = [black_scholes(s, k, t, r, sigma) for sigma in vola]

plt.plot(vola, option_prices)
plt.xlabel("Volatility")
plt.ylabel("Put option Price")
plt.title("Long Put Option Price vs. Volatility")
plt.show()


# In[116]:


##RELANTIONSHIP BETWEEN LONG PUT OPTION VS TIME##
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

def black_scholes(s, k, t, r, sigma):
    d1 = (np.log(s/k) + (r + sigma**2/2)*t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    put = k * np.exp(-r * t) * norm.cdf(-d2) - s * norm.cdf(-d1)
    return put

s = 60 # stock price
sigma = 0.2 # volatility
r = 0.03 # risk-free interest rate
k = 60 # Strike price

time = np.arange(0.1, 2, 0.01)
option_prices = [black_scholes(s, k, t, r, sigma) for t in time]

plt.plot(time, option_prices)
plt.xlabel("Time to expiration")
plt.ylabel("Put option Price")
plt.title("Long Put Option Price vs. Time")
plt.show()

