import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.55,1.9, num=60)
test=np.linspace(0,2)
uniform_distribution = sts.uniform.pdf(mu) + 1

uniform_distribution = uniform_distribution/uniform_distribution.sum()
beta_dist = sts.beta.pdf(mu, 3, 8, loc=1.55, scale = 0.5)
beta_dist = beta_dist/beta_dist.sum()
plt.plot(mu, beta_dist, label = "Beta Distribution")
plt.plot(mu, uniform_distribution, label = "Uniform Distribution")
plt.xlabel("Value of $\mu$ in meters")
plt.ylabel("Probability density")
plt.legend()



