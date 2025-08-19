import pandas

CSV_FILE = "../resources/nato_phonetic_alphabet.csv"

def main():
    df = pandas.read_csv(CSV_FILE)
    nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

    name = input("Enter text to convert: ").upper()

    result = [nato_dict[letter] for letter in name if letter.isalnum()]
    print(result)

if __name__ == "__main__":
    main()