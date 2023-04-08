def qan_tic():
    tic = "QAN.AX"
    print(tic)

res = qan_tic()
print(res)

def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

print(qan_tic)



def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

tic = "WES.AX"
print(tic)
qan_tic()

def qan_tic():
    print(tic)
    return tic

tic = "WES.AX"
print(tic)
qan_tic()

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]

def is_even_num(lis):
    evennum = []
    for n in lis:
        if n % 2 == 0:
            evennum.append(n)
    return evennum

print(is_even_num(input_list))


my_list = [2, 3, 10, 14, 20, 21, 25, 13, 15]
squared_list = [x**2 for x in my_list if x**2 > 150]
print(squared_list)

