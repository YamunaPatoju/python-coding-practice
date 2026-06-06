def sort012(self, arr):
    zero = []
    one = []
    two = []

    for i in arr:
        if i == 0:
            zero.append(i)
        elif i == 1:
            one.append(i)
        elif i == 2:
            two.append(i)

    arr[:] = zero + one + two
