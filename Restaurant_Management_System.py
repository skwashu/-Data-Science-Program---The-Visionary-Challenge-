class FoodItem:
    def __init__(self, code, name, price, quantity):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = quantity

class RestaurantManagementSystem:
    def __init__(self):
        self.food_items = [
            FoodItem("FI001", "Cheeseburger", 50, 10),
            FoodItem("FI002", "Pizza", 90, 15),
            FoodItem("FI003", "Caesar Salad", 35, 20),
            FoodItem("FI004", "Chicken Wings", 60, 25),
            FoodItem("FI005", "Fried Rice", 70, 30)
        ]
    
    def print_menu(self):
        print("Menu:")
        print("------------------------------")
        print("{:<10} {:<20} {:<10}".format("Code", "Item", "Price"))
        for item in self.food_items:
            print("{:<10} {:<20} {:<10}".format(item.code, item.name, item.price))
    
    def place_order(self, code, quantity):
        for item in self.food_items:
            if item.code == code:
                if item.quantity < quantity:
                    print("Sorry, we do not have enough", item.name, "available.")
                    return False
                else:
                    item.quantity -= quantity
                    print("Order placed successfully.")
                    print("Total price:", quantity * item.price)
                    return True
        print("Invalid food code.")
        return False

# Example usage:
restaurant = RestaurantManagementSystem()
restaurant.print_menu()
restaurant.place_order("FI001", 2)
restaurant.place_order("FI002", 3)
restaurant.place_order("FI006", 1)
