import csv
import sys

def xgcd(a,b):
    if b == 0:
        return [1,0,a]
    else:
        x,y,d = xgcd(b, a%b)
        return [y, x - (a//b)*y, d]

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

#c2 would be a and Modulus N would be m
def modInverse(a, m):
    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def convert_hex_to_ascii(h):
    chars_in_reverse = []
    while h != 0x0:
        chars_in_reverse.append(chr(h & 0xFF))
        h = h >> 8

    chars_in_reverse.reverse()
    return ''.join(chars_in_reverse)

def main():
    with open('crackme.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    c1=int(data[0][1],16)
    c2=int(data[1][1],16)
    e1=int(data[2][1],16)
    e2=int(data[3][1],16)
    N=int(data[4][1],16)
    euclidConstants=xgcd(e1,e2)
    a=euclidConstants[0]	
    b=euclidConstants[1]

    eq1=modInverse(c2,N)
    #(c1^a * eq1^-b) mod N
    result1=pow(eq1,-b,N)
    result2=pow(c1,a,N)

    result3=result1*result2
    finalresult=result3%N
    print(hex(finalresult))
    #print(convert_hex_to_ascii(finalresult))
if __name__ == "__main__":
    main()