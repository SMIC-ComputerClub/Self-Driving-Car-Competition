def drive(distances, velocity):
    right = sum(distances[0:18])
    left = sum(distances[18:36])
    print(left, right)
    acceleration = 1 if velocity < 30 else 0
    if right > left + 50:
        return 15, acceleration
    elif left > right + 50:
        return -15, acceleration
    else:
        return 0, acceleration