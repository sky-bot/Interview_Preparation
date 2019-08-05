import java.util.*;
import java.lang.*;
import java.io.*;

class Edit
{
    public static void main(String[] args)throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.printf("Enter your String 1: ");
        String str1 = br.readLine().toLowerCase();
        System.out.printf("Enter your String 2: ");
        String str2 = br.readLine().toLowerCase();

        int[][] arr = new int[str1.length()+1][str2.length()+1];

        arr[0][0]=0;
        for(int i=0;i<=str1.length();i++)
        {   
            for(int j=0;j<=str2.length();j++)
            {
                if(i==0 && j!=0)
                    arr[0][j] = arr[0][j-1] + 1; 
            }
            arr[i][0] = i;
        }
           
        // Display(arr);

        for(int i=1;i<=str1.length();i++)
        {
            for(int j=1;j<=str2.length();j++)
            {
                if(str1.charAt(i-1)==str2.charAt(j-1))
                    arr[i][j] = Min(arr[i][j-1],arr[i-1][j-1],arr[i-1][j]); 
                else
                {
                    arr[i][j] =  Min(arr[i][j-1],arr[i-1][j-1],arr[i-1][j]) + 1; 
                }
            }
        }

        System.out.printf("Minimun Distance is %d", arr[str1.length()][str2.length()]);
        // Display(arr);



    }
    public static int Min(int a, int b, int c)
    {
        if(a <= b && a <= c)
            return a;
        
        if(b <= a && b <= c)
            return b;
        
        return c;
    }

    // public static void Display(int[][] arr)   
    // {
    //     System.out.printf("\n");
    //     for(int i=0;i<arr.length;i++)
    //     {
    //         for(int j=0;j<arr[0].length;j++)
    //         {
    //             System.out.printf("%d\t", arr[i][j]);
    //         }
    //         System.out.printf("\n");
    //     }
    //     System.out.printf("===========================");
     
    // }
}