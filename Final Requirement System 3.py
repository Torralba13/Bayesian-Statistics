"""Real World Example 3 Predicting Survey Response Rate using 
Bayesian Inferences."""

import numpy as np
import matplotlib.pyplot as plt
while True:
    print("App Download Conversion Prediction System")

    num_reached_out= int(input("Enter the number of people reached out for a survey: "))
    num_responded = int(input("Enter the number of people who responded and surveyed: "))

    if num_reached_out <= 0:
        print("The number of visitors must be greater than 0.")
    elif num_responded < 0:
        print("The number of downloads success cannot be negative.")
    elif num_responded > num_reached_out:
        print("Download success numbers cannot exceed to the number of visitors")
    else:
        
        prior_alpha = 1
        prior_beta = 1

        posterior_alpha = prior_alpha + num_responded
        posterior_beta = prior_beta + (num_reached_out - num_responded)
        posterior_samples = np.random.beta(posterior_alpha, posterior_beta, 500)

        plt.figure(figsize=(16,10))
        plt.hist(posterior_samples, bins=30, density=True, color='green', edgecolor='black')
        plt.title('Posterior Distribution of Surveyed People Rate')
        plt.xlabel('People Respondend Rate')
        plt.ylabel('Density')
        plt.xlim(min(posterior_samples), max(posterior_samples))
        plt.grid(True)
        plt.show()

        mean = posterior_alpha / (posterior_alpha + posterior_beta)
        mode = (posterior_alpha-1) / (posterior_alpha + posterior_beta - 2)
        print("Mean of People Responded Rate:", round(mean, 2))
        print("Mode of People Responded Rate:", round(mode, 2))
        
        choice = input("Do you still want to make another Survey Response prediction? (yes/no): ")
        if choice not in ["yes", "Yes", "YES"]:
            print("Thank you for using this prediction system. Until we meet again")
            break




