import java.util.*;
import java.io.*;
class subarray
{
	public static void main(String c[]) throws Exception
	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		System.out.printf("Enter the length of Array");
		int len = Integer.parseInt(br.readLine());
		int ar[] = new int[len];
		System.out.printf("Enter the Array");
		for (int i=0;i<len ;i++ )
		{
			ar[i] = Integer.parseInt(br.readLine());	
		}
		System.out.printf("Enter the Target");
		int target = Integer.parseInt(br.readLine());
		int sum=0,flag=-1;

		for (int i=0;i<len-1 ;i++ ) 
		{
			sum = ar[i];
			for (int j=i+1;j<len ;j++ ) 
			{
				sum = sum + ar[j];
				if(sum==target)
				{
					System.out.printf("%d %d",i+1,j+1);
					flag=1;
					break;
				}

				if(sum>target)
					break;
			}
			if(flag==1)
				break;
		}
	}
}

