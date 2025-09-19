import matplotlib.pyplot as plt
import pandas as pd

def scatter(df: pd.DataFrame, x: str, y: str, hue: str = "target_name"):
    fig, ax = plt.subplots()
    for name, g in df.groupby(hue):
        ax.scatter(g[x], g[y], label=name)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.legend(title=hue)
    return fig