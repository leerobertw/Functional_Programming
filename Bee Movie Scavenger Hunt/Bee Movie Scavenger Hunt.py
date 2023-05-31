# Bee Movie Scavenger Hunt assignment
# The file "Bee Movie.txt" must be in the same directory

def load_file():
    with open("Bee Movie.txt", 'r') as file:
        return [line.strip() for line in file]


def find_jazz(script):
    index = 0
    for line in script:
        if "You like jazz?" in line:
            return index, line.find("You like jazz?")
        index += 1
    return -1, -1


def find_bees(script):
    count = 0
    for line in script:
        count += line.count("bee")
    return count


def find_bees_stretch(script):
    count = 0
    for line in script:
        count += line.count("bee ") + line.count("bees ") + line.count("Bee ") + line.count("Bees ")
    return count


def last_line(data):
    return data[-1]


def main():
    data = load_file()
    index, offset = find_jazz(data)
    print(f"The line \"You like jazz?\" is at index {index + 1} and offset {offset + 1}", )
    print(f"The text \"bee\" appeared {find_bees(data)} times in the script.")
    print(f"The actual word 'bee' appeared {find_bees_stretch(data)} times in the script")
    print(f"The last line of the script is: \"{last_line(data)}\"")


if __name__ == '__main__':
    main()
