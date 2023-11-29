def gcd(a, b):
    if not b:
        return a
    r = a % b
    return gcd(b, r)

n, m = map(int, input().split())
print(int(n * m / gcd(n, m)))