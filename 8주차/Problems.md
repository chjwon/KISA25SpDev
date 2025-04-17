# 1. Subarray MaxMin

Given an array, for each of its subarrays of a given length, determine the minimum element in the subarray. Of all these minima, determine the maximum. The first subarray starts at index 0 and suvvessive subarrays start at indices 1, 2, and so on until the last element of the subarray is the last element of the array. 

**Example**

n = 5, the number of elements  
arr = [1,2,3,4,5]  
k = 2

For subarray szie k = 2, the subarrays are [1,2], [2,3], [3,4], [4,5] and the minima are [1,2,3,4]. The maximum of these is 4, the final answer.

**Function Description**

Complete the function MaxMin in the editor below.

*maxMin* has the following parameter(s):

    int arr[n] : an array of integers
    int k : an integer

Returns:

    int: an integer inficating the maximum of the minima of the subarrays

**Constraints**

* 1 $\leq$ n $\leq$ $10^6$
* 1 $\leq$ arr[i] $\leq$ $10^9$

    (0 $\leq$ i $\lt$ n)

* 1 $\leq$ k $\leq$ n


## Sample Case 0

### Sample Input

5   -> arr[] size n = 5  
1   -> arr = [1,2,3,1,2]  
2  
3  
1  
2  
1 -> k = 1

### Sample Output

3

### Explanation
Each element of arr = [1,2,3,1,2] is an array of size k = 1 and its minimum. The maximum of these minima is 3.

## Sample Case 1
### Sample Input
3 -> arr[] size n = 3  
1 -> arr = [1,1,1]  
1  
1  
2 -> k = 2

### Sample Output
1

### Explanation
The two subarrays of size k = 2 are [1,1],[1,1]

## Sample Case 2
### Sample Input
5 -> arr[] size n = 5  
2  -> arr = [2,5,4,6,8]  
5  
4  
6  
8  
3 -> k = 3

### Sample Output
4

### Explanation
The subarrays of arr = [2,5,4,6,8] of size k = 3 are [2,5,4],[5,4,6],[4,6,8]. Their minima are [2,4,4] and the maximum of these is 4. 

<hr/>
<hr/>
<hr/>  

# 2. Anagrams
An anagram is a sequence of numbers that can be formed by rearranging the digits of a string. Given a string that consists of only digits, modify the first half of the string so that it is an anagram of the second half. Determine the minimum number of operations needed to complete the task.

The following is one operation:
* Replace any digit in the string with any other digit (0-9).

**Example**  
s = '123122'  
The first half is '123' and the second half is '122'. Change the 3 in the first half to 2, resulting in '122', an anagram of the second half.

**Function Description**  
Complete the function *getAnagram* in the editor below.  

*getAnagram* has the following parameter:

    string: a string of digits

Returns:

    int: the minimum number of operations needed to make the string's first half an anagram of its second half

**Constraints**
* 1 $\leq$ n $\leq$ $10^5$
* s consists of digits only.
* The length of s is a multiple of 2.

## Sample Case 0
### Sample Input
123456 -> s = '123456'
### Sample Output
3
### Explanation
The first half, '123' can be converted to '456' in 3 operations. Converting it to '465', '546', '654', etc. would also work, but in all cases, it requires 3 operations. 

## Sample Case 1
### Sample Input
786678
### Sample Output
0
### Explanation
The first half, '786' is already an anagram of '678', so no operations are needed.