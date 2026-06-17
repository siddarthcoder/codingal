bill_amount = float(input("Enter the total bill amount: "))
paid_amount = float(input("Enter the amount paid by the customer: "))

due_amount = bill_amount - paid_amount

if due_amount > 0:
    print(f"The customer still owes: {due_amount:.2f}")
elif due_amount < 0:
    print(f"Change to return to customer: {abs(due_amount):.2f}")
else:
    print("Bill paid in full. No balance due.")