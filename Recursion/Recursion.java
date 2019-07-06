import java.io.*;
import java.lang.*;
import java.util.*;

class Recursion
{
    public static void main(String args[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());

        System.out.printf("Sum is: %d\n",recurs(num));
    }
    public static int recurs(int num)
    {     
        return (num==0) ? 0 : ((num==1) ? 1: (num + recurs(num-1)));
    }
}