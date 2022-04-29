def study_schedule(permanence_period, target_time):
    count = 0

    for start_time, end_time in permanence_period:
        try:
            if start_time <= target_time <= end_time:
                count += 1
        except TypeError:
            return None

    return count
