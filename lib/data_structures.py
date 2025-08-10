spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods_list = []
    for food in spicy_foods:
        if food["heat_level"] > 5:
            spiciest_foods_list.append(food)
    return spiciest_foods_list

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food["name"]
        cuisine = food["cuisine"]
        heat_level = food["heat_level"]
        chili_emojis = "🌶" * heat_level
        print(f"{name} ({cuisine}) | Heat Level: {chili_emojis}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_food_list = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_food_list)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    
    total_heat = 0
    for food in spicy_foods:
        total_heat += food["heat_level"]
    
    average = total_heat / len(spicy_foods)
    return int(average)

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods

