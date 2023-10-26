from random import randint

numbers = []
numbers_length = 50
for i in range(numbers_length):
    numbers.append(randint(0,100))

def main(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if (list[i]<list[i+1]):
                list[i],list[i+1]= list[i+1], list[i]
    return list


print(numbers)
if __name__ == '__main__':
    main(numbers)
    print(numbers)