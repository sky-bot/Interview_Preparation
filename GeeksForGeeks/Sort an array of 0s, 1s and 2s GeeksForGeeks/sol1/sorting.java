// Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.

// Input:
// The first line contains an integer 'T' denoting the total number of test cases. Then T testcases follow. Each testcases contains two lines of input. The first line denotes the size of the array N. The second lines contains the elements of the array A separated by spaces.

// Output: 
// For each testcase, print the sorted array.

// Constraints: 
// 1 <= T <= 500
// 1 <= N <= 106
// 0 <= Ai <= 2

// Example:
// Input :
// 2
// 5
// 0 2 1 2 0
// 3
// 0 1 0

// Output:
// 0 0 1 2 2
// 0 0 1
// solution_1 O(nlogn)
import java.util.*;
import java.lang.*;
import java.io.*;

class sorting {
	public static void main (String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t=0,k=0,i=0;
		System.out.printf("Enter number of test cases: ");
		t = Integer.parseInt(br.readLine());
		
		while(k<t){

		    int len=0;
		    System.out.printf("Enter len of first array: ");
		    len = Integer.parseInt(br.readLine());
		    

		    int ar[]= new int[len];
		    System.out.printf("Enter Your Array: ");
		    for(i=0;i<len;i++)
		    {
		    
		        ar[i] = Integer.parseInt(br.readLine());
		    }
		    
		  	Arrays.sort(ar);
		    
		    for(int j=0;j<len;j++)
		        System.out.printf("%d ",ar[j]);
		    k++;
		}
		System.out.printf("\n");
	}
}