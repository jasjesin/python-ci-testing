import pytest
import numpy as np
from matrix_tools.basic_utils import get_numpy_version, add_matrices, SizeError

# Test class for the matrix-tools package

class TestMatrixTools:

    # Define inputs and expected outputs
    # Test Case 1: Will pass with exact comparison
    a1 = np.array([[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]])
    b1 = np.array([[8, 7, 6],
                   [5, 4, 3],
                   [2, 1, 0]])
    expected1 = np.array([[8, 8, 8],
                          [8, 8, 8],
                          [8, 8, 8]])

    # Test Case 2: Will fail with exact comparison due to numerical error
    a2 = np.array([[0, 1, 2],
                   [3, 4, 5],
                   [6, 7, 8]])
    b2 = np.array([[3*0.1, 2,  3],
                   [0,     0,  0],
                   [-1,   -2, -3]])
    expected2 = np.array([[0.3, 3, 5],
                          [3,   4, 5],
                          [5,   5, 5]])

    # Test Case 3: Will exercise shape mismatches
    a3 = np.array([[1, 2],
                   [3, 4]])
    b3 = np.array([[0, 9, 8],
                   [7, 6, 5],
                   [4, 3, 2]])
    expected3 = None

    # Define test methods
    def test_numpy_version(self):
        """
        Checks for the correct NumPy version as per specification
        """
        np_ver = get_numpy_version()
        assert(np_ver == "1.17.0")
        print("Correct NumPy version found: " + np_ver)

    @pytest.mark.skip(reason="Not using exact matrix comparison")
    @pytest.mark.parametrize("a,b,expected",[(a1,b1,expected1),(a2,b2,expected2)])
    def test_addition_exact(self,a,b,expected):
        """
        Tests the addition of 2 matrices by exact comparison
        """
        actual = add_matrices(a,b)
        assert((expected == actual).all())
        print("Matrices are exactly equal")

    @pytest.mark.parametrize("a,b,expected",[(a1,b1,expected1),(a2,b2,expected2),(a3,b3,expected3)])
    def test_addition_close(self,a,b,expected):
        """
        Tests the addition of 2 matrices by checking if they are close within some tolerance
        """

        # Try run the test
        try:
            actual = add_matrices(a,b)
            assert(np.allclose(actual,expected,rtol=1e-05,atol=1e-08))
            print("Matrices are equal within specified tolerance")

        # If there is an exception thrown of type SizeError, this is an expected failure.
        # We will still pass the test and reprint it.
        except SizeError as e:
            print("Correctly found size exception:")
            print(e.args[0])

        