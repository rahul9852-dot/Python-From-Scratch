# python code to demonstrate 
# checking of element existence
# using loops and in

# Initializing list

test_list=[1,6,3,5,3,4]
print("Checking if 4 exists in list (using loop) :")

# checking if 4 exists in list
# using loop
for i in test_list:
    if i==4:
        print("Element Exists.")
print("checking if 4 exists in list (using in):")


# Another approach for checking
if (4 in test_list):
    print("Element Exists")
    