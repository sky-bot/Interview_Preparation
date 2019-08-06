import java.util.*;
import java.lang.*;
import java.io.*;

class Stairs
{
    public static void main(String[] args)throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        int[] arr = new int[s.length];

        for(int i=0;i<s.length;i++)
            arr[i] = Integer.parseInt(s[i]);

        int OneStep = Min(arr, -1, 0);

        System.out.printf("%d", OneStep);
        return;
    }

    public static int Min(int[] arr, int index, int sum)
    {
        if(index==arr.length)return sum;
        int OneStep, SecStep;
        if(index+1>=arr.length)
            OneStep = sum;
        else
            OneStep = Min(arr, index+1, sum+arr[index+1]);

        if(index+2>=arr.length)
                SecStep = sum;
        else
            SecStep = Min(arr, index+2, sum+arr[index+2]);

        return OneStep < SecStep ? OneStep : SecStep ;
    }





}