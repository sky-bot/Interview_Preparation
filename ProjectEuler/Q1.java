class Q1
{
    public static void main(String c[])
    {
        int sum3=0, sum5=0, sumT=0;

        for(int i=3;i<1000;i++)
        {
            if(i%3==0)
                sum3= sum3 + i;
            
            if(i%5==0)
                sum5= sum5 + i;

            if(i%5==0 && i%3==0)
                sumT = sumT + i;
        }

        System.out.printf("%d",sum3+sum5-sumT);

    }
}