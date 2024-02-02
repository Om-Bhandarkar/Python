def factorial_array(arr):
    fact = 1
    result = []

    for num in arr:
        fact *= num
        result.append(fact)

    return result

arr = [1, 2, 3, 4, 5]
print(factorial_array(arr))