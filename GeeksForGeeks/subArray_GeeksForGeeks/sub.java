import java.util.*;
import java.lang.*;
import java.io.*;



class sub
{
	public static void main(String c[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.printf("Enter Your No. of test cases: ");
		int t = Integer.parseInt(br.readLine());
		int k=0;

		while(k<t)
		{
			System.out.printf("Enter your length: ");
			int len = Integer.parseInt(br.readLine());
			int ar[] = new int[len];
			int sum[] = new int[len];

			for (int i=0;i<len ;i++ ) {
				ar[i]=Integer.parseInt(br.readLine());
				sum[i]=ar[i];
			}


			for (int i=1;i<len ;i++ ) 
			{
				for (int j=0;j<i ;j++ ) 
				{
					if(ar[j]<ar[i])
						sum[i]=sum[i]+ar[j];
				}
			}

			int max=sum[0];
			for (int i=1;i<len ;i++ ) {
				System.out.printf("%d   ",sum[i]); 
				if(max<sum[i])
					max = sum[i];
			}

			System.out.printf("\nOutput: %d",max);

			k++;
		}
	}
}