import random

def main():
    people = [
        "Dane","Parker", "Shangwen", "Ved", "Jackson", "Cody", "Johan", "Luis",
        "Trostin", "Turner", "Anfal", "Ivan", "Anar", "Akshay", "Marin",
        "James", "Caleb", "Fikir", "Jamethiel", "Isaac", "Adonis"
    ]

    groups = {
        "Group A": 3,
        "Group B": 3,
        "Group C": 3,
        "Group D": 3,
        "Group E": 3,
        "Group F": 2,
        "Group G": 2,
        "Group H": 2,
    }
    random.shuffle(people)

    for key in groups:
        print(f'{key}: ', end='')
        group = []
        for i in range(groups[key]):
            group.append(people.pop())
        print(', '.join(group))


if __name__ == '__main__':
    main()
