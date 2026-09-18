import unittest
class StudentResult:

    def __init__(self):
        self.marks = []
    def add_marks(self, mark):
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")
        self.marks.append(mark)
    def calculate_average(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    def get_result(self):
        average = self.calculate_average()
        if average >= 40:
            return "Pass"
        else:
            return "Fail"

class TestStudentResult(unittest.TestCase):
    def test_pass_student(self):
        student = StudentResult()
        student.add_marks(60)
        student.add_marks(70)
        student.add_marks(80)
        self.assertEqual(student.calculate_average(), 70)
        self.assertEqual(student.get_result(), "Pass")
    def test_fail_student(self):
        student = StudentResult()
        student.add_marks(30)
        student.add_marks(35)
        student.add_marks(40)
        self.assertEqual(student.calculate_average(), 35)
        self.assertEqual(student.get_result(), "Fail")
    def test_negative_marks(self):
        student = StudentResult()
        with self.assertRaises(ValueError):
            student.add_marks(-10)
    def test_marks_above_100(self):
        student = StudentResult()
        with self.assertRaises(ValueError):
            student.add_marks(110)
    def test_boundary_average(self):
        student = StudentResult()
        student.add_marks(40)
        self.assertEqual(student.calculate_average(), 40)
        self.assertEqual(student.get_result(), "Pass")

if __name__ == "__main__":
    unittest.main()