import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1)
Nsim = 10000
m = 200
mu = 2
xrange = np.linspace(0,5,100)

means = []

for i in range(Nsim):
    # Unobservable Poission
    y = np.random.poisson(mu, m)
    # How many of the eggs have bacteria?
    r = sum([1 if yi > 0 else 0 for yi in y])
    # Division by zero error!
    try:
        mu_hat = np.log(m / (m-r))
    except ZeroDivisionError:
        continue
    means.append(mu_hat)


Femp = lambda means: [np.sum(means < x) / len(means) for x in xrange]
print("Estimated mean: ", np.mean(means))
print("Estimated variance: ", np.var(means))
theoretical_var = (np.exp(mu) - 1) / m
print("Theoretical variance: ", theoretical_var)

plt.plot(xrange,Femp(means))
plt.xlabel("x")
plt.ylabel("Fn(x)")
plt.title("Empirical CDF")
plt.savefig("CDF2.png")
plt.close()

from scipy.stats import probplot
plt.figure(figsize=(12, 10))

for j, m in enumerate([20, 50, 100, 500]):
    mu_hats = []
    for i in range(Nsim):
        y = np.random.poisson(mu, m)
        r = sum([1 if yi > 0 else 0 for yi in y])
        try:
            mu_hat = np.log(m / (m - r))
        except ZeroDivisionError:
            continue
        mu_hats.append(mu_hat)

    plt.subplot(2, 2, j + 1)
    probplot(mu_hats, dist="norm", plot=plt)
    plt.title(f"Normal Q-Q plot, m = {m}")

plt.tight_layout()
plt.savefig("QQ.png")
plt.show()