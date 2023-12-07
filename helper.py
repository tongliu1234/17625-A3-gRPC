def retrive_top_n_comments(arr, n):
    x = 0
    res = []
    # Bubble sort
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j].score > arr[j + 1].score:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        res.append(arr[len(arr) - i - 1])
        x += 1
        if x == n:
            break
    return res
