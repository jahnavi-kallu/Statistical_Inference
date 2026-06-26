import numpy as np
import scipy.stats as stats
import os

from preprocessing import load_and_clean

PLOTS_DIR = "outputs/plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

ALPHA = 0.05


def run_f_test(df=None, verbose=True):
    if df is None:
        df = load_and_clean()

    male = df[df["Gender"] == "Male"]["Salary"].dropna().values
    female = df[df["Gender"] == "Female"]["Salary"].dropna().values

    var_m = np.var(male, ddof=1)
    var_f = np.var(female, ddof=1)

    F = var_m / var_f
    df1, df2 = len(male) - 1, len(female) - 1

    # right-tailed
    f_crit = stats.f.ppf(1 - ALPHA, df1, df2)
    p_val = 1 - stats.f.cdf(F, df1, df2)

    result = {
        "F_stat": F,
        "var_male": var_m,
        "var_female": var_f,
        "f_crit": f_crit,
        "p_value": p_val,
        "reject_H0": F > f_crit
    }

    if verbose:
        print("\nF-TEST RESULT")
        print("F-stat:", round(F, 4))
        print("p-value:", round(p_val, 6))
        print("reject H0:", result["reject_H0"])

    return result