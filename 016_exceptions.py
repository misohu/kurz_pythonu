# Video https://youtu.be/0YrtiuSQxuQ
# Vynimky vieme zachytit v bloku try catch
# x = 2/0 

try:
    x = 2/0
except ZeroDivisionError as e:
    print("Nastalo delenie nulou")

# Vynimky bez try except prerusuju beh programu 
# print("Toto sa vypise")
# x = 2/0
# print("Totot sa uz nevypise")

try:
    print("Toto sa vypise")
    x = 2/0
except ZeroDivisionError as e:
    print("Nastalo delenie nulou. a program pokracuje dalej")
print("Totot sa uz vypise lebo tam bol try except")

# Zachytit vieme akukolvek vynimku nemusime ju vzdy definovat aj ked je dobrym zvykom zachytavat presnu vynimku
arr = [1,2,3]
try:
    arrr[102] # index neexistuje 
except Exception: # vsimni si ze som nepridal as e 
    print("nastala vynimka")


# As e v sebe drzi nieco co sa vola objekt vyniky. Ak zachytavam kazdu vynimku viem potom zistit o aku vynimku slo
arr = [1,2,3]
try:
    arrr[102] # index neexistuje 
except Exception as e: # vsimni si ze som nepridal as e 
    print("Nastala vynimka:")
    print(e)


# Zachytit vieme aj viac vynimiek naraz ked specifikujeme typy vynimiek
def division(number1, number2):
    try:
        result = number1/number2
    except ZeroDivisionError:
        print("Nastalo delenie nulou vraciam vysledok 0")
        result = 0
    except TypeError:
        print("Prosim do funkcie posielajte len cisla vraciam vysledok 0")
        result = 0
    return result

print(division(2, 0))
print(division("Ahoj", "Miso"))
print(division(10, 5))