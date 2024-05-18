# Mean-Variance-Standard Deviation Calculator

This is the boilerplate for the Mean-Variance-Standard Deviation Calculator project. 

This project is a Python module named mean_var_std.py that contains a function named calculate(). The function takes a list of 9 digits as input and converts it into a 3x3 Numpy array. It then calculates and returns the mean, variance, standard deviation, max, min, and sum along both axes (rows and columns) and for the flattened matrix.

## Function Description
The calculate() function performs the following steps:

1. Input Validation:

  * Checks if the input list contains exactly 9 elements.
  * Raises a ValueError with the message "List must contain nine numbers." if the input list does not meet this requirement.

2. Conversion to Numpy Array:

  * Converts the input list into a 3x3 Numpy array.

3. Calculations:

  * Computes the mean, variance, standard deviation, max, min, and sum for the rows, columns, and the flattened matrix.

4. Output:

  * Returns a dictionary with the calculated values. The dictionary keys are: mean, variance, standard deviation, max, min, and sum.
  * Each key maps to a list containing the values calculated along axis 1 (rows), axis 2 (columns), and the flattened matrix.

## Example
from mean_var_std import calculate

result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
print(result)

## Expected Output:


{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}

## File Structure
*  mean_var_std.py: Contains the implementation of the calculate() function.
*  main.py: Used for testing and running the calculate() function.
*  test_module.py: Contains unit tests for the calculate() function.

replit link to run the project: https://replit.com/@rahulramakrish2/boilerplate-mean-variance-standard-deviation-calculator
