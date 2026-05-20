from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_tsne(df, meta, method, 
              group_col="group",
              save_dir="../results",
              figsize=(7, 6)):
    
    # log transform
    X_log = np.log10(df + 1e-6)

    # scaling
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_log)

    # t-SNE
    tsne = TSNE(
        n_components=2,
        perplexity=30,
        random_state=42
    )

    X_tsne = tsne.fit_transform(X_scaled)

    # df for plot
    df_tsne = pd.DataFrame(
        X_tsne,
        columns=["TSNE1", "TSNE2"],
        index=df.index
    )

    df_tsne["sample"] = df_tsne.index
    df_tsne["status"] = df_tsne["sample"].map(meta[group_col])

    # plot

    palette = {"disease": "red",
        "healthy": "green"}

    plt.figure(figsize=figsize)

    sns.scatterplot(
        data=df_tsne,
        x="TSNE1",
        y="TSNE2",
        hue="status",
        s=80,
        palette=palette
    )

    title = f"t-SNE of microbial composition ({method})"
    plt.title(title)

    save_path = f"{save_dir}/tsne_{method.lower()}.png"

    plt.savefig(save_path, dpi=300, bbox_inches="tight")
    plt.show()

    return df_tsne, tsne
