/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int l=0,t = Integer.parseInt(br.readLine());
		int ans=-1;
		String s[];
		
		while(l<t)
		{
		    ans=-1;
		    int len = Integer.parseInt(br.readLine());
		    s = br.readLine().split(" ");
		    int ar[] = new int[len];
		    for(int i=0;i<len;i++)
		    {
		        ar[i] = Integer.parseInt(s[i]);
		    }
		    int max=ar[0];
		    
		    for(int i=1;i<len-1;i++)
		    {
		        if(ar[i]>max)
		        {
		            max=ar[i];
		            ans=ar[i];
		            for(int j=i+1;j<len;j++)
		            {
		                if(max>ar[j])
		                {
		                    ans=-1;
		                    break;
		                }
						
		            }
					if(ans!=-1)
						break;
		        }
		    }
		    System.out.printf("%d\n",ans);
		    l++;
		}
	}
}