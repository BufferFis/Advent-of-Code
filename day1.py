def read_input(filename):
    with open(filename) as f:
        list1 = []
        list2 = []
        lines = f.readlines()
        for line in lines:
            list1.append(line.split()[0])
            list2.append(line.split()[1])
        return list1, list2
    

def main():
    list1, list2 = read_input('day1input.txt')
    list1.sort()
    list2.sort()
    sum = 0
    for i in range(len(list1)):
        sum += abs(int(list1[i]) - int(list2[i]))
    print(sum)

if __name__ == '__main__':
    main()