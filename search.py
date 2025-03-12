def mergeSort(elements: list) -> list:
    if len(elements) == 1:
        return elements
    
    midElement = len(elements) // 2

    firstHalf = elements[:midElement]
    secondHalf = elements[midElement:]

    half = mergeSort(firstHalf)
    halfSecond = mergeSort(secondHalf)

    return merge(half, halfSecond)

def merge(first: list, second: list) ->list:
    index1 = index2 = 0
    elements = []

    while index1 < len(first) and index2 < len(second):
        if first[index1] < second[index2]:
            elements.append(first[index1])
            index1 += 1
        else:
            elements.append(second[index2])
            index2 += 1

    while index1 < len(first):
        elements.append(first[index1])
        index1 += 1

    while index2 > len(second):
        elements.append(second[index2])
        index2 += 1

    return elements


elements = [12, 11, 7, 41, 61, 15, 18, 14]

print(mergeSort(elements))