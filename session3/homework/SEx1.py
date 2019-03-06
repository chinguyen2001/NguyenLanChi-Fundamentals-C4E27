print("Welcome to our store, what do you want?")
print("Pick one of the following options [C, R, U, D] to procede.")
print("C: Enter new items")
print("R: View current item list")
print("U: Update item list")
print("D: Delete current items")

n = str(input("Please enter your choice: "))

item_list = ['T-Shirt', 'Sweater']
choices = ['C', 'R', 'U', 'D']

while n not in choices:
    print("Please choose C, R, U, or D to procede.")
    n = str(input())

if n == 'C':
    print("Enter new items: ")
    c = str(input())
    item_list.append(c)
    print("Your item has been added. The current item list is: ", end="")
    print(item_list)

elif n == 'R':
    print("The current item list is: ",end="")
    print(item_list)

elif n == 'U':
    print("What is the update position? ",end="")
    posi = int(input()) - 1
    item_list.pop(posi)
    print("What is the new item? ",end="")
    new_item = str(input())
    item_list.insert(posi,new_item)
    print("Your list has been updated. The current item list is: ", end="")
    print(item_list)

else:
    print("What is the deleted position? ",end="")
    del_posi = int(input()) - 1
    item_list.pop(del_posi)
    print("Your list has been updated. The current item list is: ",end="")
    print(item_list)
