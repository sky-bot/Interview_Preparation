/*package whatever //do not write package name here */

// Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.

// Input:
// The first line of input contains an integer T denoting the number of test cases.
// The first line of each test case contains a single integer N denoting the size of array and the size of subarray K.
// The second line contains N space-separated integers A1, A2, ..., AN denoting the elements of the array.

// Output:
// Print the maximum for every subarray of size k.

// Constraints:
// 1 ≤ T ≤ 200
// 1 ≤ N ≤ 107
// 1 ≤ K ≤ N
// 0 ≤ A[i] <= 107

// Example:
// Input:
// 2
// 9 3
// 1 2 3 1 4 5 2 3 6
// 10 4
// 8 5 10 7 9 4 15 12 90 13

// Output:
// 3 3 4 5 5 5 6
// 10 10 10 15 15 90 90

// Explanation:
// Testcase 1: Starting from first subarray of size k = 3, we have 3 as maximum.
// Moving the window forward, maximum element are as 3, 4, 5, 5, 5 and 6.
// Solution O(nk) = O(n)

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t=Integer.parseInt(br.readLine());
		int k=0;
		String a[];
		String s[];
		
		while(k<t)
		{
		    a = br.readLine().split(" ");
		    int len = Integer.parseInt(a[0]);
		    int size = Integer.parseInt(a[1]);
		    int ar[] = new int[len];
		    
		    s = br.readLine().split(" ");
		    for(int i=0;i<len;i++)
		        ar[i]= Integer.parseInt(s[i]);
		        
		    for(int i=0;i<len-size+1;i++)
		    {
		        int max=ar[i];
		        for(int j=i;j<i+size;j++)
		        {
		            if(ar[j]>max)
		                max=ar[j];
		        }
		        System.out.printf("%d ",max);
		        max=0;
		    }
		    System.out.printf("\n");
		    k++;
		}
		
		
	}
}