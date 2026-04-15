import math
from collections import Counter

def calculate_entropy(text):
    """Calculate Shannon entropy of a string"""
    if not text:
        return 0.0
    
    freq = Counter(text)
    entropy = 0.0
    for count in freq.values():
        p = count / len(text)
        entropy -= p * math.log2(p)
    return entropy

def calculate_redundancy(text, alphabet_size=256):
    """Calculate redundancy = log2(N) - H(X)"""
    max_entropy = math.log2(alphabet_size)
    entropy = calculate_entropy(text)
    return max_entropy - entropy

# Test cases for entropy/redundancy
test_inputs = ["aaaa", "abcd", "hello world"]

print("=" * 60)
print("ENTROPY AND REDUNDANCY TEST RESULTS")
print("=" * 60)

results = []
for text in test_inputs:
    entropy = calculate_entropy(text)
    redundancy = calculate_redundancy(text)
    results.append((text, entropy, redundancy))
    print(f"\nInput: '{text}'")
    print(f"  Entropy: {entropy:.6f}")
    print(f"  Redundancy: {redundancy:.6f}")

print("\n" + "=" * 60)

# Output results in table format
print("\n| Input | Entropy | Redundancy | Note |")
print("|---|---:|---:|---|")
for text, entropy, redundancy in results:
    note = "Low entropy, high redundancy" if entropy < 2 else "Higher entropy, lower redundancy"
    print(f"| {text} | {entropy:.4f} | {redundancy:.4f} | {note} |")
