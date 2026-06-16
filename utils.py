# utils.py -- 성적 분석 함수 모음
#   (함수 이름과 매개변수는 바꾸지 마세요. 내용만 고치세요.)
#   ※ 각 함수가 정확히 어떻게 동작해야 하는지는 '문제지(정상 동작 명세)'를 따르세요.

GPA_TABLE = {"A": 4.5, "B": 4.0, "C": 3.0, "D": 2.0, "F": 0.0}


def total_score(student):
    """학생의 총점."""
    return student["국어"] + student["영어"] + student["수학"]


def average_score(student):
    """학생의 평균."""
    # 과목 수인 3으로 나누어야 합니다. (len(student)는 4이므로 버그 유발)
    return total_score(student) / 3.0


def to_grade(avg):
    """평균을 학점으로 변환."""
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def grade_to_gpa(grade):
    """학점을 평점으로 변환."""
    return GPA_TABLE.get(grade, 0.0)


def subject_average(students, subject):
    """과목 평균."""
    if not students:
        return 0.0
    # 하드코딩된 "국어" 대신 subject 변수를 사용하여 해당 과목 점수를 더하고 전체 학생 수로 나눕니다.
    total = sum(stu[subject] for stu in students)
    return total / len(students)


def subject_top(students, subject):
    """과목 최고점."""
    if not students:
        return 0
    # 최고점을 정상적으로 찾기 위해 max를 사용합니다.
    return max(stu[subject] for stu in students)


def grade_distribution(students):
    """학점별 인원."""
    dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for stu in students:
        g = to_grade(average_score(stu))
        if g in dist:
            dist[g] += 1
    return dist


def rank_list(students):
    """총점 기준 정렬."""
    # 총점이 높은 학생이 1등이 되도록 내림차순(reverse=True)으로 정렬합니다.
    return sorted(students, key=lambda s: total_score(s), reverse=True)


def pass_rate(students, cutoff=60):
    """합격 비율(%)."""
    if not students:
        return 0.0
    count = 0
    for stu in students:
        if average_score(stu) >= cutoff:
            count += 1
    return count / len(students) * 100
