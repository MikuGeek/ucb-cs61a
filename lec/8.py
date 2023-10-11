def same_count_test():
    pairs = [[1,2],[2,2],[3,2],[4,4]]
    same_count = 0
    for x, y in pairs:
        print(x, "Then", y)
        if x == y:
            same_count += 1
    print(same_count)
    # x, y is assigned to the two value of pairs in sequence.
