class Q9
{
    public static void main(String s[])
    {
        int arr[] = new int[800];
        for(int i=0;i<800;i++)
            arr[i]=i*i;

        for (int i = 800-1; i >= 2; i--) 
        { 
      
        int l = 0; 
        int r = i-1; 
        while (l < r) 
        { 
            // A triplet found 
            if (arr[l] + arr[r] == arr[i] && l+r+i==1000){
                System.out.printf("%d\t%d\t%d\t",l,r,i);
                break;
            } 
                
  
            // Else either move 'l' or 'r' 
            if(arr[l] + arr[r] < arr[i])
                l++;
            else
                r--; 
        } 
    } 
    }
}