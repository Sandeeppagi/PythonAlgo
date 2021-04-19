def staircase(to_climb, max_jump):
    # base case of when there is no stair
    if to_climb == 0:
        return 1
    no_of_ways_to_climb = 0
    # iterate over number of steps, we can take
    for jump in range(1, max_jump + 1):
        # if steps remaining is smaller than the jump step, skip
        if jump <= to_climb:
            # recursive call with n i units lesser where i is the number of steps taken here
            no_of_ways_to_climb += staircase(to_climb - jump, max_jump)
    return no_of_ways_to_climb


print(staircase(3, 2))
