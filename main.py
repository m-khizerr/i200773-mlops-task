TOTAL_STUDENTS = 0

class StudentsInMLOps:
    @staticmethod
    def enrollStudents(num_students: int):
        global TOTAL_STUDENTS
        if num_students < 0:
            raise ValueError("Number of students to enroll cannot be negative.")
        
        TOTAL_STUDENTS += num_students

    @staticmethod
    def dropStudents(num_students: int):
        global TOTAL_STUDENTS
        if num_students < 0:
            raise ValueError("Number of students to drop cannot be negative.")
        
        TOTAL_STUDENTS -= num_students
        if TOTAL_STUDENTS < 0:
            TOTAL_STUDENTS = 0

    @staticmethod
    def getTotalStrength() -> int:
        return TOTAL_STUDENTS

    @staticmethod
    def getClassName() -> str:
        return StudentsInMLOps.__name__
