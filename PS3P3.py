print("Enter number of books: ")
numberofbooks = float(input())
print("Enter Cost per book: ")
costperbook = float(input())
total = numberofbooks * costperbook
print("Amount due: $" + str(total))
if total > 50:
    print("Free shipping charge")
    print("Total amount due: $" + str(total))
else:
    print("shipping charge will be $25")
    totalwithshipping = total + 25.0
    print("Total amount due: $" + str(totalwithshipping))
