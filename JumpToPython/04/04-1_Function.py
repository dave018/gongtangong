def add(a,b):
    print("a : {0}, b : {1}".format(a,b))
    return a+b

print(add(3,5))
print(add(b=5,a=3)) # a=3, b=5, return 3+5

# many arguments
def add_many(*args):
    result = 0
    for i in args:
        result += i
    print(type(args)) #args is tuple
    return result

print(add_many(1,2,3))

# make dic with arguments = keyword arguments
def print_kwargs(**args):
    print(args)
    print(type(args))
    print(args.keys())
print_kwargs(a=1, b="apple") #{'a': 1, 'b': 'apple'}

# multiple return using tuple
# default argument value
def add_and_mul(a,b=5):
    return a+b, a*b
result_add, result_mul = add_and_mul(3,5)
print("{0}, {1}".format(result_add, result_mul))

result_add, result_mul = add_and_mul(3)
print("{0}, {1}".format(result_add, result_mul))

# keyword global
global_int = 1
def global_add_foo():
    global global_int
    global_int += 1
print(global_int)
global_add_foo()
print(global_int)

#lambda
#lambda doesn't need return. but there is return value. But only 1 line
add = lambda a, b: a+b
print(add(3,4))