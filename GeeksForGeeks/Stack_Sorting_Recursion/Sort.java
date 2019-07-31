import java.util.*;
import java.lang.*;
import java.io.*;

class Sort
{
    public static void main(String args[])throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Integer> S = new Stack<>();
        
        System.out.print("Enter Your Element");
        String[] str = br.readLine().split(" ");


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
            S = Rev(S);

            S = Insert(S, x);
        }
        return S;
    }

    public static Stack<Integer> Insert(Stack<Integer> S, int x)
    {
        if(S.size()==0){
            S.push(x);
            return S;
        }

        if(x<S.peek())
        {
            int temp = S.peek();
            S.pop();
            S = Insert(S, x);
            S.push(temp);
        }
        
        else
            S.push(x);
            
        return S;
    }
}