from prettytable import PrettyTable

def prettytable_example():
    pokemon_table = PrettyTable()
    pokemon_table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    pokemon_table.add_column("Type", ["Electric", "Water", "Fire"])
    pokemon_table.align = "l"
    print(pokemon_table)


def main():
    prettytable_example()


if __name__ == "__main__":
    main()