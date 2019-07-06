import java.lang.*;
import java.util.*;
import java.io.*;

class nTable
{
    public static void main(String[] args)throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int upto = 20;
        int from = 1 ;
        table(n, upto, from);
        return;
    }

    public static void table(int n, int upto, int from)
    {   
        System.out.printf("%d * %d = %d\n", n, from, n*from);
        if(from==upto)
            return;
        else
            table(n, upto, from+1);
    }
}