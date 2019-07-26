// Subset Sum Problem | DP-25
// Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.
// Example:

// Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
// Output:  True  9.
// this approach is not good since time complexity is 2^n

import java.io.*;
import java.util.*;
import java.lang.*;

class EqualPartition
{
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = {1,8,2,11};
        
        int total=0;

        for(int i=0;i<arr.length;i++)
            total = total + arr[i];

        if(total%2!=0){
            System.out.printf("Not Possibe");
            return;
        }

        boolean result = fun(arr,0,0,total);

        if(result==true)
            System.out.println("Possible");
        else
            System.out.println("Not Possible");

    }

    public static boolean fun(int[] arr, int sum, int index, int total)
    {   
        if(2*sum==total)return true;
        if(index==arr.length)return false;
        boolean include = fun(arr, sum+arr[index], index+1, total);
        boolean exclude = fun(arr, sum, index+1, total);

        if(include==true||exclude==true)
            return true;
        else
            return false;
    }

    public static int sumList(List<Integer> li)
    {
        int sum =0;
        for(int i:li)
            sum = sum + i;
        return sum;
    }
}