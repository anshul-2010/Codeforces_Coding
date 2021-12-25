'''
Petya loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits 4 and 7. For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.

Petya calls a number almost lucky if it could be evenly divided by some lucky number. Help him find out if the given number n is almost lucky.

Input
The single line contains an integer n (1 ≤ n ≤ 1000) — the number that needs to be checked.

Output
In the only line print "YES" (without the quotes), if number n is almost lucky. Otherwise, print "NO" (without the quotes).
'''
n=int(input())
fl=0
l=[str(i) for i in range(4,n+1) if n%i==0]
for j in range(len(l)):
    c1=l[j].count("4")
    c2=l[j].count("7")
    c=c1+c2
    if(c==len(l[j])):
        fl=1
if(fl==1):
    print("YES")
else:
    print("NO")
