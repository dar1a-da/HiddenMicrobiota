from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_pca(
    df,
    meta,
    method,
    group_col="group",
    pseudocount=1e-6,
    save_dir="../results",
    figsize=(7, 6)
):
    # log transform
    X_log = np.log10(df + pseudocount)

    # scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_log)

    # PCA
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X_scaled)

    # DF for plot
    pca_df = pd.DataFrame(
        X_pca,
        columns=["PC1", "PC2"],
        index=df.index
    )

    pca_df["sample"] = pca_df.index
    pca_df["status"] = pca_df["sample"].map(meta[group_col])

    # plot

    palette = {"disease": "red",
        "healthy": "green"}
    
    plt.figure(figsize=figsize)

    sns.scatterplot(
        data=pca_df,
        x="PC1",
        y="PC2",
        hue="status",
        s=80, 
        palette=palette
    )

    plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0] * 100:.1f}%)")
    plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1] * 100:.1f}%)")

    title = f"PCA of microbial composition ({method})"
    plt.title(title)

    save_path = f"{save_dir}/pca_{method.lower()}.png"

    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()

    return pca_df, pca