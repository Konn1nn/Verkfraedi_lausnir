from Text_pattern import add_one_letter
def overlap(interval1, interval2):
    if (interval1[0] < interval2[1]) and (interval2[0] < interval1[1]):
        return True
    else:
        return False

if __name__ == "__main__":
    i_1 = [0, 10]
    i_2 = [5, 16]
    i_3 = [-13, 3]
    i_4 = [1, 10]
    i_5 = [9, 11]
    i_6 = [100, 150]
    i_7 = [170, 200]
    my_intervals_combo = [
        [i_1, i_2],
        [i_1, i_3],
        [i_3, i_2],
        [i_4, i_5],
        [i_6, i_7]
    ]
    for i in my_intervals_combo:
        print(f"Interval 1 start: {i[0][0]}")
        print(f"Interval 1 end: {i[0][1]}")
        print(f"Interval 2 start: {i[1][0]}")
        print(f"Interval 2 end: {i[1][1]}")
        if(overlap(i[0], i[1])):
            print("The two intervals overlap")
        else:
            print("The two intervals do not overlap")
        print()

        add_one_letter("Seathor")