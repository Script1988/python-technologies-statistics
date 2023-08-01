import pandas as pd
from app.scraping.parse import get_page_info


def technologies_analysis():
    data = get_page_info()
    df = pd.DataFrame.from_dict(data, orient="index")
    df = df.T  # swap rows and columns
    df["Git"] = df["GIT"] + df["git"]
    df = df.drop(columns=["GIT", "git"])
    df = df.T.sort_values(0, ascending=False)
    ax = df.plot.bar(
        title="Technologies used in Python",
        figsize=(15, 5),
        ylabel="Number of occurrences",
        xlabel="Technology name",
        legend=False,
    )
    # Calculating the number of occurrences for every technology and displaying them over the bar
    for p in ax.patches:
        ax.annotate(
            str(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()),
            ha="center", va="bottom"
        )


if __name__ == '__main__':
    technologies_analysis()
