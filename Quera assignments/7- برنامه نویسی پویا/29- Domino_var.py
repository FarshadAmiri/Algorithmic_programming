n = int(input())

# recursive
# def fibo(n):
#     if (n == 0) or (n == 1):
#         return 1
#     for i in range(2,n):
#         return fibo(n-1) + fibo(n-2)


# Dynamic programming
n = int(input())
def fibo_dyn(n):
    fibo_dict = {0: 1, 1: 1}
    for i in range(2,n+1):
        fibo_dict[i] = (fibo_dict[i-1] + fibo_dict[i-2])%(1e9 + 7)
    return fibo_dict[n]


print(int(fibo_dyn(n)%(1e9 + 7)))