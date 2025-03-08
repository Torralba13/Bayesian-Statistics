#Posterior
import scipy.stats as sts
import numpy as np
import matplotlib.pyplot as plt

mu = np.linspace(1.55,1.9, num=60)
test=np.linspace(0,2)
uniform_distribution = sts.uniform.pdf(mu) + 1

uniform_distribution = uniform_distribution/uniform_distribution.sum()
beta_dist = sts.beta.pdf(mu, 3, 8, loc=1.55, scale = 0.5)
beta_dist = beta_dist/beta_dist.sum()

def likelihood(datum,mu):
    likelihood_output = sts.norm.pdf(datum, mu, scale = 0.5)
    return likelihood_output/likelihood_output.sum()

likelihood_output = likelihood(1.65, mu)

unnormalized_posterior = likelihood_output * uniform_distribution
plt.plot(mu, unnormalized_posterior)
plt.xlabel("$\mu$ in meters")
plt.ylabel("Unnormalized Posterior")
plt.show()
