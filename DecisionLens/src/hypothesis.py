# Business Question : 
# =======================================================================
# Did the new recommendation engin improve customer purchase probability 

# Hypothesis
# =======================================================================
# null hypothesis ( H0 ) : new recommendation system have no effect on cusotmer prurchase probability 

# alternative hypothesis ( H1 ) : new recommendation systems have any affect on customer purchase probability  ( increase or decrease )

# Identifying Variables 
# =======================================================================
# independent var : experiment_group 
# dependent var : purchase_prob

# Selecting statistical test
# =======================================================================
# comarision between 
# two groups : Group A and Group B
# numeric values : purchase_prob 
# test - test

# Significance level 
# =======================================================================
# alpha = .05

# =======================================================================
# Initiating Hypothesis 
# =======================================================================

# imports
import os
import pandas as pd
import numpy as np
from scipy.stats import ttest_ind   


# path config 
data_with_prob = os.path.join('DecisionLens', 'data', 'stimulated_data_prob.csv')

data = None
if os.path.getsize(data_with_prob) == 0:
    print("Data file empty.")
else:
    data = pd.read_csv(data_with_prob)

try:
    group_a = data[data['experiment_group'] == 'A']['purchase_prob']
    group_b = data[data['experiment_group'] == 'B']['purchase_prob']

    t_stat, p_value = ttest_ind(
        group_a,
        group_b,
        equal_var=False
    )

    difference = group_b.mean() - group_a.mean()

    print(f"T-statistic : {t_stat:.4f}")
    print(f"P-value     : {p_value:.4f}")
    print(f"Mean A      : {group_a.mean():.4f}")
    print(f"Mean B      : {group_b.mean():.4f}")
    print(f"Difference  : {difference:.4f}")

    alpha = 0.05

    if p_value < alpha:
        print("\nDecision: Reject H0")
        print("Conclusion: The new recommendation engine significantly affected customer purchase probability.")
    else:
        print("\nDecision: Fail to Reject H0")
        print("Conclusion: There is insufficient evidence that the new recommendation engine changed customer purchase probability.")

except Exception as e:
    print(f"Test Failed")
    print("Error : ", e)

finally:
    print("Finished Execution")
