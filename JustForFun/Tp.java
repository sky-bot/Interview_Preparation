import java.util.*;
import java.io.*;
import java.lang.*;

class Tp
{
    public static void main(String[] args)
    {
        int[] arr = {1,2,3,4,5,6};
        int a=10;
        fun(arr, a);
        System.out.println("arr: =" + arr[3]);
        System.out.printf("\na = %d",a);
    }

    public static void fun(int[] arr, int a)
    {
        arr[3]=0;
        a = 99;
    }
}
