#!/usr/bin/env python3
"""
Autograder for Anagrams problem.
This script loads student code from 2_main.py and evaluates it.
"""

import unittest
import time
import random
import sys
import os
from collections import Counter

def load_student_submission(filename="2_main.py"):
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

# Model solution to compare against
class Solution:
    def getAnagram(self, string):
        """
        Calculate the minimum operations to make the first half an anagram of the second half.
        
        :type string: string
        :rtype: int
        """
        if len(string) % 2 != 0:
            return -1  # Invalid input, length must be even
        
        # Split the string into two halves
        mid = len(string) // 2
        first_half = string[:mid]
        second_half = string[mid:]
        
        # Count frequencies of digits in both halves
        first_counter = Counter(first_half)
        second_counter = Counter(second_half)
        
        # Calculate minimum operations needed
        operations = 0
        for digit in '0123456789':
            operations += max(0, first_counter[digit] - second_counter[digit])
        
        return operations

def grade_submission(submission_code, timeout=5):
    """
    Grade a submission for the Anagrams problem.
    
    Args:
        submission_code (str): The submitted code as a string
        timeout (int): Maximum execution time in seconds
    
    Returns:
        dict: Results including score, feedback, and details
    """
    # Create a namespace to execute the submission code
    submission_namespace = {}
    
    try:
        # Execute the submission code to define the Anagrams class
        exec(submission_code, submission_namespace)
        
        # Check if the required class and method exist
        if 'Anagrams' not in submission_namespace:
            return {
                'score': 0,
                'feedback': "Error: 'Anagrams' class not found.",
                'details': []
            }
        
        anagrams = submission_namespace['Anagrams']
        instance = anagrams()
        
        if not hasattr(instance, 'getAnagram'):
            return {
                'score': 0,
                'feedback': "Error: 'getAnagram' method not found in 'Anagrams' class.",
                'details': []
            }
        
        # Create test cases
        test_cases = [
            {
                'name': 'Sample Case 0',
                'string': '123456',
                'expected': 3
            },
            {
                'name': 'Sample Case 1',
                'string': '786678',
                'expected': 0
            },
            {
                'name': 'All Digits Same',
                'string': '111111',
                'expected': 0
            },
            {
                'name': 'Completely Different',
                'string': '123987',
                'expected': 3
            },
            {
                'name': 'Partially Matching',
                'string': '112233',
                'expected': 0
            },
            {
                'name': 'Different Frequencies',
                'string': '121212',
                'expected': 0
            },
            {
                'name': 'Large Same Digit',
                'string': '5' * 1000,
                'expected': 0
            }
        ]
        
        # Add a large random test case
        random.seed(42)  # For reproducibility
        large_test = ''.join(str(random.randint(0, 9)) for _ in range(10000))
        # Calculate expected result using the model solution
        model = Solution()
        large_expected = model.getAnagram(large_test)
        
        test_cases.append({
            'name': 'Large Random Input',
            'string': large_test,
            'expected': large_expected
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
                result = instance.getAnagram(test_case['string'])
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
    print("Anagrams Problem - Autograder")
    print("-"*50)
    
    # Define file path
    submission_file = "2_main.py"
    
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