import unittest

from course.department import Department

__author__ = "Eric Tarrant etarrant@rrc.ca"
__version__ = "1.0.0"

class TestDepartment(unittest.TestCase):

    def test_enumeration_values_initalizated(self):

        #Arrange, Act, Assert

        self.assertEqual(1, Department.COMPUTER_SCIENCE)
        self.assertEqual(2, Department.EDUCATION)
        self.assertEqual(3, Department.ENGINEERING)
        self.assertEqual(4, Department.MEDICINE)

if __name__ == "__main__":
    unittest.main()
 