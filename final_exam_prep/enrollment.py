def gather_credits(number_of_credits: int, * args):
    courses = []
    gathered_credits = 0
    result =""
    for course_name, course_credits in args:
        if gathered_credits < number_of_credits and course_name not in courses:
            courses.append(course_name)
            gathered_credits += course_credits

    if gathered_credits >= number_of_credits:
        result += f"Enrollment finished! Maximum credits: {gathered_credits}.\n" \
                  f"Courses: {', '.join(sorted(courses))}"
    else:
        result += f"You need to enroll in more courses! You have to gather {number_of_credits - gathered_credits} credits more."
    return result






