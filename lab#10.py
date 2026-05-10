# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 12:34:30 2026

@author: Tarin Katasema

How to run code:
Make sure you have your data file in the same folder as this python file. 

refrence used:
    
pandas.pydata.org/docs/reference/api/pandas.read_csv.html
pandas.pydata.org/docs/reference/api/pandas.DataFrame.htm
docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_1samp.html
https://docs.python.org/3/tutorial/inputoutput.html

"""

import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp, t as t_dist
import matplotlib.pyplot as plt
import stats

def summary_stats(data, label):
    lst = list(data)
    print(f"--- Summary Stats: {label} ---")
    print(f"  Mean: {stats.mean(lst)}")
    print(f"  N:    {len(lst)}")
    print(f"  SD:   {stats.sampleDev(lst)}\n")

def paired_ttest(diff, label):
    lst    = list(diff)
    n      = len(lst)
    df     = n - 1
    M_D    = stats.mean(lst)
    sd_d   = stats.sampleDev(lst)
    se     = sd_d / (n ** 0.5)
    t_crit = t_dist.ppf(0.975, df)
    t_stat, p_val = ttest_1samp(lst, popmean=0)

    print(f"=== Paired Samples T-Test: {label} ===")
    print(f"  Mean Difference:  {round(M_D, 4)}")
    print(f"  Std Dev of Diff:  {round(sd_d, 4)}")
    print(f"  t-statistic:      {round(t_stat, 4)}")
    print(f"  df:               {df}")
    print(f"  95% CI:           ({round(M_D - t_crit * se, 4)}, {round(M_D + t_crit * se, 4)})")
    print(f"  p-value (2-tail): {round(p_val, 4)}\n")
    return t_stat, p_val




stress_before = [8, 7, 6, 9, 10, 5, 7, 11, 3, 7, 7, 8]
stress_after  = [7, 5, 6, 7,  9, 6, 5,  9, 4, 7, 6, 8]
stress_diff   = [stress_before[i] - stress_after[i] for i in range(len(stress_before))]
paired_ttest(stress_diff, label="Stress Scores Verification")




df = pd.read_csv("freshman_15.csv")
print("Columns:", df.columns.tolist(), "\n")

df["Weight Diff"] = df["September Weight"] - df["April Weight"]
df["BMI Diff"]    = df["September BMI"]    - df["April BMI"]
print(df[["September Weight", "April Weight", "Weight Diff"]].head(10), "\n")
print(df[["September BMI", "April BMI", "BMI Diff"]].head(10), "\n")

plt.hist(df["Weight Diff"].tolist(), bins=8, edgecolor="black")
plt.title("Difference in Weights (September - April)")
plt.xlabel("Weight Difference")
plt.ylabel("Frequency")
plt.show()

summary_stats(df["Weight Diff"], label="Weight Difference (All)")
paired_ttest(df["Weight Diff"], label="Weight (All Students)")

males = df[df["Sex"] == "M"]
print("Male data:\n", males, "\n")

summary_stats(males["Weight Diff"], label="Weight Difference (Males)")
paired_ttest(males["Weight Diff"], label="Weight (Males Only)")

plt.hist(df["BMI Diff"].tolist(), bins=8, edgecolor="black")
plt.title("Difference in BMI (September - April)")
plt.xlabel("BMI Difference")
plt.ylabel("Frequency")
plt.show()

summary_stats(males["BMI Diff"], label="BMI Difference (Males)")
paired_ttest(males["BMI Diff"], label="BMI (Males Only)")


# 
# 
#

parent = pd.read_csv("parentht.csv")
print("parentht columns:", parent.columns.tolist())
print(parent.head(), "\n")

height_diff = parent["  \"Father's Height\""] - parent["  \"Mother's Height\""]

plt.hist(height_diff.tolist(), bins=10, edgecolor="black")
plt.title("Difference in Parent Heights (Father - Mother)")
plt.xlabel("Height Difference (inches)")
plt.ylabel("Frequency")
plt.show()

summary_stats(height_diff, label="Parent Height Difference")
paired_ttest(height_diff, label="Parent Heights")








    