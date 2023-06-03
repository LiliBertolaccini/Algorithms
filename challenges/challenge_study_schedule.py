def study_schedule(permanence_period, target_time):
    students_present = 0
    if not isinstance(target_time, int):
        return None
    for start, end in permanence_period:
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if start <= target_time <= end:
            students_present += 1
    return students_present
