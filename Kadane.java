import java.lang.*;
import java.io.*;
import java.util.*;

class Kadane
{
	public static void main(String ch[]) throws Exception
	{
		int max_so_far=Integer.MIN_VALUE,max_ending=0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
 
		System.out.printf("Enter the length of your array: ");
		size = Integer.parseInt(br.readLine());
		int ar[] = new int[size];


		System.out.printf("Enter your Elements");
		for (int i;i<size ;i++ ) 
		{
			ar[i] = Integer.parseInt(br.readLine());	
		}


		for (int i=0;i<size ;i++ ) 
		{
			max_ending = max_ending + ar[i];
			if(max_ending>max_so_far)
				max_so_far = max_ending;

			if(max_ending<0)
				max_ending=0; 	
		}

		System.out.printf("%d",max_so_far);





	}
}