// Problem
// Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

// Input:
// The first line contains T, denoting the number of testcases. Then follows description of testcases.
//  Each case begins with a single positive integer N denoting the size of array. 
//  The second line contains the N space separated positive integers denoting the elements of array A.

// Output:
// For each testcase, print "Yes" or  "No" whether it is Pythagorean Triplet or not (without quotes).

// Constraints:
// 1 <= T <= 100
// 1 <= N <= 107
// 1 <= A[i] <= 1000

// Example:
// Input:
// 1
// 5
// 3 2 4 6 5

// Output:
// Yes

// Explanation:
// Testcase 1: a=3, b=4, and c=5 forms a pythagorean triplet, so we print "Yes"

//Solution O(n^2)
/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int l=0, t =Integer.parseInt(br.readLine());
        String s[];
        
		while(l<t)
		{
		    int len = Integer.parseInt(br.readLine());
		    s = br.readLine().split(" ");
		    int ar[]=new int[len];
		    for(int i=0;i<len;i++){
		        ar[i] = Integer.parseInt(s[i]);
		        ar[i] = ar[i]*ar[i];
		    }
		    Arrays.sort(ar);
		    
		    int left, right;


		    for(int i=len-1;i>1;i--)
		    {
		    	left=0;
		    	right=i-1;

		    	while(left<right)
		    	{
		    		if(ar[i]==ar[left]+ar[right]){
		    			System.out.printf("Yes\n");
		    			return;
		    		}

		    		if(ar[left] + ar[right] < ar[i])
		    			left++;
		    		else 
		    			right--; 
		    	}
		    }
		    
		    
		    System.out.printf("No\n");
		    l++;
		}
	}
}