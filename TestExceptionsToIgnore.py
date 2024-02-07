import unittest
from contextlib import redirect_stdout
from io import StringIO

from NoExceptions.ExceptionsToIgnore import ExceptionsToIgnore


class TestExceptionsToIgnore(unittest.TestCase):

    def test_ignore_zero_division_error(self):
        """
        Test to ignore ZeroDivisionError exception.
        """
        # Initialize printed_output variable
        printed_output = None

        # Capture the print output
        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([ZeroDivisionError]).handle_exceptions():
                # Attempt a division by zero
                1 / 0

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output = "Ignoring exception division by zero"
        if expected_output in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output '{expected_output}' not found in printed output '{printed_output}'")

    def test_ignore_type_error(self):
        """
        Test to ignore TypeError exception.
        """
        # Initialize printed_output variable
        printed_output = None

        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([TypeError]).handle_exceptions():
                # Attempt operation with inappropriate type
                1 + "2"

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output = "Ignoring exception unsupported operand type(s) for +: 'int' and 'str'"
        if expected_output in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output '{expected_output}' not found in printed output '{printed_output}'")

    def test_ignore_value_error(self):
        """
        Test to ignore ValueError exception.
        """
        # Initialize printed_output variable
        printed_output = None

        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([ValueError]).handle_exceptions():
                # Attempt operation with inappropriate value
                int("abc")

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output = "Ignoring exception invalid literal for int() with base 10: 'abc'"
        if expected_output in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output '{expected_output}' not found in printed output '{printed_output}'")

    def test_ignore_name_error(self):
        """
        Test to ignore NameError exception.
        """
        # Initialize printed_output variable
        printed_output = None

        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([NameError]).handle_exceptions():
                # Attempt to access undefined variable
                print(undefined_variable)

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output = "Ignoring exception name 'undefined_variable' is not defined"
        if expected_output in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output '{expected_output}' not found in printed output '{printed_output}'")

    def test_ignore_key_error(self):
        """
        Test to ignore KeyError exception.
        """
        # Initialize printed_output variable
        printed_output = None

        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([KeyError]).handle_exceptions():
                # Attempt to access non-existent key in dictionary
                my_dict = {"key": "value"}
                print(my_dict["nonexistent_key"])

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output = "Ignoring exception 'nonexistent_key'"
        if expected_output in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output '{expected_output}' not found in printed output '{printed_output}'")

    def test_ignore_index_error(self):
        """
        Test to ignore IndexError exception.
        """
        # Initialize printed_output variable
        printed_output = None

        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([IndexError]).handle_exceptions():
                # Attempt to access index out of range
                my_list = [1, 2, 3]
                print(my_list[10])

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output = "Ignoring exception list index out of range"
        if expected_output in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output '{expected_output}' not found in printed output '{printed_output}'")

    def test_ignore_file_not_found_error(self):
        """
        Test to ignore FileNotFoundError exception.
        """
        # Initialize printed_output variable
        printed_output = None

        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([FileNotFoundError]).handle_exceptions():
                # Attempt to open non-existent file
                with open("nonexistent_file.txt", "r") as file:
                    pass

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output = "Ignoring exception [Errno 2] No such file or directory"
        if expected_output in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output '{expected_output}' not found in printed output '{printed_output}'")

    def test_ignore_zero_division_and_type_error(self):
        """
        Test to ignore ZeroDivisionError and TypeError exceptions.
        """
        # Initialize printed_output variable
        printed_output = None

        with StringIO() as buffer, redirect_stdout(buffer):
            with ExceptionsToIgnore([ZeroDivisionError, TypeError]).handle_exceptions():
                # Attempt division by zero
                1 / 0

                # Attempt operation with inappropriate type
                1 + "2"

            # Get the printed output
            printed_output = buffer.getvalue().strip()

        # Check if the expected print statement occurred
        expected_output_1 = "Ignoring exception division by zero"
        expected_output_2 = "Ignoring exception unsupported operand type(s) for +: 'int' and 'str'"
        if expected_output_1 in printed_output or expected_output_2 in printed_output:
            print("Success")
        else:
            self.fail(f"Expected output expected_output_1: {expected_output_1}. expected_output_2:"
                      f" {expected_output_2}. not found in printed output: {printed_output}")


if __name__ == "__main__":
    unittest.main()
