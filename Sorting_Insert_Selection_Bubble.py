# Insertion Sorting, Selection Sorting , Bubble Sorting
import sys
class Sorting:
    n = int(input("Enter Length of the Array "))
    list = []
    for i in range(n):
        ele = int(input("Enter Element: "))
        list.append(ele)

    @classmethod
    def bubble_sorting(cls):
        ll = []
        ll.extend(cls.list)       # coping static l[] ---> ll[]
        m = cls.n              # coping static n--> m
        # below is Logic
        for i in range(m-1):
            for j in range(m-1-i):
                if ll[j] > ll[j+1]:
                    ll[j], ll[j+1] = ll[j+1], ll[j]
        # print Result
        print("\nBubble Sort Result : ", end="")
        for i in ll:
            print(i, end=" ")
        print("")

    @classmethod
    def selection_sorting(cls):
        ll = []
        ll.extend(cls.list)  # coping static l[] ---> ll[]
        m = cls.n  # coping static n--> m
        # below is Logic
        for i in range(m-1):
            min = i
            j = i+1
            while j< m :
                if ll[j] < ll[min]:
                    min = j
                j = j + 1
            ll[min], ll[i] = ll[i], ll[min]
        # print Result
        print("\nSelection Sort Result : ", end="")
        for i in ll:
            print(i, end=" ")
        print("")

    @classmethod
    def insertion_sorting(cls):
        ll = []
        ll.extend(cls.list)  # coping static l[] ---> ll[]
        m = cls.n  # coping static n--> m
        # below is Logic
        i = 1
        while i <= m-1:
            key = ll[i]
            j = i-1
            while j >=0 and ll[j] > key:
                ll[j+1] = ll[j]
                j = j - 1
            ll[j+1] = key
            i = i + 1
        # Print Result
        print("\nInsertion Sort Result : ", end="")
        for i in ll:
            print(i, end=" ")
        print("")


while True:
    print("\n......Different Sorting Technique.....")
    print("b - Bubble Sorting\ts - Selection Sorting\ti - Insertion Sorting"
          "\ne - Exit\n............")
    option = input("Choose Your Option : ")
    if option.lower() == 'b':
        Sorting.bubble_sorting()
    elif option.lower() == 's':
        Sorting.selection_sorting()
    elif option.lower() == 'i':
        Sorting.insertion_sorting()
    elif option.lower() == 'e':
        sys.exit()
    else:
        print("invalid Entry.........Enter valid Option ")
