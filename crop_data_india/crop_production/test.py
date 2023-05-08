import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def plotfucntion(df):
    """plots different functions for given data frame"""

    df["Mean value"] = df["Season"] + df["mean_p/a"].astype('str')

    # plot Season wise production for different season over the years
    sns.relplot(data=df, x="Year", y="P/A", kind="line", hue="Season",
                col="Mean value", markers="Season", row="Area cat")
    plt.show()

    # plot barplot of seasons
    sns.barplot(data=df, x="Season", y="p/a",)
    plt.title(f"Rice production/Area in {df} based on seasons")
    plt.show()

    # plot district wise production
    fig, ax = plt.subplots(figsize=(20, 30))
    sns.barplot(data=df, x="P/A", y="District_Name", hue="Season")
    plt.title(f"Rice Prodiction in {df} District wise data")
    plt.show()

    # Rice Farming distribution across Karantaka districts

    fig, ay = plt.subplots(figsize=(20, 30))
    sns.barplot(data=df, x="P/A", y="District_Name", hue="Area cat")
    plt.title("Rice farming Area distribution across the state")
