def spy_game(nums):
    pattern_position = 0

    for num in nums:
        if pattern_position == 0 and num == 0:
            pattern_position += 1
        elif pattern_position == 1 and num == 0:
            pattern_position += 1
        elif pattern_position == 2 and num == 7:
            return True

    return False


print(spy_game([1, 2, 4, 0, 0, 7, 5])) #True
print(spy_game([1, 0, 2, 4, 0, 5, 7])) #True
print(spy_game([1, 7, 2, 0, 4, 5, 0])) #False
