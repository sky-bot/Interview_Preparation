import java.util.*;
import java.lang.*;
import java.io.*;

class Reverse
{
    public static void main(String args[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter Your Numbers");

        String[] str = br.readLine().split(" ");

        Stack<Integer> S = new Stack<>();
        for(int i=0;i<str.length;i++)
            S.push(Integer.parseInt(str[i]));
        
        S = Rev(S);

        System.out.print(S.pop());
        System.out.print(S.pop());
        System.out.print(S.pop());
        System.out.print(S.pop());
        
    }

    public static Stack<Integer> Rev(Stack<Integer> S)
    {
        if(S.size()>0)
        {
            int x = S.peek();
            S.pop();
            Rev(S);

            S = InsertElement(x,S);
            
            return S;
        }
        return S;
    }

    public static Stack<Integer> InsertElement(int x, Stack<Integer> S)
    {
        if(S.size()==0)
            S.push(x);
        else
        {
            int a = S.peek();
            S.pop();

            S = InsertElement(x,S);

            S.push(a);
        }
        return S;
    }

}