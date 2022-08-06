# Kontrolovanie zatvoriek
Na vstupe máme string pozozstávajúci len z ľavých a pravých zátvoriek (,{,[,],},). String pozostáva z 0 až n takýchto znakov. Napíšte program, ktorý rozpozná či daný string spĺňa nasledujúce podmienky:
- Každá otvorená zátvorka je uzavretá svojou opačnou verziou
- Otvorené zátvorky sú uzavreté v správnom poradí

### Priklad
```{python}
s = is_valid("") # True
s = is_valid("()") # True
s = is_valid("[") # False
s = is_valid("[)") # False
s = is_valid("([][]{()})") # True
s = is_valid("({([()()])}))") # False
s = is_valid("({([()()])})") # True
