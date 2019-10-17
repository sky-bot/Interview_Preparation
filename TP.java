import java.util.*;
import java.io.*;
import java.lang.*;

class TP
{
    public static void main(String[] args)throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        System.out.printf("Enter Your String: ");
        char[] str = br.readLine().toCharArray();
        for(int i=0;i<str.length;i++)
            System.out.printf("%c", str[i]);
        int count = 0;
        int flag=0,first=0,last=0;

        System.out.printf("Enter your char: ");
        char[] target = br.readLine().toCharArray();

        for(int i=0;i<str.length-1;i++)
        {
            if(str[i]==target[0])
            {
               findLast(str, i+1, target[0]);

            }
        
        }

    }

    public static void findLast(char[] str, int i, char target)
    {
        int count=0, white=0;

        for(int k=i;k<str.length;k++)
        {
            if(str[k]==' '){
                white++;
                continue;
            }
            count++;
            if(str[k]==target)
            {
                System.out.printf("result: %d", (k - (i-1) - white) );
                break;
            }    
        }

    }
}