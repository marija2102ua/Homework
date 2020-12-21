def count_positives_sum_negatives(arr):
    if arr == []: return []
    first = 0
    second = 0
    for i in arr:
        if i > 0:
            first += 1
        if i < 0:
            second += i
    return [first, second]

