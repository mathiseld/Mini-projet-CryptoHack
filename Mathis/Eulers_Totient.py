from sympy import isprime
from sympy.functions.combinatorial.numbers import totient

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
N = p * q

print("N est premier :", isprime(N)) 
# phi_de_N = N-1 si N est premier
phi_de_N = (p - 1) * (q - 1)
print("phi(N) :", phi_de_N)