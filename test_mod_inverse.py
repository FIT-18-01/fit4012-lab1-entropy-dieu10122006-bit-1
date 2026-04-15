import sys

def gcd(a, b):
    """Calculate GCD using Euclidean algorithm"""
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def extended_euclid(a, b):
    """Extended Euclidean algorithm - returns (gcd, x, y) where ax + by = gcd"""
    if b == 0:
        return a, 1, 0
    
    g, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return g, x, y

def mod_inverse(a, m):
    """Find modular inverse of a modulo m using extended Euclidean algorithm"""
    g, x, y = extended_euclid(a, m)
    
    if g != 1:
        return -1  # Inverse does not exist
    
    return (x % m + m) % m  # Ensure positive result

# Test cases
test_cases = [
    (3, 7),
    (10, 17),
    (6, 9),
]

print("=" * 70)
print("MODULAR INVERSE TEST RESULTS")
print("=" * 70)

for a, m in test_cases:
    g = gcd(a, m)
    print(f"\nInput: a={a}, m={m}")
    print(f"  gcd({a}, {m}) = {g}", end="")
    
    if g != 1:
        print(" -> Inverse does not exist")
        result = -1
    else:
        inv = mod_inverse(a, m)
        verification = (a * inv) % m
        print(f" -> Inverse exists")
        print(f"  Modular inverse: {inv}")
        print(f"  Verification: {a} * {inv} mod {m} = {verification}")
        result = inv

print("\n" + "=" * 70)

# Output results in table format
print("\n| a | m | Expected | Program Result | Status |")
print("|---:|---:|---|---|---|")

expected = [5, 12, -1]
for i, (a, m) in enumerate(test_cases):
    inv = mod_inverse(a, m)
    status = "✓ PASS" if inv == expected[i] else "✗ FAIL"
    expected_str = str(expected[i]) if expected[i] != -1 else "Not exist"
    result_str = str(inv) if inv != -1 else "Not exist"
    print(f"| {a} | {m} | {expected_str} | {result_str} | {status} |")
