from sympy import isprime

N = 882564595536224140639625987659416029426239230804614613279163
e = 65537
c = 77578995801157823671636298847186723593814843845525223303932
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

print(f"N = q * q : {N == p*q}\n")

print(f"N est premier : {isprime(N)}\n") 
# phi_de_N = N-1 si N est premier
phi_de_N = (p - 1) * (q - 1)
print(f"phi(N) : {phi_de_N}\n")

d = pow(65537, -1, phi_de_N)
print(f"d : {d}\n")

msg = pow(c, d, N)
print(f"Le message est : {msg}")