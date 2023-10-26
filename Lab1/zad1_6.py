import random

randomlist = []
for i in range(0,10):
    n = random.randint(1,100)
    randomlist.append(n)

print("Not sorted:", randomlist)

#bubble sort
randomlist1 = randomlist.copy()
counter = 0
old_counter = 0

while True:
    for i in range(len(randomlist1)-1):
        if randomlist1[i] > randomlist1[i+1]:
            randomlist1[i], randomlist1[i+1] = randomlist1[i+1], randomlist1[i]
            counter+=1
    if counter == old_counter:
        break
    else:
        old_counter = counter

print("Sorted using bubble sort:", randomlist1)

#insertion sort
randomlist2 = randomlist.copy()

for j in range(1, len(randomlist2)):
    key = randomlist2[j]
    x = j - 1
    while x >= 0 and key < randomlist2[x]:
        randomlist2[x+1] = randomlist2[x]
        x -= 1
    randomlist2[x+1] = key

print("Sorted using insertion sort:", randomlist2)

#python method to check
randomlist.sort()
print("Sorted using Python:", randomlist)