# Sample course data
courses = {
    "course_1": {"name": "Python Programming", "category": "Programming", "difficulty": "Intermediate"},
    "course_2": {"name": "Web Development with Django", "category": "Web Development", "difficulty": "Advanced"},
    "course_3": {"name": "Data Science with Python", "category": "Data Science", "difficulty": "Intermediate"},
    "course_4": {"name": "Machine Learning Fundamentals", "category": "Machine Learning", "difficulty": "Advanced"},
    "course_5": {"name": "Introduction to Algorithms", "category": "Computer Science", "difficulty": "Advanced"}
}

# Function to recommend courses based on user preferences
def recommend_courses(user_scores):
    recommended_courses = []

    for course_id, course_data in courses.items():
        # Calculate a score for each course based on user preferences
        score = 0
        if course_data["category"] in user_scores["categories"]:
            score += 1
        if course_data["difficulty"] == user_scores["preferred_difficulty"]:
            score += 1

        # Adjust score based on additional factors (you can customize this part)
        # Add more conditions or factors as needed
        if "Python" in course_data["name"]:
            score += 1

        # Recommend courses with a score of 2 or higher
        if score >= 2:
            recommended_courses.append(course_data["name"])

    return recommended_courses

# Sample user preferences
user_preferences = {
    "categories": ["Programming", "Data Science"],
    "preferred_difficulty": "Intermediate"
}

# Get course recommendations based on user preferences
recommended_courses = recommend_courses(user_preferences)

# Display recommendations
if recommended_courses:
    print("Recommended Courses:")
    for course in recommended_courses:
        print(f"- {course}")
else:
    print("No courses match your preferences.")
