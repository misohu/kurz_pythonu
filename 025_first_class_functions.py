# Funkcie v Pythone sú takzvané funkcia prvej triedy 'First class functions'
def hello_world():
    print("helllo world")

print(type(hello_world)) # Aj funkcia je len objekt (pre tych co videli moj kurz OOP)

# To znamená že ich napríklad vieme priradiť do premenných
x=hello_world # vsimni si ze nepouzivam okruhle zatvorky to znamena ze nevolam funkciu
x()

# Ale aj poslat ako parameter funkcie
def function_wrapper(func):
    print("This is function wrapper")
    func()

function_wrapper(hello_world)

# Funkcia tiez vie vratit funkciu, ktora sa v nej vytvori
def function_factory():
    def hello_world():
        print("Hello world but different")
    return hello_world

print(function_factory)
print(function_factory())
print(function_factory()())

# Funkcie vies ulozit do pola presne ako akekolvek ine hodnoty
def adder(x, y):
    return x + y

def substractor(x, y):
    return x - y

def multiplier(x, y):
    return x * y

math_functions = [adder, substractor, multiplier]

for function in math_functions:
    print(function(1, 2))


# Annonymous function
def function_wrapper2(func, x, y):
    print("This is function wrapper")
    return func(x, y)

print(function_wrapper2(lambda x,y: x+y, 10, 20))
