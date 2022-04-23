"""
https://structy.net/problems/premium/combine-intervals
"""


def combine_intervals(intervals):
    sorted_intervals = sorted(intervals)
    combined = [sorted_intervals[0]]
    current = 0

    while current < len(sorted_intervals):
        last = combined[-1]
        last_x, last_y = last
        current_x, current_y = sorted_intervals[current]

        if current_x <= last_y:
            if last_y < current_y:
                combined[-1] = (last_x, current_y)
        else:
            combined.append((current_x, current_y))
        current += 1
        
    return combined


if __name__ == '__main__':
    intervals = [
        (1, 4),
        (12, 15),
        (3, 7),
        (8, 13),
    ]
    print(combine_intervals(intervals))
    # -> [ (1, 7), (8, 15) ]

    intervals = [
        (6, 8),
        (2, 9),
        (10, 12),
        (20, 24),
    ]
    print(combine_intervals(intervals))
    # -> [ (2, 9), (10, 12), (20, 24) ]
