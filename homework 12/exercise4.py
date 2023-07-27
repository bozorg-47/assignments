# num = int(input("enter a number"))
# mod = num %2
# if mod > 0:
#     print("this is an odd number")
# else:
#     print("this is an even number")
  


# def is_even(num):
#     mod = num %2
#     if mod > 0:
#         print("this is an odd number")
#     else:
#         print("this is an even number")
# is_even(10)


def is_even(a):
 
    if a %2 == 0:
        return True
    else:
        return False

print(is_even(10))