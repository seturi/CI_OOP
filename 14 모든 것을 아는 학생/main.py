class Student:
    def __init__(self, name, id, major):
        self.student_info = student_info(name, id, major)
        self.grades = []
        
class student_info:
    """학생 기본 정보 수정 메소드"""
    def __init__(self, name, id, major):
        self.name = name
        self.id = id
        self.major = major

def add_grade(student: Student, *grades):
    """학점 추가 메소드"""
    for i in grades:
        if 0 <= i <= 4.3:
               student.grades.append(i)
        else:
            print("수업 학점은 0과 4.3 사이여야 합니다!")

def get_average_gpa(grades):
    """평균 학점 계산 메소드"""
    return sum(grades) / len(grades)

def print_report_card(student: Student):
    """학생 성적표 출력 메소드"""
    print("코드잇 대학 성적표\n\n학생 이름:{}\n학생 번호:{}\n소속 학과:{}\n평균 학점:{}"\
    .format(student.student_info.name,
            student.student_info.id, 
            student.student_info.major, 
            get_average_gpa(student.grades)))
        

# 학생 인스턴스 정의
younghoon = Student("강영훈", 20120034, "통계학과")
younghoon.student_info = student_info("강영훈", 20130024, "컴퓨터 공학과")

# 학생 성적 추가
add_grade(younghoon, 3.0, 3.33, 3.67, 4.3)
# 학생 성적표 
print_report_card(younghoon)