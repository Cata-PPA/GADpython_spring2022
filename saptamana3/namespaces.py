# def my_function():
#     global msg
#     msg = "Hello"
#     print(msg)
#     return None
#
# print(dir(my_function()))
# # print(my_function())
# print(msg)

def my_function():
    def my_second_function():
        global msg
        msg = "hello"
        return None

    my_second_function()
    print(locals(), 'locale la nivel de my second function')
    msg = "Hello1"
    print(f"functia principala {msg}")
    return None

def functie2():
    print(msg, '>>>')
    return None

my_function()
print(msg)
print(globals())
print(locals())