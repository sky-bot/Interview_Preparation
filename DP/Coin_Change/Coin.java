import java.util.*;
import java.lang.*;
import java.io.*;

class Coin
{
    public static void main(String[] str)throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // System.out.print("Enter Your Sum");
        int target = 11 ;//Integer.parseInt(br.readLine());


        int[] coins = {0,1,2,4,5,6,8};
        int[][] arr = new int[coins.length][target+1];

        // System.out.printf("row: %d Col : %d\n",arr.length, arr[0].length);
        for(int i=0;i<arr.length;i++)
            for(int j=0;j<arr[0].length;j++){
                arr[i][j] = 0;
                if(i==0 || j==0)
                    arr[i][j]=0; 
            }
        arr[1][1]=0;
        // Display(arr);
        
        for(int i = 1; i < arr.length; i++)
            for(int j=0;j<arr[0].length; j++)
            {
                if(coins[i]<=j)
                {
    
                    arr[i][j] = arr[i][j - coins[i]] + 1;
                   
                }
                else
                {
                    // System.out.printf("i= %d, j: %d\n", i, j);
                    arr[i][j] = arr[i-1][j];
                }
            }
            
        }

        System.out.printf("To make 11 we need %d minimum coin");
    }
    // public static void Display(int[][] arr)   For debugging purpose
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