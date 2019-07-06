import java.io.*;
import java.lang.*;
import java.util.*;

class BubbleSortRecursive
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int len = Integer.parseInt(br.readLine());;
        String s[];
        s = br.readLine().split(" ");
       
        int[] arr = new int[len];

        for(int i=0;i<len;i++)
            arr[i] = Integer.parseInt(s[i]); 
        System.out.printf("Our Initial Array: ");
        Display(arr);

        arr = BubbleSort(arr, len);
        System.out.println("Final Array: ");
        Display(arr);

        System.out.println(arr);
    }

    public static void Display(int[] arr)
    {
        for(int i=0;i<arr.length;i++)
            System.out.printf("%d\t",arr[i]);
        System.out.println();
    }
    private static int[] BubbleSort(int[] arr, int len)
    {   
        if (len<2)
            return arr;
        
        for(int i=0;i<len-1;i++)
        {
            if(arr[i]>arr[i+1])
            {
                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp; 
            }
        }

        return BubbleSort(arr, len-1);
    }

}