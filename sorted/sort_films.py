import csv


def parse_name(full_name):
    name_parts = full_name.split(" ")
    if name_parts[-1][0].islower():
        return name_parts[0], ''
    else:
        return name_parts[-1], name_parts[0]


def load_data(filename):
    with open(filename) as file:
        reader = csv.reader(file)
        return [row for row in reader]


def sort_by_director(data):
    return sorted(data, key=lambda film: (parse_name(film[0]), film[1]))


def sort_by_year(data):
    return sorted(data, key=lambda film: (film[1], parse_name(film[0])))


def print_films(sorted_films):
    for film in sorted_films:
        print(f"Director: {film[0]}, Year:{film[1]}, {film[2]}")


def main():
    data = load_data("films.csv")
    print("Films sorted by director")
    print_films(sort_by_director(data))

    print()
    print("Films sorted by year")
    print_films((sort_by_year(data)))


main()
