# Linear Search && Binary Search Program
import sys
class Search:
    @staticmethod
    def linear_search() :
        print("\n......Linear Search............\n")
        n=int(input("Enter Length of the Array "))
        l = []
        for i in range(n):
            ele = int(input("Enter Element: "))
            l.append(ele)
        find = int(input("Enter Search_Element to find in Array: "))
        for i in range(n):
            if l[i] == find :
                print(find, "is found at index",i)
                flag = True
        if not flag:
            print(find, "is not Found in List")

    @staticmethod
    def binary_search():
        print("\n...........Binear Search..............\n")
        n = int(input("Enter Length of the Array "))
        l = []
        for i in range(n):
            ele = int(input("Enter Element: "))
            l.append(ele)
        l.sort()
        find = int(input("Enter Element to Find in Array: "))
        s = 0
        e = n-1
        flag = False
        while s <= e:
            mid = (s+e)//2
            if l[mid] == find :
                print(l[mid], "found at index ", mid)
                flag = True
                break
            elif find < l[mid]:
                e = mid -1
            elif find > l[mid]:
                s = mid +1
        if not flag :
            print(find, "is not Found ")

while True:
    print("\n........... Linear Search and Binary Search ..........")
    print("l - Linear Search\nb - Binary Search\ne - Exit")
    option = input("Your Choose Your Option : ")
    if option.lower() == 'l':
        Search.linear_search()
    elif option.lower() == 'b':
        Search.binary_search()
    elif option.lower() == 'e':
        sys.exit()
    else:
        print("invalid Entry.........Enter valid Option ")
