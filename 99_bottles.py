for bottles in range(99, 0, -1):
    next_bottles = bottles - 1

    bottle_word = "bottle" if bottles == 1 else "bottles"
    next_word = 'no more bottles' if next_bottles == 0 else f"{next_bottles} bottle{"s" if next_bottles > 1 else ""}"


    print(f"{bottles} {bottle_word} of beer on the wall")
    print(f"{bottles} {bottle_word} of beer")
    print("Take one down, pass it around")
    print(f"{next_word} of beer on the wall\n")
                                                                                