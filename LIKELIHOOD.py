#Likelihood
import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu=np.linspace(1.55,1.9, num = 60)


def likelihood(datum,mu):
    likelihood_output = sts.norm.pdf(datum, mu, scale = 0.5)
    return likelihood_output/likelihood_output.sum()

likelihood_output = likelihood(1.65, mu)

plt.plot(mu, likelihood_output)
plt.title("The likelihood of $\mu$ given observation 1.65m")
plt.ylabel("Probability Density/Likelihood")
plt.xlabel("Value of $\mu$")
plt.show()