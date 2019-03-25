// Given an array arr and a number K where K is smaller than size of array, the task is to find the K’th smallest element in the given array. It is given that all array elements are distinct.

// Expected Time Complexity: O(n)

// Input:
// The first line of input contains an integer T, denoting the number of testcases. Then T test cases follow. Each test case consists of three lines. First line of each testcase contains an integer N denoting size of the array. Second line contains N space separated integer denoting elements of the array. Third line of the test case contains an integer K.

// Output:
// Corresponding to each test case, print the desired output in a new line.

// Constraints:
// 1 <= T <= 100
// 1 <= N <= 105
// 1 <= arr[i] <= 105
// 1 <= K <= N

// Example:
// Input:
// 2
// 6
// 7 10 4 3 20 15
// 3
// 5
// 7 10 4 20 15
// 4

// Output:
// 7
// 15

// Explanation:
// Testcase 1: 3rd smallest element in the given array is 7.


/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int l=0, t=Integer.parseInt(br.readLine());
		String s[];
		
		while(l<t)
		{
		    int len = Integer.parseInt(br.readLine());
		    s = br.readLine().split(" ");
		    int ar[] = new int[len];
		    
		    for(int i=0;i<len;i++)
		        ar[i]=Integer.parseInt(s[i]);    
		    
		    int k = Integer.parseInt(br.readLine());
		    
		    Arrays.sort(ar);
		    
		    for(int i=0;i<len-1;i++)
		    {
		        if(ar[i]<ar[i+1])
		            k--;
		        
		        if(k==1)
		            System.out.printf("%d",ar[i+1]);

		        if(k==0)
		        	System.out.printf("%d",ar[i]);        
		    }
		    
		    l++;
		}
	}
}


