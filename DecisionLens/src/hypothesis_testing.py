# Hypothesis testign engine 
# Performing ttest on the data 
# Reason : 2 Groups only and relation between cat and num cols 
# Results : t-statistic , p-value, business conclusion

from scipy.stats import ttest_ind
import pandas as pd

def get_group_summary(df):

    summary = (
        df.groupby("experiment_group")["purchase_prob"]
        .agg(
            Mean="mean",
            Median="median",
            Std="std",
            Count="count"
        )
        .round(3)
    )

    return summary

def perform_ttest(df):

    group_a = df.loc[
        df["experiment_group"] == "A",
        "purchase_prob"
    ]

    group_b = df.loc[
        df["experiment_group"] == "B",
        "purchase_prob"
    ]

    t_stat, p_value = ttest_ind(
        group_a,
        group_b,
        equal_var=False
    )

    return t_stat, p_value

def hypothesis_result(p_value, alpha=0.05):

    if p_value < alpha:

        return {
            "Decision": "Reject Null Hypothesis",
            "Result": True
        }

    return {
        "Decision": "Fail to Reject Null Hypothesis",
        "Result": False
    }

def business_conclusion(result):

    if result:

        return (
            "The experimental recommendation strategy "
            "produced a statistically significant increase "
            "in purchase probability."
        )

    return (
        "The experiment did not produce sufficient evidence "
        "to conclude that the recommendation strategy "
        "improved purchase probability."
    )