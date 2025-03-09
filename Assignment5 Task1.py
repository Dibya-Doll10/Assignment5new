student = {
    "Alice": "50",
    "John" : "60",
    "Babe" : "70",
    "Sampson" : "80",
    "Harry" : "85"
}
temp = str(input("Enter the required student's name: "))
smarks = student.get("Alice")
if temp=="Alice":
     print("Alice's marks is ",smarks)
elif temp== "John":
    print("John's marks is: ", student.get("John"))

elif temp == "Babe":
    print("Babe's marks is: ", student.get("Babe"))

elif temp == "Sampson":
    print("Sampson's marks is: ", student.get("Sampson"))

elif temp == "Harry":
    print("Harry's marks is: ", student.get("Harry"))

else:
    print("Name not found")
