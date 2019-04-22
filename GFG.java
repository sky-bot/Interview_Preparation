class GFG
{
    public static void main(String s[]) throws Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int len = Integer.parseInt(br.readLine());
        int arr[] = new int[len];
        String s[] = br.readLine().split(" ");
        int once=0,zeros=0;

        for(int i=0;i<len;i++)
        {
            arr[i]=Integer.parseInt(s[i]);
            if(arr[i]==0){
                arr[i]=-1;
                zeros++;
            }else
                once++;        
        }

        for(int i=0;i<len;i++)
        {
            for(int j=0;j<len;j++)
            {
                
            }
        }


    }
} 