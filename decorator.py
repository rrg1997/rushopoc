'''#decorator-->it is a function that modifies the result of another func.
1.decorator modifies the result of another func.
2.decorator modifies the type of another func.

1.decorator takes a func as its parameter.
2.decorator contaibs anothetr function inside
3.decorator returns another func.'''

#a decorator that increment the result of another func by 10
def decor(func):
    def inner():
        res=func()
        return res+10

    return inner
@decor
def myfunc():
    return 100
x=myfunc()
print(x)

'''
x=decor(myfunc)
print(x())'''
