import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import os

from preprocessing import load_and_clean

PLOTS_DIR = "outputs/plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

ALPHA = 0.05


def run_t_test(df=None, verbose=True):
    if df is None:
        df = load_and_clean()

    male = df[df["Gender"] == "Male"]["Salary"].dropna().values
    female = df[df["Gender"] == "Female"]["Salary"].dropna().values

    # Welch t-test
    t_stat, p_two = stats.ttest_ind(male, female, equal_var=False)

    # one-tailed p-values
    p_right = p_two / 2 if t_stat > 0 else 1 - p_two / 2
    p_left  = p_two / 2 if t_stat < 0 else 1 - p_two / 2

    # mean difference
    diff = male.mean() - female.mean()

    # standard error
    vm, vf = np.var(male, ddof=1), np.var(female, ddof=1)
    nm, nf = len(male), len(female)
    se = np.sqrt(vm/nm + vf/nf)

    # Welch df
    df_w = (vm/nm + vf/nf)**2 / ((vm/nm)**2/(nm-1) + (vf/nf)**2/(nf-1))

    # CI
    t_crit = stats.t.ppf(1 - ALPHA/2, df_w)
    ci = (diff - t_crit*se, diff + t_crit*se)

    result = {
        "t_stat": t_stat,
        "p_two": p_two,
        "p_right": p_right,
        "p_left": p_left,
        "mean_diff": diff,
        "ci": ci,
        "reject": p_two < ALPHA
    }

    if verbose:
        print("\nT-TEST RESULT")
        print("t-stat:", round(t_stat, 4))
        print("p-value:", round(p_two, 6))
        print("mean diff:", round(diff, 2))
        print("CI:", (round(ci[0], 2), round(ci[1], 2)))
        print("Reject H0:", result["reject"])

    return result