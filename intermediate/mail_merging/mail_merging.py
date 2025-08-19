import os

LETTER_FILE = "./input/starting_letter.txt"
INVITED_FILE = "./input/invited_names.txt"
OUTPUT_FOLDER = "./output"
PLACEHOLDER = "[name]"

def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    with open(INVITED_FILE) as invited_file:
        names = invited_file.readlines()

    with open(LETTER_FILE) as letter_file:
        letter_content = letter_file.read()
        for name in names:
            stripped_name = name.strip()
            new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
            with open(f"./output/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)


if __name__ == "__main__":
    main()