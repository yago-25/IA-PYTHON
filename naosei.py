def search(elements: list, element: int) -> int:
    for index, value in enumerate(elements):
        if value == element:
            return index
        
        return "nao hj nao"

elementos = [3, 4, 1, 5, 14]
oi = search(elementos, 4)
print(oi)