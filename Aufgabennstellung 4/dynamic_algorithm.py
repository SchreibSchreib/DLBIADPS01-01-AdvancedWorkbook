from operator import itemgetter


def activities_dynamic(activities):
    activities.sort(key=itemgetter(1))
    number_of_activities = len(activities)

    max_activities = [0] * number_of_activities
    max_activities[0] = 1

    for current_index in range(1, number_of_activities):
        number_if_taken = 1
        for previous_index in range(current_index - 1, -1, -1):
            if activities[previous_index][1] <= activities[current_index][0]:
                number_if_taken += max_activities[previous_index]
                break
        
        number_if_skipped = max_activities[current_index - 1]

        max_activities[current_index] = max(number_if_taken, number_if_skipped)

    return max_activities[-1]


activities = [
    (3, 5),
    (2, 14),
    (5, 7),
    (3, 9),
    (6, 10),
    (5, 9),
    (1, 4),
    (8, 11),
    (0, 6),
    (8, 12),
    (12, 16),
]

print(f"Nicht überlappende Aktivitäten: {activities_dynamic(activities)}")
