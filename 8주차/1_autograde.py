#!/usr/bin/env python3
"""
Autograder for SubarrayMaxMin problem.
This script loads student code from 1_main.py and evaluates it.
"""

import unittest
import time
import random
import sys
import os

def load_student_submission(filename="1_main.py"):
    """
    Load the student's submission from file.
    
    Args:
        filename (str): Path to the student's submission
    
    Returns:
        str: The content of the student's submission
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: Could not find {filename}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading {filename}: {str(e)}")
        sys.exit(1)

def grade_submission(submission_code, timeout=10):
    """
    Grade a submission for the SubarrayMaxMin problem.
    
    Args:
        submission_code (str): The submitted code as a string
        timeout (int): Maximum execution time in seconds
    
    Returns:
        dict: Results including score, feedback, and details
    """
    # Create a namespace to execute the submission code
    submission_namespace = {}
    
    try:
        # Execute the submission code to define the SubarrayMaxMin class
        exec(submission_code, submission_namespace)
        
        # Check if the required class and method exist
        if 'SubarrayMaxMin' not in submission_namespace:
            return {
                'score': 0,
                'feedback': "Error: 'SubarrayMaxMin' class not found.",
                'details': []
            }
        
        subarrayMaxMin = submission_namespace['SubarrayMaxMin']
        instance = subarrayMaxMin()
        
        if not hasattr(instance, 'maxMin'):
            return {
                'score': 0,
                'feedback': "Error: 'maxMin' method not found in 'SubarrayMaxMin' class.",
                'details': []
            }
        
        # Create test cases
        test_cases = [
            {
                'name': 'Example Case',
                'arr': [1, 2, 3, 4, 5],
                'k': 2,
                'expected': 4
            },
            {
                'name': 'Sample Case 0',
                'arr': [1, 2, 3, 1, 2],
                'k': 1,
                'expected': 3
            },
            {
                'name': 'Sample Case 1',
                'arr': [1, 1, 1],
                'k': 2,
                'expected': 1
            },
            {
                'name': 'Sample Case 2',
                'arr': [2, 5, 4, 6, 8],
                'k': 3,
                'expected': 4
            },
            {
                'name': 'Edge Case: k equals n',
                'arr': [7, 2, 9, 3, 1],
                'k': 5,
                'expected': 1
            },
            {
                'name': 'Decreasing Array',
                'arr': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                'k': 3,
                'expected': 8
            },
            {
                'name': 'All Same Elements',
                'arr': [5, 5, 5, 5, 5],
                'k': 3,
                'expected': 5
            }
        ]
        
        # Add larger test case for performance testing
        large_arr = list(range(1, 1001))
        random.shuffle(large_arr)  # Shuffle to make it more realistic
        
        # Calculate the correct expected result for the shuffled array
        expected_result = float('-inf')
        for i in range(len(large_arr) - 500 + 1):
            subarray = large_arr[i:i+500]
            min_val = min(subarray)
            expected_result = max(expected_result, min_val)
        
        test_cases.append({
            'name': 'Large Array Test',
            'arr': large_arr,
            'k': 500,
            'expected': expected_result  # Correctly calculated max of mins
        })
        
        # Execute test cases
        results = []
        total_score = 0
        points_per_test = 100 / len(test_cases)
        
        for test_case in test_cases:
            test_result = {
                'name': test_case['name'],
                'passed': False,
                'feedback': ''
            }
            
            try:
                start_time = time.time()
                result = instance.maxMin(test_case['arr'], test_case['k'])
                end_time = time.time()
                
                if end_time - start_time > timeout:
                    test_result['feedback'] = f"Time Limit Exceeded: took {end_time - start_time:.2f} seconds (limit: {timeout} seconds)"
                elif result == test_case['expected']:
                    test_result['passed'] = True
                    test_result['feedback'] = f"Correct! Execution time: {end_time - start_time:.4f} seconds"
                    total_score += points_per_test
                else:
                    test_result['feedback'] = f"Wrong Answer: Expected {test_case['expected']}, got {result}"
            except Exception as e:
                test_result['feedback'] = f"Error: {str(e)}"
            
            results.append(test_result)
        
        # Calculate final score and provide feedback
        final_score = round(total_score)
        
        # Determine overall feedback with specific details about pass/fail
        passed_tests = [test['name'] for test in results if test['passed']]
        failed_tests = [test['name'] for test in results if not test['passed']]
        
        if final_score == 100:
            feedback = "Excellent work! Your solution passed all test cases efficiently."
        elif final_score >= 80:
            feedback = f"Good job! Your solution works for most cases. Passed: {', '.join(passed_tests)}. Failed: {', '.join(failed_tests)}."
        elif final_score >= 50:
            feedback = f"Your solution passes some test cases but needs improvement. Passed: {', '.join(passed_tests)}. Failed: {', '.join(failed_tests)}."
        else:
            if passed_tests:
                feedback = f"Your solution needs significant work. Only passed: {', '.join(passed_tests)}. Failed: {', '.join(failed_tests)}."
            else:
                feedback = "Your solution failed all test cases. Review the problem requirements carefully and try again."
        
        return {
            'score': final_score,
            'feedback': feedback,
            'details': results
        }
    
    except Exception as e:
        return {
            'score': 0,
            'feedback': f"Error evaluating submission: {str(e)}",
            'details': []
        }

def print_results(results):
    """Print the grading results in a readable format."""
    print("\n" + "="*50)
    print("GRADING RESULTS")
    print("="*50)
    
    print(f"\nScore: {results['score']}/100")
    print(f"Feedback: {results['feedback']}")
    print("\nTest Case Details:")
    
    for i, test in enumerate(results['details']):
        status = "✓ PASS" if test['passed'] else "✗ FAIL"
        print(f"\n{i+1}. {test['name']}: {status}")
        print(f"   {test['feedback']}")
    
    print("\n" + "="*50)

def main():
    """Main function to run the autograder."""
    print("SubarrayMaxMin Problem - Autograder")
    print("-"*50)
    
    # Define file path
    submission_file = "1_main.py"
    
    # Check if custom file path is provided
    if len(sys.argv) > 1:
        submission_file = sys.argv[1]
    
    print(f"Loading submission from: {submission_file}")
    
    # Load and grade the submission
    submission_code = load_student_submission(submission_file)
    results = grade_submission(submission_code)
    
    # Print results to console
    print_results(results)

if __name__ == "__main__":
    main()