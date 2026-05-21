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
    figsize=(7, 6),
    distance_matrix=False
):

    # distance matrix (f.e. Mash)
    if distance_matrix:
        X_scaled = df
        sample_index = meta.index

    # abundance table
    else:
        X = df.T.astype(float)

        if method.lower() == "metaphlan":
            X = X / 100

        # log transform
        X_log = np.log10(X + pseudocount)

        # scaling
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X_log)

        sample_index = X.index

    # PCA
    pca = PCA(n_components=2)

    X_pca = pca.fit_transform(X_scaled)

    # dataframe for plot
    pca_df = pd.DataFrame(
        X_pca,
        columns=["PC1", "PC2"],
        index=sample_index
    )

    pca_df["status"] = pca_df.index.map(meta[group_col])

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

    plt.title(f"PCA of microbial composition ({method})")

    save_path = f"{save_dir}/pca_{method.lower()}.png"

    plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()

    return pca_df, pca
