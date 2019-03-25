/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int l=0, t =Integer.parseInt(br.readLine());
        String s[];
        
		while(l<t)
		{
		    int len = Integer.parseInt(br.readLine());
		    s = br.readLine().split(" ");
		    int ar[]=new int[len];
		    for(int i=0;i<len;i++){
		        ar[i] = Integer.parseInt(s[i]);
		        ar[i] = ar[i]*ar[i];
		    }
		    
		    for(int i=0;i<len-2;i++)
		    {
		        for(int j=i+1;j<len-1;j++)
		        {
		            for(int k=len-1;k>j;k--)
		            {
		                if((ar[i]+ar[j])==ar[k])
		                {
		                    System.out.printf("Yes\n");
		                    return;
		                }      
		            }
		        }
		    }
		    
		    System.out.printf("No\n");
		    l++;
		}
	}
}