print(f"{'Ordenação de valores':^30}")
list_one = list()
for c in range(1, 6):
    while True:
        try:
            list_one.append(int(input(f"Informe o {c}º número: ")))
        except ValueError or TypeError:
            print('Somente números, e tem que ser inteiro tambem')
        else:
            break
list_two = list()
c1 = c2 = 0

for c1 in range(len(list_one)):
    if c1 == 0 or list_one[c1] > list_two[-1]:
        list_two.append(list_one[c1])
        continue
    for c2 in range(len(list_two)):
        if list_one[c1] <= list_two[c2]:
            list_two.insert(c2, list_one[c1])
            break

print(f"\nDados inseridos -> {list_one}\nPrimeira lista com o a função Sorted -> {sorted(list_one)}\self"
      f"Segunda lista utilizando meu algoritmo -> {list_two}")
