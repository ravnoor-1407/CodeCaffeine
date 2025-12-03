# Define the menu structure of CodeCaffeine
menu = {
    "Beverages": {
        "Hot Coffees": {
            "Caffè Americano": 250,
            "Caffè Latte": 320,
            "Cappuccino": 320,
            "Espresso": 200,
            "Flat White": 350,
            "Mocha": 360,
        },
        "Hot Teas": {
            "Chai Tea Latte": 280,
            "Matcha Green Tea Latte": 340,
            "Royal English Breakfast Tea": 240,
            "Earl Grey Tea": 240,
        },
        "Cold Coffees": {
            "Iced Caffè Americano": 280,
            "Iced Caffè Latte": 350,
            "Iced Caramel Macchiato": 380,
            "Cold Brew Coffee": 320,
        },
        "Cold Teas": {
            "Iced Black Tea": 260,
            "Iced Green Tea": 260,
            "Iced Passion Tango Tea": 280,
            "Iced Chai Tea Latte": 310,
        },
        "Frappuccinos": {
            "Mocha Frappuccino": 380,
            "Caramel Frappuccino": 380,
            "Java Chip Frappuccino": 400,
            "Vanilla Bean Crème Frappuccino": 380,
        },
        "Refreshers": {
            "Strawberry Acai Refresher": 320,
            "Mango Dragonfruit Refresher": 320,
            "Very Berry Hibiscus Refresher": 320,
            "Pink Drink": 340,
        },
        "Bottled Beverages": {
            "Bottled Iced Coffee": 280,
            "Bottled Cold Brew": 300,
            "Bottled Juice": 250,
            "Bottled Water": 100,
        },
    },
    "Food": {
        "Breakfast": {
            "Bacon, Gouda & Egg Sandwich": 420,
            "Spinach, Feta & Egg White Wrap": 400,
            "Classic Oatmeal": 280,
            "Blueberry Muffin": 220,
        },
        "Lunch": {
            "Turkey & Havarti Sandwich": 480,
            "Chicken & Quinoa Protein Bowl": 550,
            "Caesar Salad with Grilled Chicken": 520,
            "Tomato Basil Soup": 340,
        },
        "Snacks": {
            "Chocolate Chip Cookie": 180,
            "Fruit & Nut Mix": 250,
            "Yogurt Parfait": 300,
            "Bagel with Cream Cheese": 280,
        },
        "Desserts": {
            "Cheesecake": 380,
            "Lemon Loaf Cake": 320,
            "Chocolate Brownie": 240,
            "Cinnamon Roll": 280,
            "Chocolate Croissant": 260,
            "Red Velvet Cake Pop": 140,
        },
        "Treats": {
            "Pumpkin Spice Latte": 360,
            "Peppermint Mocha": 360,
            "Caramel Brulée Latte": 380,
            "Toasted White Chocolate Mocha": 380,
        },
        "Bakery": {
            "Butter Croissant": 240,
            "Almond Croissant": 280,
            "Multigrain Bagel": 220,
            "Cinnamon Swirl Coffee Cake": 300,
        }
    }
}

# Greet the customer
print("Welcome to CodeCaffiene!")
print("Here is our menu:")
for category, items in menu.items():
    print(f"{category}:")
    for subcategory, items_dict in items.items():
        print(f"  {subcategory}:")
        for item, price in items_dict.items():
            print(f"{item}: ₹{price}")

# Variable to keep track of the total order amount
order_total = 0

# Take the first order from the customer
item1 = input("Hey! What would you like to order: ")
found = False
for category, items in menu.items():
    for subcategory, items_dict in items.items():
        if item1 in items_dict:
            order_total += items_dict[item1]
            print(f"Your item {item1} added to your order! Current total: ₹{order_total}")
            found = True
            break
    if found:
        break

if not found:
    print(f"Sorry, the ordered item {item1} is not available on the menu yet!")

# Ask if the customer wants to order more items
another_order1 = input("Would you like to order anything else? (Yes/No) ")

# Take the second order if the customer wants more
if another_order1 == "Yes":
    item2 = input("Please enter the food item you would like to order: ")
    found = False
    for category, items in menu.items():
        for subcategory, items_dict in items.items():
            if item2 in items_dict:
                order_total += items_dict[item2]
                print(f"Your item {item2} added to your order! Current total: ₹{order_total}")
                found = True
                break
        if found:
            break

    if not found:
        print(f"Sorry, the ordered item {item2} is not available on the menu yet!")

# Finalize the order and display the total amount
print(f"Thank you for your order! Your final total is: ₹{order_total}.")


# Initialize payment methods
payment_method = ("Which payment method would you like to use? (credit/debit cards, mobile UPI payments, and cash.)")
if payment_method == "credit/debit cards":
    print("Please swipe or insert your card to complete the payment.")
elif payment_method == "mobile UPI payments":
    print("Please scan the QR code to complete the payment via UPI.")
elif payment_method == "cash":
    print("Please hand over the cash to the cashier to complete the payment. Don't forget to collect your change if any!")

# Ask for dine-in or take away
dine_option = input("Would you like to dine in or take away? (Dine In/Take Away) ")
if dine_option == "Dine In":
    print("Great! Please proceed to your table and we will bring your order to you shortly.")
elif dine_option == "Take Away":
    print("No problem! We will prepare your order for take away.Wait for the name to be called.Till then, relax and enjoy the ambiance of our café.")


# Give a closing message and warm goodbye
print("Thank you for choosing CodeCaffeine! We hope to see you again soon. Have a wonderful day!")