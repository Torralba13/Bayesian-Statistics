# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 18:32:53 2025

@author: Matthew
"""

"""Real World Example: Predicting the Coffee Orders that is being orderd in Website 
Using Bayesian Inference. This system is trying to predict how many coffee consumers 
will buy an coffee product to the ratio of the number of the website visitors.The following python 
is written below for this system."""

import numpy as np
import matplotlib.pyplot as plt


num_coffee_website_visitors = 500
num_coffee_order = 75

prior_alpha = 1
prior_beta = 1

posterior_alpha = prior_alpha + num_coffee_order
posterior_beta = prior_beta + (num_coffee_website_visitors- num_coffee_order)

posterior_samples = np.random.beta(posterior_alpha, posterior_beta, size=500)

plt.figure(figsize=(12,8))
plt.hist(posterior_samples, bins = 30, density=True, color='blue', edgecolor='black', alpha=0.7)
plt.title('Posterior Distribution of Number of Coffee Orders', fontsize=16)
plt.xlabel('Order Rate', fontsize=14)
plt.ylabel('Density', fontsize=14)
plt.xlim(0,0.3)
plt.show()

mean_order_rate = posterior_alpha/(posterior_alpha + posterior_beta)
mode_order_rate = (posterior_alpha-1)/(posterior_alpha + posterior_beta - 2)
print("Mean Order Rate:", round(mean_order_rate,2))
print("Mode Order Rate:", round(mode_order_rate,2))


