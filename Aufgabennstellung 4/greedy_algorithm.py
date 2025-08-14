from operator import itemgetter


def activities_greedy(activities):
    activities.sort(key=itemgetter(1))
    current_end_time = 0
    number_of_activities = 0

    # Einmaliges lineares durchlaufen der Elemente
    for start_activity, end_activity in activities:
        if start_activity >= current_end_time:
            # Erhöhen der Anzahl der Aktivitäten
            number_of_activities += 1
            # Aktualisieren des letzten Endwertes
            current_end_time = end_activity

    return number_of_activities


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
print(f"Non overlapping activities: {activities_greedy(activities)}")
