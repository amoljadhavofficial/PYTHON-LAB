dataset_schema = ("CustomerID", "Name", "PurchaseAmount", "Segment")

purchase_amounts = []

unique_customers = set()

customer_records = {}

while True:
    print("\n----Menu Customer Analytics------")
    print("1. Add Customer Data")
    print("2. View Purchase Amounts (List)")
    print("3. View Dataset Schema (Tuple)")
    print("4. View Unique Customers (Set)")
    print("5. View Customer Records (Dictionary)")
    print("6. Remove Duplicate Purchases using Set")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cid = input("Enter Customer ID: ")
        name = input("Enter Customer Name: ")
        amount = float(input("Enter Purchase Amount: "))

        purchase_amounts.append(amount)
        unique_customers.add(cid)

        if amount >= 5000:
            segment = "Premium"
        elif amount >= 2000:
            segment = "Gold"
        else:
            segment = "Regular"

        customer_records[cid] = {
            "Name": name,
            "Purchase": amount,
            "Segment": segment
        }

        print("Customer data added successfully.")

    elif choice == 2:
        print("\nPurchase Amounts (List):", purchase_amounts)
        if purchase_amounts:
            print("Total Sales:", sum(purchase_amounts))
            print("Average Sales:", sum(purchase_amounts) / len(purchase_amounts))

    elif choice == 3:
        print("\nDataset Schema (Tuple - Immutable):")
        for field in dataset_schema:
            print(field)

    elif choice == 4:
        print("\nUnique Customers (Set):", unique_customers)
        print("Total Unique Customers:", len(unique_customers))

    elif choice == 5:
        print("\nCustomer Records (Dictionary):")
        for cid, details in customer_records.items():
            print(cid, "=>", details)

    elif choice == 6:
        unique_purchases = set(purchase_amounts)
        print("\nOriginal Purchase List:", purchase_amounts)
        print("After Removing Duplicates (Set):", unique_purchases)

    elif choice == 7:
        print("Exiting Customer Analytics System...")
        break

    else:
        print("Invalid choice! Please try again.")
