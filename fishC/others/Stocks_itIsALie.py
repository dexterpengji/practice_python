# -- coding: utf-8 --
# Original:
# https://www.quantinsti.com/blog/gold-price-prediction-using-machine-learning-python

# Reference:
# https://zhuanlan.zhihu.com/p/35501733
# https://zhuanlan.zhihu.com/p/23471979

# LinearRegression is a machine learning library for linear regression   
from sklearn.linear_model import LinearRegression   
# pandas and numpy are used for data manipulation   
import pandas as pd   
import numpy as np   
# matplotlib and seaborn are used for plotting graphs   
import matplotlib.pyplot as plt   
import seaborn   
# fix_yahoo_finance is used to fetch data 
import fix_yahoo_finance as yf

# Read data 
# gafataDict={'谷歌':'GOOG','亚马逊':'AMZN','Facebook':'FB','苹果':'AAPL','阿里巴巴':'BABA','腾讯':'0700.hk'}
Df = yf.download('GLD','2008-01-01','2018-12-01')
# Only keep close columns 
Df=Df[['Close']] 
# Drop rows with missing values 
Df= Df.dropna() 
# Plot the closing price of GLD 
Df.Close.plot(figsize=(10,5)) 
plt.ylabel("Gold ETF Prices")
plt.show()

# Define explanatory variables
Df['S_3'] = Df['Close'].shift(1).rolling(window=3).mean() 
Df['S_9']= Df['Close'].shift(1).rolling(window=9).mean() 
Df= Df.dropna() 
X = Df[['S_3','S_9']] 
X.head()
print '='*100
print X

# Define dependent variable
y = Df['Close']
y.head()
print '='*100
print y

# Split the data into train and test dataset
t=.8
t = int(t*len(Df)) 
# Train dataset 
X_train = X[:t] 
y_train = y[:t]  
# Test dataset 
X_test = X[t:] 
y_test = y[t:]

# Create a linear regression model
# Y = m1 * X1 + m2 * X2 + C
# Gold ETF price = m1 * 3 days moving average + m2 * 15 days moving average + c
linear = LinearRegression().fit(X_train,y_train)
print '='*100
print "Gold ETF Price =", round(linear.coef_[0],2), "* 3 Days Moving Average", round(linear.coef_[1],2), "* 9 Days Moving Average +", round(linear.intercept_,2)

# Predicting the Gold ETF prices
predicted_price = linear.predict(X_test)  
predicted_price = pd.DataFrame(predicted_price,index=y_test.index,columns = ['price'])  
predicted_price.plot(figsize=(10,5))  
y_test.plot()  
plt.legend(['predicted_price','actual_price'])  
plt.ylabel("Gold ETF Price")
plt.show()

# the goodness of the fit using the score() function
r2_score = linear.score(X[t:],y[t:])*100
print '='*100
print float("{0:.2f}".format(r2_score))