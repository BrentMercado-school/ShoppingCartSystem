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

customer = []

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

    elif choice == '2':
        print("\n------ AVAILABLE PRODUCTS ------")
        for product in products:
            print(f"{product['name']} - ₱{product['price']} (Stock: {product['quantity']})")
        print("--------------------------------")
        name = input("Enter product name: ")
        for product in products:
            if product['name'] == name:
                quantity = int(input("Enter quantity: "))
                product['quantity'] -= quantity
                price = product['price'] * quantity
                customer.append({'name': name, 'price': price, 'quantity': quantity})
                print(f"{quantity} {product['name']} added to your cart!")
                input("Press any key to continue...")
                print("\n")

    elif choice == '4':
        print("\n------ YOUR SHOPPING CART ------")
        if len(customer) == 0:
            print("You don't have anything in your cart")
            input("Press any key to continue...")
            print("\n")
        else:
            total_price = 0
            for product in customer:
                print(f"{product['name']} x{product['quantity']} = ₱{product['price']}")
                total_price += product['price']
            print("--------------------------------")
            print(f"Total: ₱{total_price}")
            print("--------------------------------")
            input("Press any key to continue...")
            print("\n")