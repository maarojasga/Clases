import numpy as np
from sympy import symbols, Eq, solve, Matrix

mod = 26

a, b, c = symbols('a b c')
row2 = [-2, 1, 0]
row3 = [-1, -1, 1]

P = Matrix([19, 17, 0])  # "TRA"
C = Matrix([19, 6, 17])  # "TGR"

row1 = [a, b, c]
key = Matrix([row1, row2, row3])

result = key * P % mod

eqs = [
    Eq(result[0], C[0]),
    Eq(result[1], C[1]),
    Eq(result[2], C[2])
]

solutions = solve(eqs, (a, b, c), dict=True)

valid_keys = []
for sol in solutions:
    test_key = Matrix([
        [sol[a], sol[b], sol[c]],
        row2,
        row3
    ])
    if test_key.det() % mod == 1:
        valid_keys.append((test_key, sol))

for key, vals in valid_keys:
    print("Matriz clave encontrada:")
    print(np.array(key).astype(int))
    print("Valores: ", vals)

    inv_key = key.inv_mod(26)
    print("Matriz inversa:")
    print(np.array(inv_key).astype(int))

    encrypted = "tgrbzioyrnbtqozplx"
    blocks = [encrypted[i:i+3] for i in range(0, len(encrypted), 3)]

    def to_num(c): return ord(c.upper()) - ord('A')
    def to_char(n): return chr(n % 26 + ord('A'))

    decrypted = ""
    for block in blocks:
        nums = Matrix([to_num(c) for c in block])
        dec = inv_key * nums % 26
        decrypted += ''.join(to_char(n) for n in dec)

    print("Mensaje desencriptado:", decrypted)
    print("-" * 40)
