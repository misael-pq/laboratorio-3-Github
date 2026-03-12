
# Usando la Criba de Eratostenes
def criba_eratostenes(limite):
    if limite < 2:
        return []

    es_primo = [True] * (limite + 1)
    es_primo[0] = es_primo[1] = False
    
    for i in range(2, int(limite ** 0.5) + 1):
        if es_primo[i]:
            # Marcar todos los múltiplos de i como no primos
            for j in range(i * i, limite + 1, i):
                es_primo[j] = False
    
    return es_primo

x = int(input())
casos = []
max_valor = 0

# Leer todos los casos y encuentra el valor máximo
for v in range(x):
    n, m = map(int, input().split())
    casos.append((n, m))
    max_valor = max(max_valor, m)

primos = criba_eratostenes(max_valor)

# Cuenta primos
for n, m in casos:
    cont = 0
    for i in range(n, m + 1):
        if i >= 2 and primos[i]:
            cont += 1  
    print(cont)
