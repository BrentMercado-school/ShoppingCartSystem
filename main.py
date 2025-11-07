products = [
    {
        'name': 'Apple',
        'price': 20.00,
        'quantity': 50
    },
    {
        'name': 'Banana',
        'price': 15.00,
        'quantity': 40
    },
    {
        'name': 'Milk',
        'price': 50.00,
        'quantity': 30
    },
    {
        'name': 'Bread',
        'price': 35.00,
        'quantity': 20
    }
]

while True:
    print("==============================")
    print("\tWELCOME TO PYTHON MART")
    print("==============================")
    print("1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart"
          "\n5. Checkout\n6. Exit")
    print("------------------------------")
    choice = input("Enter your choice: ")

    if choice == '1':
        print("\n------ AVAILABLE PRODUCTS ------")
        for product in products:
            print(f"{product['name']} - ₱{product['price']} (Stock: {product['quantity']})")
        print("--------------------------------")
        input("Press any key to continue...")
        print("\n")