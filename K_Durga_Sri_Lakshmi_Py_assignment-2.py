university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}


for sid, details in university_data.items():
    print(f"\n{details['name']} -- {details['major']}")


for sid, details in university_data.items():
    print(f"\nStudent: {details['name']}")

    for course, scores in details['courses'].items():
        avg = sum(scores.values()) / len(scores)
        print(f" \n {course} - Avg: {avg:.2f}")


for sid, details in university_data.items():
    courses = details.get("courses", {})

    if "Python101" in courses and courses["Python101"].get("final", 0) > 90:
        print(f"\n{details['name']} - Final: {courses['Python101']['final']}")


university_data["S101"]["courses"]["404"] = {"midterm": 78, "final": 99, "project": 97}
print("\n404 added successfully.\n")


crs_tot = {}
crs_cnt = {}


for sid, details in university_data.items():
    for course, scores in details["courses"].items():
        if course not in crs_tot:
            crs_tot[course] = 0
            crs_cnt[course] = 0

        crs_tot[course] += sum(scores.values()) / len(scores)
        crs_cnt[course] += 1

for course in crs_tot:
    avg = crs_tot[course] / crs_cnt[course]
    print(f"\n{course} - Avg Score: {avg:.2f}")

