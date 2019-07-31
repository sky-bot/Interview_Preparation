import java.util.*;
import java.io.*;
import java.lang.*;

class Mini
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter Your number");
        int target = Integer.parseInt(br.readLine());
        int num=0,count=0;

        int result = fun(target, num, count);

        System.out.println(result);
    }

    public static int fun(int target, int num, int count)
    {
        if(num==target)
            return count;

        if(num>target|| count==target)return 100000;
        
        int plus=fun(target, num+1, count+1);
        int mul = fun(target, num*2, count+1); 
        
        if(plus<mul)
            return plus;
        else
            return mul;
    }
}