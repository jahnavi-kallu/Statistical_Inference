import sys
import os

# add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from preprocessing import load_and_clean, summarize
from eda import run_eda
from t_test import run_t_test
from f_test import run_f_test
from regression import run_regression


def main():
    print("\n" + "=" * 50)
    print(" GENDER SALARY ANALYSIS PIPELINE ")
    print("=" * 50)

    # 1. Load data
    df = load_and_clean("data/Salary_data.xlsx")
    summarize(df)

    # 2. EDA
    run_eda(df)

    # 3. Hypothesis tests
    run_t_test(df)
    run_f_test(df)

    # 4. Regression
    run_regression(df)

    print("\nAnalysis complete. Results saved.")


if __name__ == "__main__":
    main()