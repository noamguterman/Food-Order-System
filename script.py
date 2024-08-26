italian_food = ["Pasta Bolognese", "Pepperoni pizza", "Margherita pizza", "Lasagna"]
indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
  if name in menu:
    return name

def select_meal(name, food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)

def display_available_meals(food_type):
  if food_type == "Italian":
    print("Available Italian Meals:")
    for i in italian_food:
      print(i)
  elif food_type == "Indian":
    print("Available Indian Meals:")
    for i in indian_food:
      print(i)
  else:
    print("Invalid food type")

def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"Meal: {name} Quantity: {amount}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")
type_input = input("What cuisine would you like to try? ")
display_available_meals(type_input)
name_input = input("What would you like to order? ")
amount_input = input("How many dishes would you like? ")
result = create_summary(name_input, amount_input, type_input)
print(result)