
list = [18,2,10,7,3,9,6,15,0,13]

def selection_sort(list):
    n = len(list)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if list[j] < list[m]:
                m = j
        list[i], list[m] = list[m], list[i]


selection_sort(list)
print(list)



def binary_search(search_element, list_to_search: list):
    pos = -1    #  используем -1, так как такого индекса нет
    result_ok = False
    first = 0
    last = len(list_to_search) - 1

    while first < last:
        middle = (first + last) // 2
        if search_element == list_to_search[middle]:
            first = middle
            last = first    # для того, чтобы прервать цикл
            result_ok = True
            pos = middle
        elif search_element > list_to_search[middle]:
            first = middle + 1
        else:
            last = middle - 1
    if result_ok:
        print(f'Элемент найден, индекс: {pos}')
    else:
        print(f' Элемент не найден')

binary_search(15, [18,2,10,7,3,9,6,15,0,13])