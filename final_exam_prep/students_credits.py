def students_credits(*args):
    student_results = {}
    total_credits = 0
    result = ""
    for current_course in args:
        course_name, course_credits, max_points, points = current_course.split("-")
        course_credits, max_points, points = int(course_credits), int(max_points), int(points)
        current_course_credits = (points/max_points) * course_credits
        total_credits += current_course_credits
        if course_name not in student_results:
            student_results[course_name] = 0
        student_results[course_name] = current_course_credits

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.\n"

    for key, value in sorted(student_results.items(), key=lambda x: (-x[1], x[0])):
        result += f"{key} - {value:.1f}\n"

    return result



print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)








