from models import Animal, Cat, Dog

def main():
    dog = Dog("Buddy", "Male", 5, "Chihuahua")
    cat = Cat("Musya", "Female", 3, "Orange")

    animals = [dog, cat]
    for a in animals:
        print(a)
        print(a.voice())
        if isinstance(a, Dog):
            print(a.eat())
        elif isinstance(a, Cat):
            print(a.sleep())


if __name__ == "__main__":
    main()