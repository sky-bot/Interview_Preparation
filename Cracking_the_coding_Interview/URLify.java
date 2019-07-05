// URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
// has sufficient space at the end to hold the additional characters, and that you are given the "true"
// length of the string. (Note: If implementing in Java, please use a character array so that you can
// perform this operation in place.)
import java.util.*;
import java.io.*;
import java.lang.*;
class URLify
{
    public static void main(String args[])throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] str = "My Smith John    ".toCharArray();
        System.out.println(str);
        int end=13;
        for(int i=0;i<end;i++)
        {
            if(str[i]==' '){
                str = rightShift(str,i);
                str = rightShift(str,i);
                str[i]='%';
                str[i+1]='2';
                str[i+2]='0';
                i=i+2;
            }
                
        }
        System.out.println(str);
        
    }
    public static char[] rightShift(char[] str, int i)
    {
        for(int j=str.length-1;j>i;j--)
            str[j]= str[j-1];
        return str;
    }

    
}