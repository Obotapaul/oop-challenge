
from pet import Pet

def main():
    pet = Pet("Jay")
    pet.get_status()
    print()
    pet.eat()
    pet.sleep()
    pet.play()
    print()
    pet.train("attack 🐶")
    pet.train("jump 🐕‍🦺")
    print()
    pet.show_tricks()
    print()
    pet.get_status()

if __name__ == "__main__":
    main()
