import numpy as np

def willans_prime(n):
    """
    Calcularemos el número primo n-ésimo usando la fórmula de Willan
   
    
    Parámetros:
    n (int): El índice del número primo que es buscado.
    
    Out:
    int: El número primo n-ésimo
    """
    if n < 1:
        raise ValueError("n debe ser entero positivo")
    
    # Willan's formula for the nth prime
    def inner_sum(i):
        """Se calcula la suma sobre j usando el teorema de Wilson para evitar los errores en el factorial dentro del coseno (error computacional por número muy grande)"""
        total = 0
        for j in range(1, i+1):
            if j == 1:
                total += 1  # Caso especial para j=1
            else:
                # Teo. de Wilson: j es primo si (j-1)! ≡ -1 mod j
                # Se usará la aritmética modular para evitar calcular enteros gigantes bajo factorial
                fact_mod = 1
                for k in range(2, j):
                    fact_mod = (fact_mod * k) % j
                
                # Teorema de Wilson: si (j-1)! ≡ -1 mod j, entonce j es primo
                if (fact_mod + 1) % j == 0:
                    total += 1
        return total
    
    # Se hace el cálculo de la sumatoria de fuera usando el resultado de la de dentro usando el teorema de Wilson.
    result = 1
    max_i = min(int(2**n), 1000)  # Límite para los enteros (evita romper la cpu)
    
    for i in range(1, max_i + 1):
        denominator = inner_sum(i)
        if denominator == 0:
            continue  # Evita división por cero
                
        # Calculamos el término para cada i
        term = n / denominator
        term = term ** (1/n)  # nth raíz
        term = np.floor(term)
        result += term
        
    return int(result)

# Usamos la función
if __name__ == "__main__":
    print("Willan's Formula Prime Number Calculation")
    print("=========================================")
    
    # Calculamos los primos hasta el n deseado
    for n in range(1, 50):
        prime = willans_prime(n)
        print(f"The {n}th prime number is: {prime}")
    
