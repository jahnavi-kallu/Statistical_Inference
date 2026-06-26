import numpy as np
import pandas as pd
import scipy.stats as stats

from preprocessing import load_and_clean


def prepare_data(df):
    df = df.copy().reset_index(drop=True)

    # Binary gender feature
    df["Male"] = (df["Gender"] == "Male").astype(int)

    # Drop original Gender column BEFORE get_dummies (fixes the string→float error)
    df.drop(columns=["Gender"], inplace=True)

    # Dummy encode Education Level and Job Title
    df = pd.get_dummies(df, columns=["Education Level", "Job Title"], drop_first=True)

    df.dropna(inplace=True)

    # Target & features
    y = df["Salary"].values.astype(float)
    X = df.drop(columns=["Salary"]).values.astype(float)

    # Add intercept column
    X = np.c_[np.ones(len(X)), X]
    return X, y, df.drop(columns=["Salary"]).columns.tolist()


def run_regression(df=None):
    if df is None:
        df = load_and_clean()

    X, y, col_names = prepare_data(df)
    n, p = X.shape

    # OLS from scratch
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    y_hat = X @ beta
    resid = y - y_hat

    # Metrics
    ssr = np.sum(resid ** 2)
    sst = np.sum((y - y.mean()) ** 2)
    r2     = 1 - ssr / sst
    adj_r2 = 1 - (1 - r2) * (n - 1) / (n - p)

    # Standard errors, t-stats, p-values
    sigma2 = ssr / (n - p)
    se     = np.sqrt(np.diag(sigma2 * np.linalg.pinv(X.T @ X)))
    t_stats = beta / se
    p_vals  = 2 * (1 - stats.t.cdf(np.abs(t_stats), df=n - p))
    ci_low  = beta - 1.96 * se
    ci_high = beta + 1.96 * se

    # Find Male coefficient index (intercept is index 0, then col_names)
    all_names = ["intercept"] + col_names
    male_idx  = all_names.index("Male")

    print("\nREGRESSION RESULTS")
    print(f"R²     : {round(r2, 4)}")
    print(f"Adj R² : {round(adj_r2, 4)}")
    print(f"\nCoefficient (Male) : {round(beta[male_idx], 2)}")
    print(f"t-statistic (Male) : {round(t_stats[male_idx], 3)}")
    print(f"p-value (Male)     : {round(p_vals[male_idx], 4)}")
    print(f"95% CI (Male)      : ({round(ci_low[male_idx], 2)}, {round(ci_high[male_idx], 2)})")
    decision = "Reject H0 — gender significantly affects salary." \
        if p_vals[male_idx] < 0.05 else \
        "Fail to reject H0 — no significant gender effect after controls."
    print(f"Decision (α=0.05)  : {decision}")

    return beta, r2, adj_r2


if __name__ == "__main__":
    run_regression()