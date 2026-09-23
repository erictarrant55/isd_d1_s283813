"""This module defines the LabCourse class."""
from course.course import Course
from course.department import Department
from course.student import Student



class LabCourse():
    """Represents a course that has a lab component"""
    def __init__(self, name:str, department: Department, credit_hours):
        """Initialize a new instance of Course Class
        
        Args:
            name(str): The name of the course.
            department(Department): The department the course is
            delivered.
            credit_hours(int): The number of credit hours

        Raises:
            ValueError when
                - the name contain no non-whitespace characters
                - the credit_hours is a positive value ie. greater than zero      
        """
        super().__init__(name, department, credit_hours)
        self.__lab_equipment = []

    def enroll_student(self, student: Student) -> None:
        """Enrolls a student in the course"""
        capacity = int (Course.ENROLLMENT_LIMIT/2)

        if len(self.students) >= capacity:
            raise ValueError("Cannot enroll student, course at capacity")

    def add_lab_equipment(self, equipment: str) -> None:
        """Add specified equipment to the required for course
                
            if the equipment already exists, it won't be added again
        
            Args:
                equipment(str) : The equipment to add to the course
        """
        equipment = equipment.strip().title()

        if equipment == "":
            raise ValueError("equipment cannot be empty")

        if equipment not in self.__lab_equipment:
            self.__lab_equipment.append(equipment)

    def __str__(self) -> str:
        """Return a nicely printable string representation of object
        
            Returns:
                str: A string representation of the lab course object
        """
        return (f"{super().__str__()}\n"
                f"Lab Equipment: {self.__lab_equipment}")
