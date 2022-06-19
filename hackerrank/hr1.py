q = [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]
n = 2


def dynamicArray(n, queries):
    # Write your code here
    # print(n, queries)
    last_ans = 0
    arr = [[] for i in range(n)]
    ans_arr = []
    print(queries)

    for i in queries:
        q = i[0]
        x = i[1]
        y = i[2]

        idx = (bool(x) ^ bool(last_ans)) % n
        if q == 1:
            arr[idx].append(y)
        elif q == 2:
            last_ans = arr[idx][y % len(arr[idx])]
            ans_arr.append(last_ans)
        print(ans_arr)
    return ans_arr

dynamicArray(n,q)