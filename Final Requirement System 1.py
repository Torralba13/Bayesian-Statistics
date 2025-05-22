"""Real World Example 1 Predicting the Newsletter Signups from Website Visitors using 
Bayesian Inferences."""

import numpy as np
import matplotlib.pyplot as plt
while True:
    print("NewsLetter SignUps Prediction System")

    num_visitors_website = int(input("Enter the number of website visitors: "))
    num_signups = int(input("Enter the number of Sign-Ups: "))

    if num_visitors_website <= 0:
        print("The number of visitors must be greater than 0.")
    elif num_signups < 0:
        print("The number of sign ups cannot be negative.")
    elif num_signups > num_visitors_website:
        print("Sign ups numbers cannot exceed to the number of visitors")
    else:
        
        prior_alpha = 1
        prior_beta = 1

        posterior_alpha = prior_alpha + num_signups
        posterior_beta = prior_beta + (num_visitors_website - num_signups)
        posterior_samples = np.random.beta(posterior_alpha, posterior_beta, 500)

        plt.figure(figsize=(10,6))
        plt.hist(posterior_samples, bins=30, density=True, color='green', edgecolor='black')
        plt.title('Posterior Distribution of Newsletter Signup Rate')
        plt.xlabel('Signup Rate')
        plt.ylabel('Density')
        plt.xlim(min(posterior_samples), max(posterior_samples))
        plt.grid(True)
        plt.show()

        mean = posterior_alpha / (posterior_alpha + posterior_beta)
        mode = (posterior_alpha-1) / (posterior_alpha + posterior_beta - 2)
        print("Mean of Sign Up Rate:", round(mean, 2))
        print("Mode of Sign Up Rate:", round(mode, 2))
        
        choice = input("Do you still want to make another newsletter sign up prediction? (yes/no): ")
        if choice not in ["yes", "Yes", "YES"]:
            print("Thank you for using this prediction system. Until we meet again")
            break




