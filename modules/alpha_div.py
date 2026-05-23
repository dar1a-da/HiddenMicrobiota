import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_shannon(
    df,
    meta,
    method,
    group_col="group",
    save_dir="../results",
    figsize=(6, 6)
):
    """
    df: rows - samples, 
        columns - features
    """

    # Metaphlan returns percentages
    if method.lower() == "metaphlan":
        df = df / 100

    # Shannon index
    def shannon(row):
        p = row[row > 0]
        return -(p * np.log(p)).sum()

    shannon_index = df.apply(shannon, axis=1)

    # df for plot
    shannon_df = pd.DataFrame({
        "sample": shannon_index.index,
        "shannon": shannon_index.values
    }).set_index("sample")

    shannon_df["group"] = meta[group_col]

    # plot
    plt.figure(figsize=figsize)

    sns.boxplot(
        data=shannon_df,
        x="group",
        y="shannon"
    )

    plt.title(f"Shannon diversity index ({method})")

    save_path = f"{save_dir}/shannon_{method.lower()}.png"

    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()

    return shannon_df


