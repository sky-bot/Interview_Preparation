class Q3
{
    public static void main(String ch[])
    {
        long a = 600851475143;
        int big=2,prime=0;

        for(int i=2;i<=a;i++)
        {
            for(int j=1;j<=i;j++)
            {
                if(i%j==0){
                     prime++;
                }       
            }

            if(prime==2)
            {
                if(a%i==0)
                    big=i;
            }
            prime=0;

        }
         System.out.printf("\n====================\n%d",big);
    }
}