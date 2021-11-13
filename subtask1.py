n = input("Input a number ")
n = int(n) 
q = 0
while (n >= q*q):
    q = q + 1
q = q - 1

print('The largest square number smaller than the one given is:', q*q)
