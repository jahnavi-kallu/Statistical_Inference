import pandas as pd

def load_and_clean(path="data/Salary_data.xlsx"):
    df = pd.read_excel(path)

    # clean string columns
    for col in df.select_dtypes(include="object"):
        df[col] = df[col].str.strip()

    # drop missing values + duplicates
    df = df.dropna().drop_duplicates()

    # remove outliers (IQR method)
    q1 = df["Salary"].quantile(0.25)
    q3 = df["Salary"].quantile(0.75)
    iqr = q3 - q1

    df = df[(df["Salary"] >= q1 - 3 * iqr) & (df["Salary"] <= q3 + 3 * iqr)]

    print("Dataset shape:", df.shape)
    return df


def summarize(df):
    print("\nGender count:\n", df["Gender"].value_counts())

    print("\nSalary by Gender:\n",
          df.groupby("Gender")["Salary"].mean().round(2))

    print("\nSalary by Education:\n",
          df.groupby("Education Level")["Salary"].mean().round(2))