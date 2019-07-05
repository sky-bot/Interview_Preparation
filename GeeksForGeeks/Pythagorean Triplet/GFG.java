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
		    for(int i=0;i<len;i++)
		    {
		        ar[i] = Integer.parseInt(s[i]);
		        ar[i] = ar[i]*ar[i];
		    }
		    Arrays.sort(ar);
		    int flag=0;
		    int c=0;
		    for(int i=ar.length-1;i>1;i--)
		    {   
		        c = ar[i];
		        int j=0,k=i-1;
		        while(j<k)
		        {
		            int sum = ar[j] + ar[k];
		            if(sum==c)
		            {
		            	flag=1;
		                System.out.printf("Yes\n");
		                break;		                
		            }
		            else if(sum>c)
		                k--;
		            else
		                j++;
		        }
		        if(flag==1)
		        	break; 
		    }
		    if(flag==0)
		    	System.out.printf("No\n");
		   
			l++;
		}
	}
}