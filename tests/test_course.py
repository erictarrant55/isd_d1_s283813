import unittest

from course.course import Course
from course.department import Department
from course.lecture_course import LectureCourse
from course.student import Student

class TestInit(unittest.testCase):
    """Defines test for the constructor __int__ method."""
    def test_lecture_hall_is_empty_string(self) -> None:

        #Arrange/Act
        with self.assertRaises(ValueError) as context:
            course = LectureCourse("ISD", Department.COMPUTER_SCIENCE, 90, "")

        #Assert
        self.assertEqual("lecture_hall cannot be an empty string", str(context.exception))

class TestLectureHallProperty(unittest.TestCase):
    """Defines tests for the lecture hall property"""

    def test_returns_current_state(self) -> None:

        course = LectureCourse("ISD", Department.COMPUTER_SCIENCE, 90, "A202")

        self.assertEqual("A202", course.Lecture_hall)


class TestEnrollStudent(unittest.TestCase):
    """Define test for the enroll student method"""
    def test_enroll_student_at_capacity(self) -> None:
        capacity = Course.ENROLLMENT_LIMIT + (Course.ENROLLMENT_LIMIT)

        for _ in range(capacity):
            self.course._Course__students.append(Student())

        with self.assertRaises(ValueError) as context:
            self.course.enroll_student(Student())

        self.assertEqual("Cannot enroll student; course at capacity",
                        str(context.exception))

if __name__ == "__main__":
    unittest.main()
 