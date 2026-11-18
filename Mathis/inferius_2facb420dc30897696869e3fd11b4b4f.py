#!/usr/bin/env python3

from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes, GCD
# import primefac

e = 65537

# if __name__ == "__main__":
#     n = 984994081290620368062168960884976209711107645166770780785733
#     factors = list(primefac.primefac(n))
#     print(factors)

# n will be 8 * (100 + 100) = 1600 bits strong (I think?) which is pretty good
p = 848445505077945374527983649411
q = 1160939713152385063689030212503
phi = (p - 1) * (q - 1)
d = inverse(e, phi)
n = 984994081290620368062168960884976209711107645166770780785733 
print(f"{n == p * q}\n")


# FLAG = b"crypto{???????????????}"
# pt = bytes_to_long(FLAG)

ct = 948553474947320504624302879933619818331484350431616834086273


print(f"n = {n}\n")
print(f"e = {e}\n")
print(f"ct = {ct}\n")

pt = pow(ct, d, n)
decrypted = long_to_bytes(pt)
print(f"decrypted = {decrypted}\n")

