import ast

def decrypt(key,n, ciphertext):
   print(hex(pow(ciphertext, key, n)))

f = open('./ptrace.trc')
c = open('./ptrace_input.txt')

data = f.read().split("\n")
cipher = c.read().split("\n")
print('point number:', len(data))



start_point = 0 # Point to start analysis
mid = 25 # sampling point interval
fence = 5 # high and low level dividing line


bin_array = []



for point_index in range(start_point, len(data), mid):
    if ast.literal_eval(data[point_index]) > fence:
    
        bin_array.append(1)

    else:

        bin_array.append(0)

bin_array2 = []
flag1=0
flag2=0
for x in bin_array:
    if x:
        flag1+=1
    else:
        if flag1 == 5:
            bin_array2.append(1)
        elif(flag1==3):
            bin_array2.append(0)
        flag1=0

d_bin = bin_array2
d = "".join(str(x) for x in d_bin)[::]

d_val = int(d,2)
n = int(cipher[1],16)
cip_val = int(cipher[0],16)
print(d_val)
print(decrypt(d_val,n,cip_val))