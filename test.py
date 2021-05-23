# https://www.programiz.com/python-programming/examples/prime-number-intervals
# Python program to display all the prime numbers within an interval

import time

start = time.time()

lower = 0
upper = 2*2*2*2*2*2*2*2*2*2*2*2*2

anz = 0

# empty list
my_list = []

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           #print(num)
           my_list.insert(anz, num)
           anz += 1

print('Anzahl = '+str(anz))

print(len(my_list))

end = time.time()
print('time in sec.: ')
print(end - start)

print(my_list)
