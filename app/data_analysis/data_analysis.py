import pandas as pd
from app.scraping.parse import get_page_info


def technologies_analysis():
    df = pd.DataFrame.from_dict(get_page_info(), orient="index")
    df = df.T  # swap rows and columns
    df["Git"] = df["GIT"] + df["git"]
    df = df.drop(columns=["GIT", "git"])
    df = df.T.sort_values(0, ascending=False)
    df.plot.bar(
        title="Technologies used in Python",
        figsize=(8, 4),
        ylabel="number of occurrences",
        xlabel="technology name",
        legend=False,
    )


if __name__ == '__main__':
    technologies_analysis()
