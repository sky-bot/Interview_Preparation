// Given an array arr of N integers. Find the contiguous sub-array with maximum sum.

// Input:
// The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. The first line of each test case contains a single integer N denoting the size of array. The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

// Output:
// Print the maximum sum of the contiguous sub-array in a separate line for each test case.

// Constraints:
// 1 ≤ T ≤ 110
// 1 ≤ N ≤ 106
// -107 ≤ A[i] <= 107

// Example:
// Input
// 2
// 5
// 1 2 3 -2 5
// 4
// -1 -2 -3 -4
// Output
// 9
// -1

// Explanation:
// Testcase 1: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.


import java.lang.*;
import java.io.*;
import java.util.*;

class Kadane
{
	public static void main(String ch[]) throws Exception
	{
		int max_so_far=Integer.MIN_VALUE,max_ending=0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
 
		System.out.printf("Enter the length of your array: ");
		int size = Integer.parseInt(br.readLine());
		int ar[] = new int[size];


		System.out.printf("Enter your Elements:");
		for (int i=0;i<size ;i++ ) 
		{
			ar[i] = Integer.parseInt(br.readLine());	
		}


		for (int i=0;i<size ;i++ ) 
		{
			max_ending = max_ending + ar[i];
			if(max_ending>max_so_far)
				max_so_far = max_ending;

			if(max_ending<0)
				max_ending=0; 	
		}

		System.out.printf("Largest Sum Contiguous Subarray is %d",max_so_far);





	}
}