#sum of all even numbers from 1 to 100

even_sum = 0
for num in range(0, 101, 2):
    even_sum += num
print(even_sum)