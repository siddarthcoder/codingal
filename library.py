book_names = ["diary of a wimpy kid", "bob's dog", "legoo ", "rubicks cube"]
copy_counts = [3, 0, 5, 2]
current_late_fees = [63, 73, 542, 3]

# 2. Combine values using zip() to pair books with their available copies
library_inventory = list(zip(book_names, copy_counts))
print("Library Inventory:", library_inventory)

# 3. Filter available books (books with a copy count greater than 0)
available_books = list(filter(lambda item: item[1] > 0, library_inventory))
print("Available Books:", available_books)

# 4. Update late fees by adding a flat surcharge (e.g., $0.50) using map()
fee_surcharge = 0.50
updated_late_fees = list(map(lambda fee: fee + fee_surcharge, current_late_fees))
print("Updated Late Fees:", updated_late_fees)

# 5. Stop the program early when a chosen book is unavailable
chosen_book = "bob's dog"

print(f"\nChecking availability for: '{chosen_book}'...")
for name, count in library_inventory:
    if name == chosen_book and count == 0:
        print(f"Error: '{chosen_book}' is out of stock! stopping the program early.")
        break
else:
    print(f"success: '{chosen_book}' is available for checkout.")