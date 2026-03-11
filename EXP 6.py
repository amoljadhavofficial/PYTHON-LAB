def apply_discount(amount, discount_rate):
    amount = amount - (amount * discount_rate)
    print("Discounted amount inside function:", amount)

def add_customer_segment(customer_data, segment):
    customer_data.append(segment)
    print("Customer data inside function:", customer_data)

def classify_customer(amount, high_value=5000):
    if amount >= high_value:
        return "High Value Customer"
    else:
        return "Regular Customer"

def safe_update(customer_data):
    new_data = customer_data.copy()
    new_data.append("Analyzed")
    return new_data

customer_profile = []

while True:
    print("\n-----Menu: Customer Purchase Analysis Case Study----")
    print("1. Apply Discount (Example: Immutable)")
    print("2. Add Customer Segment (Example: Mutable)")
    print("3. Classify Customer (Keyword Arguments)")
    print("4. Safe Data Update (Prevent Modification)")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        purchase_amount = float(input("Enter purchase amount: "))
        discount = float(input("Enter discount rate (e.g. 0.10 for 10%): "))
        apply_discount(purchase_amount, discount)
        print("Purchase amount outside function:", purchase_amount)

    elif choice == 2:
        customer_id = input("Enter Customer ID: ")
        purchase_amount = float(input("Enter purchase amount: "))
        customer_profile = [customer_id, purchase_amount]
        segment = input("Enter customer segment (Premium/Regular): ")
        add_customer_segment(customer_profile, segment)
        print("Customer data outside function:", customer_profile)

    elif choice == 3:
        amount = float(input("Enter purchase amount: "))
        limit = float(input("Enter high value limit: "))
        category = classify_customer(amount=amount, high_value=limit)
        print("Customer Category:", category)

    elif choice == 4:
        if not customer_profile:
            print("No customer data available. Please add customer first.")
        else:
            updated_data = safe_update(customer_profile)
            print("Original Data:", customer_profile)
            print("Updated Data:", updated_data)

    elif choice == 5:
        print("Exiting Program... Thank You!")
        break

    else:
        print("Invalid choice! Please try again.")

