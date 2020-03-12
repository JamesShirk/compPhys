import time

# Main PRNG
def psuedoRanXOR(seed, m1, p, q, n, upperLimit, m2 = None):
    # Allows for the use of two m values (mod value for the Fibbonacci generator)
    m2 = m1 if not isinstance(m2, int) else m2
    # Generates the intial random data using the simple Fibbonacci generator
    nInitial = p + 1 if p > q else q + 1
    initial = psuedoRanSum(seed, m1, nInitial, p, q)
    # Appends values to the end of the list equal to (Xp XOR Xq mod m2)
    for _ in range(0, n):
        initial.append((initial[len(initial) - p] ^ initial[len(initial) - q]) % m2)
    # generates even distribution by modding the output by some upperlimit
    output = [i % upperLimit for i in initial]
    # Returns only the XOR generated values
    return(output[nInitial:n + nInitial])

# Generates Fibbonacci values using a seed as x0 and seed mod p as x1 then just x2 = x1 + x0 mod m
def psuedoRanSum(seed, m, n, p, q):
    x0 = seed
    x1 =  seed % p if seed % 2 == 0 else seed % q
    x2 = 0
    values = []
    for _ in range(0, n):
        x2 = (x1 + x0) % m
        x1 = x2
        x0 = x1
        values.append(x2)
    return values

def rand_sample(x):
    randy = psuedoRanXOR(round(time.time()), (2**32) - 1, 250, 103, 1000, x)
    return randy[-1]

if __name__ == "__main__":
    for i in range(100):
        print(rand_sample(5))