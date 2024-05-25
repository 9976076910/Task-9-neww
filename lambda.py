arr_list = [10, 501, 22, 37,100,999,87,351] # declaring the list elements
element = 351
#assigning the variable
a = lambda arr_list, element: True if element in arr_list else False
if (a(arr_list, element)):
    print("Element is Present in the list",type(element)) #print the type of the element
else:
    print("Element is Not Present in the list")