def f1():
    print('hello')

def f2(_func):
    _func()

def calc(_func):
    x = int(input('enter number: '))
    y = int(input('enter number: '))
    print(_func(x, y))


f2( f1 )
f2( lambda : print('hello') )
#calc( lambda x,y: x + y)
calc( lambda x,y: x * y)

# write a function which gets a list and a func as argument
# run on the list, for each item invoke the function and put the new value there
# you can use a function of power 2
#_list[i] = _func( _list[i] )