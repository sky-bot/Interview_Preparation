class Q6
{
    public static void main(String ch[])
    {
        double sum=0,sqSum=0;

        for(double i=1;i<101;i++)
        {
            sum = sum + i*i;
        }

        sqSum = (100*101)/2;

        System.out.printf("%f",(sqSum*sqSum)-sum);
    }
}