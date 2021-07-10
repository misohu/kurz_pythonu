visitor={
    "name": "Michal",
    "age": 13
}

def play_movie(visitor):
    print(f"I am playing movie for {visitor['name']}")

# What is we want to play movie only for adults
if visitor['age'] >= 18:
    play_movie(visitor)

# Decorator
def play_movie():
    print(f"I am playing movie")

def adult_function(func):
    def make_adult_function():
        if visitor['age'] >= 18:
            return func()
        else:
            print("Grow up!!!")
    return make_adult_function

play_movie=adult_function(play_movie)
play_movie()

# Decorator @
@adult_function
def show_image():
    print("Showing image")

show_image()


# Decorators with arguments
# niekedy chceme aby nasa funcktia mala viacero argumentov 
import datetime
import time

def log_duration(func):
    def wrapper(x):
        print(datetime.datetime.now())
        func(x)
        print(datetime.datetime.now())
    return wrapper

@log_duration
def sleeper(seconds):
    time.sleep(seconds)

# sleeper(5)

# Co ak chcem viacero argumentov
def log_duration(func):
    def wrapper(*args):
        print(datetime.datetime.now())
        func(*args)
        print(datetime.datetime.now())
    return wrapper

@log_duration
def sleeper(seconds, name):
    time.sleep(seconds)
    print(f"Hi, my name is {name}")

# sleeper(5, "Michal")


# Co ak chceme nieco vratit
def log_duration(func):
    def wrapper(*args):
        print(datetime.datetime.now())
        return_value = func(*args)
        print(datetime.datetime.now())
        return return_value
    return wrapper

@log_duration
def sleeper(seconds, name):
    time.sleep(seconds)
    print(f"Hi, my name is {name}")
    return name

# print(sleeper(5, "Michal"))


# Introspection TOTO JE BONUS NAD RAMEC VIDEA
# Kazda funkcia si so sebou nesie meno a po dekorovani sa meni meno funkce 
def hello_world():
    print("Hello world")

print(hello_world.__name__)

@log_duration
def hello_world():
    print("Hello world")

print(hello_world.__name__)

# Takto to vieme opravit
import functools

def log_date(func):
    @functools.wraps(func)
    def wrapper(*args):
        print(datetime.datetime.now)
        return_value=func(*args)
        print(datetime.datetime.now)
        return return_value
    return wrapper

@log_date
def hello_world():
    print("Hello world")

print(hello_world.__name__)

# Domaca uloha spravte dekorator ktory zopakuje volanie funkcie 3 krat
# DOMACA EXTRA spravte decorator ktory zavola dekorovanu funkciu n krat kde n je lubovolne cele kladne cislo 

