# Ethan Pham    Lab-B    11-3-25
# Uses student ID to return the name of student and their grades
def assign_students():
    students = {}
    with open("students.txt", "r") as file:
        next(file)
        for i in file:
            word = i.strip().split(",")
            studentid = word[0]
            name = word[1]
            students[studentid] = name.strip()
    return students 

def scores(students):
    scores = {}
    with open("scores.txt", "r") as file:
        for studentid in students:
            file.seek(0)
            next(file)
            scorelist = []
            for i in file:
                word = i.strip().split(",")
                if word[0] == studentid:
                    score = int(word[2].strip())
                    scorelist.append(score)
            scores[studentid] = scorelist
    return scores

def grades(scores, student):
    grades = [["Student ID", "Name", "Total Score", "Sum of All Scores", "Score Average"]]
    for student_id, name in student.items():
        score_list = scores.get(student_id, [])
        total_scores = len(score_list)
        sum_scores = sum(score_list)
        average = round(sum_scores / total_scores, 1)
        grades.append([
            student_id,
            name,
            str(total_scores),
            str(sum_scores),
            str(average)
        ])
    grades = "\n".join([",".join(line) for line in grades])
    with open("grades.txt", 'w') as file:
        file.write(grades)
    return grades



def main():
    print(assign_students())
    print("\n------------------------------")
    print(scores(assign_students()))
    print("\n------------------------------")
    print(grades(scores(assign_students()), assign_students()))

if __name__ == "__main__":
    main()