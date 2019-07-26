// Subset Sum Problem | DP-25
// Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
// Example:

// Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
// Output:  True  9.
// this approach is not good since time complexity is 2^n

import java.io.*;
import java.util.*;
import java.lang.*;

class SubsetSum
{
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = {1,8,2,3,12};
        int target=11, sum=0, index=0;

        boolean result = fun(arr, target, sum, index);

        if(result==true)
            System.out.print("Possible");
        else
            System.out.print("Not Possible");
    }

    public static boolean fun(int[] arr, int target, int sum, int index)
    {
        
        if(sum==target)return true;
        if(index==arr.length)return false;

        boolean include = fun(arr, target, sum+arr[index], index+1);
        boolean exclude = fun(arr, target, sum, index+1);

        if(include==true||exclude==true)
            return true;
        else    
            return false;
    }
}