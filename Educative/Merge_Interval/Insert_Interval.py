def insert(intervals, new_interval):
    merged = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(len(intervals)-1):
        if intervals[1] < start:
            merged.append(intervals)
            merged.append(intervals[i])
            continue
        

    return merged


def main():
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    # print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()
