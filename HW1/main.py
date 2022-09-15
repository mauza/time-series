import pandas as pd

def main():
    df = pd.read_csv("data/utah_house_prices.csv")
    df = df.sort_values(by=["last_update"])
    df["last_update"] = df["last_update"].astype('datetime64[ns]')
    print(df.info())
    s2 = df.groupby(df.last_update.dt.month).count()
    print(s2)


if __name__ == "__main__":
    main()
