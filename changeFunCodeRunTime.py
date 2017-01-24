"""
     This code defines a function and changes its code runtime
"""
def f():
    y = "vasim"
    print "My name is " + str(y)

f()


# change function code dynamically
new_code_text = """
y = "Vasim Kachhi"
print "My Full name is " + str(y)
"""
f.func_code = compile(new_code_text, __name__, 'exec')
f()

# change function code dynamically
new_code_text = """
y = "Vasim Ahamed Kachhi"
print "My Full name is " + str(y)

"""
f.func_code = compile(new_code_text, '<string>', 'exec')
f()

print f.func_code
c = f.func_code
print c.co_consts
print f.func_code.co_varnames
print f.func_code.co_argcount


def test(a, b):
    """
        Description:
            Test function
        Parameters:
            a: number to be added
            b: number to be added
        return:
            number addition of parameters passed
        @type a: int
        @param a: An number
        @type b: int
        @param b: An number
        @return:  a + b
    """
    print a, b
    return a + b

print test(4, 4)
print test.func_doc



