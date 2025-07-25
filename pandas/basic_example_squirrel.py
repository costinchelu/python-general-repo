import pandas as pd
import os

SQUIRREL_FILE = "../resources/2018_Central_Park_Squirrel_Census.csv"
OUTPUT_FOLDER = "../resources/output"
OUTPUT_FILE = OUTPUT_FOLDER + "/squirrel_count.csv"

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    squirrel_dict = {}
    squirrel_df = pd.read_csv(SQUIRREL_FILE)

    colors_list = squirrel_df["Primary Fur Color"].dropna().unique()
    for color in colors_list:
        squirrel_dict[color] = len(squirrel_df[squirrel_df["Primary Fur Color"] == color])

    pd.DataFrame(
        list(squirrel_dict.items()),
        columns=["Fur Color", "Count"]
    ).to_csv(OUTPUT_FILE)


if __name__ == "__main__":
    main()