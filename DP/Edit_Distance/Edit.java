import java.util.*;
import java.lang.*;
import java.io.*;

class Edit
{
    public static void main(String[] args)throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str1 = br.readLine();
        str2 = br.readLine();

        int[][] table = new int[str1.length()+1][str2.length()+1];

        table[0][0]=1;
        for(int i=0;i<str1.length();i++)
        {   
            for(int j=0;j<str2.length;j++)
            {
                if(i==0 && j!=0)
                    table[0][j] = table[0][j-1] + 1; 
            }
            table[i][0] = i;
        }
           


    }
}