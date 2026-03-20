import numpy as np
import math
import random
import matplotlib.pyplot as plt
#i have assumed that the the probability function is F(x)=Lambda. e^(-lambda*x)
#the corresponding cdf function is 1-e^(-lamda*x)
#the inverse of the cdf is x=-1/lambda*ln(1-u) where u is the uniform random variable
def inverse_cdf(Lambda,u):#this function returns the value we get from plugging in our random uniform variables into the inverse of the cdf function
    return (-1/Lambda)*(math.log(u))
Lambda=10
arr=[]
for i in range(100000):#taking large amount of simulations for accurate data
    u=random.random()
    value=inverse_cdf(Lambda,u)
    arr.append(value)
plt.hist(arr,bins=300)
plt.title("Probability distribution")
plt.xlabel("Generated Exponential Value")
plt.ylabel("Frequency")
plt.show()



