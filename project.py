import pandas as pd


class AnimalDataFrame:
    def __init__(self):
        self.data = {
            "animal_name": [
                "Lion",
                "Elephant",
                "Tiger",
                "Giraffe",
                "Panda",
                "Kangaroo",
                "Dolphin",
                "Shark",
                "Octopus",
            ],
            "animal_type": [
                "Mammal",
                "Mammal",
                "Mammal",
                "Mammal",
                "Mammal",
                "Mammal",
                "Water Animal",
                "Water Animal",
                "Water Animal",
            ],
            "animal_life_span": [10, 50, 15, 25, 20, 15, 20, 30, 3],
            "scientific_name": [
                "Panthera leo",
                "Loxodonta africana",
                "Panthera tigris",
                "Giraffa camelopardalis",
                "Ailuropoda melanoleuca",
                "Macropus",
                "Delphinidae",
                "Selachimorpha",
                "Octopoda",
            ],
        }
        self.df = pd.DataFrame(self.data)

    def sort_by_life_span(self):
        sorted_df = self.df.sort_values(by="animal_life_span")
        return sorted_df

    def find_animal_details_by_name(self, animal_name):
        animal_details = self.df[self.df["animal_name"] == (animal_name.title())]
        return animal_details

    def find_animal_details_by_scientific_name(self, scientific_name):
        animal_details = self.df[self.df["scientific_name"] == scientific_name]
        return animal_details

    def filter_animal_details_by_type(self, animal_type):
        filtered_details = self.df[self.df["animal_type"] == animal_type]
        return filtered_details


def menu():
    animal_data = AnimalDataFrame()
    while True:
        print("WLCOME TO ANIMAL KINGDOM \u2728  ")
        # print("\u2728")
        print("1. Sort animals by life span")
        print("2. Find animal details by name")
        print("3. Find animal details by scientific name")
        print("4. Filter animal details by type")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sorted_df = animal_data.sort_by_life_span()
            print("Sorted by life span:")
            print(sorted_df)
        elif choice == "2":
            animal_name = input("Enter animal name: ")
            animal_details = animal_data.find_animal_details_by_name(animal_name)
            print("\nDetails of", animal_name)
            print(animal_details)
        elif choice == "3":
            scientific_name = input("Enter scientific name: ")
            animal_details = animal_data.find_animal_details_by_scientific_name(
                scientific_name
            )
            print("\nDetails of animal with scientific name", scientific_name)
            print(animal_details)
        elif choice == "4":
            animal_type = input("Enter animal type: ")
            filtered_details = animal_data.filter_animal_details_by_type(animal_type)
            print("\nDetails of animals of type", animal_type)
            print(filtered_details)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again")


menu()
