# Sum of digits of a +ve integer number

def sumofDigits(n):
    assert n >= 0 and int(n) == n,'Give non -ve integer numbers only!'
    if n ==0:
        return 0
    else:
        return int(n%10) + sumofDigits(int(n/10))

print(sumofDigits(10))

# Calculating power of a number

def power(base,exp):
    assert exp >= 0 and int(exp) == exp ,'Give exp as non -ve integer number only!'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base,exp-1)

print(power(2,5))

# Finding GCD

def gcd(a,b):
    assert int(a) == a and int(b) == b,'Give a and b as integers only!'
    if a<0:
       a = -1*a
    if b<0:
       b = -1*b
    if b == 0:
       return a
    else:
       return gcd(b, a%b)
print(gcd(48,18))

# Converting decimal to binary number
def dec_to_bin(n):
    assert int(n)==n, 'The parameter must be an integer only!'
    if n ==0:
        return 0
    else:
        return n%2 + 10 * dec_to_bin(int(n/2))

print(dec_to_bin(13) )