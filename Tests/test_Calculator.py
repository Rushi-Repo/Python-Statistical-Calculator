import unittest

from Calculator.Calculator import Calculator

from CSVReading.CSVReading import CsvReader


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calobject = Calculator()  # Object of the class Calculator

    def test_instantiate_calculator(self):  # Instantiate the Calculator class
        self.assertIsInstance(self.calobject, Calculator)

    def test_addition_method_calculator(self):  # Testing of the add function
        print("Testing Addition")
        try:
            test_data = CsvReader('./Data/Unit Test Addition.csv').data  # Loading the .csv data file
        except:
            print('File not found, Please input valid file.')

        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.add(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)
        print('Successful Testing!')

    def test_subtraction_method_calculator(self):  # Testing of the subtract function
        print(' ')
        print('Testing Subtraction')
        try:
            test_data = CsvReader('./Data/Unit Test Subtraction.csv').data  # Loading the .csv data file
        except:
            print('File not found, Please input valid file.')

        for row in test_data:
            x = row['Value 1']
            y = row['Value 2']
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.subtract(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)
        print('Successful Testing!')

    def test_multiply_method_calculator(self):  # Testing of the multiply function
        print(' ')
        print('Testing Multiplication')
        try:
            test_data = CsvReader('./Data/Unit Test Multiplication.csv').data  # Loading the .csv data file
        except:
            print('File not found, Please input valid file.')

        for row in test_data:
            x = int(row['Value 1'])
            y = int(row['Value 2'])
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.multiply(x, y), expect_result)
            self.assertEqual(self.calobject.result, expect_result)
        print('Successful Testing!')

    def test_divide_method_calculator(self):  # Testing of the divide function
        print(' ')
        print('Testing Division')
        try:
            test_data = CsvReader('./Data/Unit Test Division.csv').data  # Loading the .csv data file
        except:
            print('File not found, Please input valid file.')

        for row in test_data:
            x = float(row['Value 1'])
            y = float(row['Value 2'])
            expect_result = float(row['Result'])
            self.assertEqual(self.calobject.divide(x, y), round(expect_result, 7))
            self.assertEqual(self.calobject.result, round(expect_result, 7))
        print('Successful Testing!')

    def test_square_method_calculator(self):  # Testing of the square function
        print(' ')
        print('Testing Squares')
        try:
            test_data = CsvReader('./Data/Unit Test Square.csv').data  # Loading the .csv data file
        except:
            print('File not found, Please input valid file.')

        for row in test_data:
            x = int(row['Value 1'])
            expect_result = int(row['Result'])
            self.assertEqual(self.calobject.square(x), expect_result)
            self.assertEqual(self.calobject.result, expect_result)
        print('Successful Testing!')

    def test_sqrt_method_calculator(self):  # Testing of the square_root function
        print(' ')
        print('Testing Square Roots')
        try:
            test_data = CsvReader('./Data/Unit Test Square Root.csv').data  # Loading the .csv data file
        except:
            print('File not found, Please input valid file.')

        for row in test_data:
            x = float(row['Value 1'])
            expect_result = float(row['Result'])
            self.assertEqual(self.calobject.square_root(x), round(expect_result, 8))
            self.assertEqual(self.calobject.result, round(expect_result, 8))
        print('Successful Testing!')


if __name__ == '__main__':  # This runs the unittest
    unittest.main()
