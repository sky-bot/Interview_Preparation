import java.util.*;
import java.io.*;
import java.lang.*;

class optimizedSol
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter Your number");
        int target = Integer.parseInt(br.readLine());
        int num=0,count=0;

        while(target!=0)
        {
            if(target%2==0)
            {
                target= target/2;
                count++;
            }
            else
            {
                target--;
                count++;
            }
        }
        System.out.printf("result= %d",count);
    }
}