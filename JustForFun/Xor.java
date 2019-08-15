import java.util.*;
import java.io.*;
import java.util.*;
class Xor
{
    public static void main(String[] args)
    {
        int a=5,b=4,carry;

        // System.out.printf("a&b: %d\n", a&b );
        // System.out.printf("a|b: %d\n", a|b);
        // System.out.printf("a^b: %d\n", a^b);
        // System.out.printf("a>>1: %d\n",a>>1);
        // System.out.printf("b<<1: %d\n", b<<1);
        // System.out.printf("a<<2: %d\n",a<<2);
        // System.out.printf("b<<2: %d\n", b<<2);

        int count=0;
        while(b!=0)
        {
            System.out.printf("\nLoop %d\n", count++);
            System.out.printf("a: %d\tb: %d", a,b);
            carry = a&b;

            a = a^b;

            b = carry<<1;

            System.out.printf("\ncarry: %d\t",  carry);
            System.out.printf("Sum: %d\t", a);
            System.out.printf("b: %d\n",b);


        }

        System.out.printf("Sum is: %d\n", a);

        return;
    }
}