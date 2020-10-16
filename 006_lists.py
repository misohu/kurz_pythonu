# Video https://youtu.be/rEhB9esEu3U
# List vieme definovat nasledovne
number_list=[0,1,2,3,4,5,6,7]
type(number_list)

# Vieme don vkladat akekolvek datove typy
string_list=["Michal", "Felipe", "John"]
combined_list=[1,"Michal", "John", True, 1.5]

# Index listu je taky isty ako list index stringu
print(number_list[0])
print(number_list[2:4]) # [2;3>
print(number_list[0:3])
print(number_list[-1])
print(number_list[-2:])

# Listy vieme scitavat
print(number_list + [8, 9, 10])

# Listyu na rozdiel od stringov vieme pomocou indexu upravovat. Posledny prikaz vrati chybu
best_teacher="Michal Hucko"
numbers=[0,1,2,3,4,5]
numbers[0]=10
print(numbers)
best_teacher[0]="N"

# Upravovat vieme aj pomocou zlozeneho indexu
numbers[1:3] # is <1;3)
numbers[1:3] = [11, 12]
print(numbers)
numbers[1:3] = [11, 12 ,13]
print(numbers)
numbers[1:3] = []
print(numbers)

# Na nascitanie novych prvkov musime vysledok operacie scitania priradit do premennej inac sa povodna premenna nezmeni 
numbers=[0,1,2,3,4,5]
numbers + [1, 2]
print(numbers)
numbers_new=numbers + [1, 2]
print(numbers_new)

# Syntactic suggar
numbers+=[1, 2] # the same as numbers=numbers + [1, 2]
print(numbers)
number_of_rooms=0 
number_of_rooms += 1 # the same syntax can be applied to numbers
print(number_of_rooms)

# Pomocou funkcie len vieme zistit dlzku pola ale aj stringu
numbers=[0,1,2,3,4,5]
len(numbers)
len("Michal")

# Funkcia append prida na koniec pola prvok v zatvorke.
numbers=[0,1,2,3,4,5]
numbers.append(10)
print(numbers)
numbers.append([7, 8])
print(numbers)

# Funkcia remove vymaze prvok na indexe v zatvorke
numbers=[0,1,2,3,4,5,0]
numbers.remove(0)
print(numbers)

# Prvkami pola mozu byt aj ine polia
numbers_and_lists=[0, 1, 2, 3, 4, 5, 0, [1, 2], [3, 4, [5]]]
print(numbers_and_lists[-1])
print(numbers_and_lists[-1][0])

# Funkcia count vrati pocet vyskytu prvku v zatvorke
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.count('c') 

# Funkcia extend rozbali pole a prida ho na koniec 
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.extend([1, 2]) 

# Funkcia index vrati poziciu prvehjo vyskytu prvku v zatvorke
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.index('i')

# Funkcia insert vlozi druhy prvok v zatvorke na poziciu (prvy prvok v zatvorke)
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.insert(3, "x") # add elemet to position
print(letters)

# Funkcia remove vymaze prvy vyskyt znaku v zatvorke
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.remove("c") 
print(letters)

# Funkcia otoci pole
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.reverse()
print(letters)

# Funkcia pop vrati posledny prvok z pola a zaroven ho z neho zmaze
nums=[1,2,3]
nums.pop()
print(nums)

# Funkcia clear zmaze cely obsah pola
letters = ['m', 'i', 'c', 'h', 'a', 'l', 'h', 'u', 'c', 'k', 'o']
letters.clear() 
print(letters)

# Funkcia sort usporiada pole
numbers=[8,4,5,1,2,7,8,9,0]
numbers.sort()
print(numbers)