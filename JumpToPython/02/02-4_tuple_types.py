#tuple is similar with list. But tuple can't add/del/modify element
list_a = [1]
#tuple_a = (1) # this is not tuple. this is integer 1.
tuple_a = (1,)
print(list_a)
print(tuple_a)

tuple_b = (1, 2, 3)
#del tuple_b[0] # TypeError
#tuple[0] = 100 #TypeError

tuple_c = 1,2,3 #tuple can skip ()
print(tuple_c)