#######Power Of A Number


def power(x,n):
    if n == 0:
        return 1
    smallOutput = power(x,n-1)
    return x * smallOutput

x,n = map(int,input().split())
print(power(x,n))

