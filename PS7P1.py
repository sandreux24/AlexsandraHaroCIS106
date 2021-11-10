def comptotal(quantity, price):
    total = quantity * price
    if total > 10000:
        total = total * 0.9
    
    return total

# Main
print("Enter quantity")
quantity = float(input())
print("Enter price per unit")
price = float(input())
comptotal(quantity, price)
total = comptotal(quantity, price)
print(total)
