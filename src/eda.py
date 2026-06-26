import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns

from preprocessing import load_and_clean

PLOTS_DIR = "outputs/plots"
os.makedirs(PLOTS_DIR, exist_ok=True)

# Clean, soft professional palette
PALETTE    = {"Female": "#F4A7B9", "Male": "#7EB8D4"}
FEMALE_CLR = "#F4A7B9"
MALE_CLR   = "#7EB8D4"
SINGLE_CLR = "#7EB8D4"

sns.set_theme(style="whitegrid", font_scale=1.1)
plt.rcParams.update({
    "figure.dpi":       150,
    "axes.spines.top":  False,
    "axes.spines.right":False,
    "axes.titleweight": "bold",
    "axes.titlesize":   13,
    "axes.labelsize":   11,
    "figure.figsize":   (8, 5),
})


def save_plot(name):
    plt.tight_layout()
    plt.savefig(f"{PLOTS_DIR}/{name}", dpi=150, bbox_inches="tight")
    plt.close()


def plot_basic_distributions(df):
    # Salary histogram
    fig, ax = plt.subplots()
    ax.hist(df["Salary"], bins=30, color=SINGLE_CLR, edgecolor="white", linewidth=0.6)
    ax.set_title("Salary Distribution")
    ax.set_xlabel("Salary (USD)")
    ax.set_ylabel("Frequency")
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    plt.xticks(rotation=20)
    save_plot("salary_dist.png")

    # Salary by gender boxplot
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Gender", y="Salary", hue="Gender",
                palette=PALETTE, legend=False,
                linewidth=1.2, flierprops=dict(marker="o", markersize=4, alpha=0.5),
                ax=ax)
    ax.set_title("Salary Distribution by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Salary (USD)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    save_plot("salary_by_gender.png")


def plot_experience_age(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Gender", y="Age", hue="Gender",
                palette=PALETTE, legend=False,
                linewidth=1.2, flierprops=dict(marker="o", markersize=4, alpha=0.5),
                ax=ax)
    ax.set_title("Age Distribution by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Age (years)")
    save_plot("age_by_gender.png")

    fig, ax = plt.subplots()
    sns.boxplot(data=df, x="Gender", y="Years of Experience", hue="Gender",
                palette=PALETTE, legend=False,
                linewidth=1.2, flierprops=dict(marker="o", markersize=4, alpha=0.5),
                ax=ax)
    ax.set_title("Experience Distribution by Gender")
    ax.set_xlabel("Gender")
    ax.set_ylabel("Years of Experience")
    save_plot("exp_by_gender.png")


def plot_relationships(df):
    fig, ax = plt.subplots(figsize=(9, 5))
    for g in ["Female", "Male"]:
        sub = df[df["Gender"] == g]
        ax.scatter(sub["Years of Experience"], sub["Salary"],
                   label=g, alpha=0.35, s=18,
                   color=PALETTE.get(g, "gray"), edgecolors="none")
    ax.set_title("Salary vs. Years of Experience by Gender")
    ax.set_xlabel("Years of Experience")
    ax.set_ylabel("Salary (USD)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax.legend(title="Gender", framealpha=0.7)
    save_plot("salary_vs_exp.png")


def plot_education(df):
    # Standardise education labels before plotting
    edu_map = {
        "Bachelor's":        "Bachelor's Degree",
        "Master's":          "Master's Degree",
        "phD":               "PhD",
    }
    df2 = df.copy()
    df2["Education Level"] = df2["Education Level"].replace(edu_map)

    order = ["High School", "Bachelor's Degree", "Master's Degree", "PhD"]
    order = [e for e in order if e in df2["Education Level"].unique()]

    fig, ax = plt.subplots(figsize=(9, 5))
    sns.boxplot(data=df2, x="Education Level", y="Salary",
                order=order, color=SINGLE_CLR,
                linewidth=1.2, flierprops=dict(marker="o", markersize=4, alpha=0.5),
                ax=ax)
    ax.set_title("Salary by Education Level")
    ax.set_xlabel("Education Level")
    ax.set_ylabel("Salary (USD)")
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    plt.xticks(rotation=15)
    save_plot("salary_by_edu.png")


def plot_correlation(df):
    df2 = df.copy()
    df2["Gender"] = (df2["Gender"] == "Male").astype(int)

    corr = df2.select_dtypes(include="number").corr()

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r",
                center=0, linewidths=0.5,
                annot_kws={"size": 9}, ax=ax)
    ax.set_title("Correlation Heatmap")
    save_plot("correlation.png")


def run_eda(df):
    print("[EDA] Running analysis...")
    plot_basic_distributions(df)
    plot_experience_age(df)
    plot_relationships(df)
    plot_education(df)
    plot_correlation(df)
    print("[EDA] Done — plots saved to", PLOTS_DIR)


if __name__ == "__main__":
    df = load_and_clean()
    run_eda(df)