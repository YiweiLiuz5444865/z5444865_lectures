print(1 is True)


var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']
print(var1 is var2) # --> True
print(var1 == var2) # --> True
print(var3 is var4) # --> False
print(var3 == var4) # --> True

x = 5
if x > 0:
    print("x is positive")

x = 0
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

hours_worked = float(input( ))

if hours_worked <= 35:
    pay = hours_worked * 51.45
else:
    pay = 35 * 51.45 + (hours_worked - 35) * 88.9

print(f"This weekly payment is: {pay}")


numbers = [3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15]

tamp_largest=numbers[0]
print('Before',tamp_largest)

for number in numbers:
    if number > tamp_largest:
        tamp_largest = number
    print(number,tamp_largest)
print(f'The largest value is {tamp_largest}')
