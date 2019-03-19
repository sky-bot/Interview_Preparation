/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG
{
	public static void main (String[] args) throws Exception 
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s[]; 
		int T = Integer.parseInt(br.readLine());
		int k=0;
		while(k<T)
		{   
		    int len = Integer.parseInt(br.readLine());
		    s = br.readLine().split(" ");
		    int sum=0,sumShouldBe=(len*(len+1))/2;
		    	
		    int ar[] = new int[len];
		    
		    
		    for(int i=0;i<len-1;i++)
		    {
		    	
		        ar[i] = Integer.parseInt(s[i]);
		        sum = sum + ar[i];
		    }
		   	
		    
		    System.out.printf("%d\n",sumShouldBe-sum);
		    k++;
		}
		
		
	}
}