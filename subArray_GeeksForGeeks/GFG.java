/*package whatever //do not write package name here */

import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int t = Integer.parseInt(br.readLine());
		int k=0,flag=0,pos=-1;
		
		while(k<t)
		{
		    int n= Integer.parseInt(br.readLine());
		    String[] s=br.readLine().split(" ");
		    int ar[] = new int[n];
		    
		    for(int i=0;i<n;i++)
		        ar[i]=Integer.parseInt(s[i]);
		    if(ar.length==1)
		    {
		    	System.out.printf("%d",ar.length);
		    	continue;
		    }
			
		    int leftSum=0, rightSum=0;    
		          
		    for(int i=0;i<n;i++)
		    {
		        leftSum = leftSum + ar[i];
		        for(int j=n-1;j>i+1;j--)
		        {
		            rightSum = rightSum + ar[j];
		            if(rightSum>leftSum)
		                continue;
		                
		            if(rightSum==leftSum && (i+1) == (j-1))
		            {
		                flag=1;
		                pos =j;
		                break;
		            }
		        }

		        if(flag==1)
		        	break;

		        rightSum=0;
		    }
		    System.out.printf("%d\n",pos);
		    k=k+1;
		}	pos = -1;	
	}
}















// import java.util.*;
// import java.lang.*;
// import java.io.*;

// class GFG {
// 	public static void main (String[] args) throws Exception {
// 		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
// 		int t = Integer.parseInt(br.readLine());
// 		int k=0;
		
// 		while(k<t)
// 		{
// 		    int n= Integer.parseInt(br.readLine());
// 		    String[] s=br.readLine().split(" ");
// 		    int ar[] = new int[n];
		    
// 		    for(int i=0;i<n;i++)
// 		        ar[i]=Integer.parseInt(s[i]);
		    
// 		    int leftSum=0, rightSum=0;    
		          
// 		    for(int i=0;i<n;i++)
// 		    {
// 		        leftSum = leftSum + ar[i];
// 		        for(int j=n-1;j>i+1;j--)
// 		        {
// 		            rightSum = rightSum + ar[j];
// 		            if(rightSum>leftSum)
// 		                continue;
		                
// 		            if(rightSum==leftSum)
// 		            {
// 		                System.out.printf("%d",j);
// 		                break;
// 		            }
// 		        }
// 		        rightSum=0;
// 		    }
// 		    k++;
// 		}		
// 	}
// }