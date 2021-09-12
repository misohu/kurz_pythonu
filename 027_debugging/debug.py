from custom_sum import custom_sum

def mistery_function(x, y):
    sum = 0 
    for i in range(x, y+1):
        breakpoint()
        sum = custom_sum(sum, i)
        print("Michal Hucko") 
    return sum


x = 2
y = 10

breakpoint()
print(mistery_function(x, y))
