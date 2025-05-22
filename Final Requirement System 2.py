"""Real World Example 2 Predicting App Download Conversion Rate using 
Bayesian Inferences."""

import numpy as np
import matplotlib.pyplot as plt
while True:
    print("App Download Conversion Prediction System")

    num_visitors= int(input("Enter the number of website visitors: "))
    num_downloads = int(input("Enter the number of Download Success: "))

    if num_visitors <= 0:
        print("The number of visitors must be greater than 0.")
    elif num_downloads < 0:
        print("The number of downloads success cannot be negative.")
    elif num_downloads > num_visitors:
        print("Download success numbers cannot exceed to the number of visitors")
    else:
        
        prior_alpha = 1
        prior_beta = 1

        posterior_alpha = prior_alpha + num_downloads
        posterior_beta = prior_beta + (num_visitors - num_downloads)
        posterior_samples = np.random.beta(posterior_alpha, posterior_beta, 500)

        plt.figure(figsize=(16,10))
        plt.hist(posterior_samples, bins=30, density=True, color='green', edgecolor='black')
        plt.title('Posterior Distribution of Download Conversion Rate')
        plt.xlabel('Download Rate')
        plt.ylabel('Density')
        plt.xlim(min(posterior_samples), max(posterior_samples))
        plt.grid(True)
        plt.show()

        mean = posterior_alpha / (posterior_alpha + posterior_beta)
        mode = (posterior_alpha-1) / (posterior_alpha + posterior_beta - 2)
        print("Mean of Download Rate:", round(mean, 2))
        print("Mode of Download Rate:", round(mode, 2))
        
        choice = input("Do you still want to make another App Downloader prediction? (yes/no): ")
        if choice not in ["yes", "Yes", "YES"]:
            print("Thank you for using this prediction system. Until we meet again")
            break




