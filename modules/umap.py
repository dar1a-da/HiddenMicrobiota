from umap import UMAP
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_umap(df, meta, method, 
              group_col="group",
              save_dir="../results",
              figsize=(7, 6)):
    
    # log transform
    X_log = np.log10(df + 1e-6)

    # scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_log)

    # UMAP
    umap = UMAP(
        n_components=2,
        n_neighbors=15,
        min_dist=0.1,
        random_state=42
    )

    X_umap = umap.fit_transform(X_scaled)

    # df for plot
    df_umap = pd.DataFrame(
        X_umap,
        columns=["UMAP1", "UMAP2"],
        index=df.index
    )

    df_umap["sample"] = df_umap.index
    df_umap["status"] = df_umap["sample"].map(meta[group_col])

    # plot
    plt.figure(figsize=figsize)

    sns.scatterplot(
        data=df_umap,
        x="UMAP1",
        y="UMAP2",
        hue="status",
        s=80
    )

    title = f"UMAP of microbial composition ({method})"
    plt.title(title)

    save_path = f"{save_dir}/tsne_{method.lower()}.png"

    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()

    return df_umap, umap
