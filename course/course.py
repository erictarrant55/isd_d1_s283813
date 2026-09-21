from abc import ABC, abstractmethod
from course.department import Department
from course.student import Student


class Course(ABC):
    """Represents a course at a post secondary institution."""

    ENROLLMENT_LIMIT = 30
    """The maximum number of student enrolled in a course."""     

    def __init__(
            self,
            name: str,
            department: Department,
            credit_hours: int):
        """Represents a course at an education institution"""
        self.__students = []

        if len(name.strip()) == 0:
            raise ValueError("name cannot be an empty string")


        # if isinstance(credit_hours, int):
            # if credit_hours <= 0:
                # raise ValueError("credit_hours must be a value greater than 0")
              

        self.__name = name
        self.__department = department
        self.credit_hours = credit_hours # call the setter directly

    @property
    def name(self) -> str:
        """Gets the name of the course

        Returns:
            str: The name of the course
        """
        return self.__name

    @property
    def department(self) -> department:
        """Gets the department to which the course belongs

        Returns:
            department: The department to which the course belongs
        """
        return self.__department

    @property
    def credit_hours(self) -> int:
        return self.__credit_hours

    @credit_hours.setter
    def credit_hours(self, credit_hours: int) -> None:
        if credit_hours <= 0:
            raise ValueError("Credit hours must be a positive integer")

        self.__credit_hours = credit_hours

    @property
    def students(self) -> list[Students]:
        """Gets the students enrolled in course.
        
            Returns:
                list[Students] : The students enrolled in the course.
        """
        return self.__students

    @abstractmethod
    def enroll_students(self, student: Student) -> None:
        """Enrolls the student in the course.
        
            Args:
                student (Students) : The student being enrolled in the course.   
        """
        pass
    
    def __str__(self) -> str:
        return (f"Course: {self.__name.title()}\n"
                f"Department: {self.__department.name.title('_','').tile()}"
                f"Credit Hours: {self.__credit_hours}")