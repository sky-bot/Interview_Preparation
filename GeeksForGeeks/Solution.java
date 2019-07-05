import java.io.*;
import java.util.*;

class Solution {
  
  static int bracketMatch(String text) {
      char[] str = text.toCharArray();
      char[] stack = new char[text.length()];
      int TOP=-1;
    
      for(int i=0;i<str.length;i++)
      {
          if(str[i]=='('){
              stack[++TOP]='(';
          }
          else if(str[i]==')')          
          {
                if(TOP==-1){
                    stack[++TOP]=')';
                    continue;    
                } 
                if(stack[TOP]=='('){
                    stack[TOP]='-';
                    TOP--;
                }
                else
                    stack[++TOP]=')';
          } 
      }
      int count=0;
      for(int i=0;i<str.length;i++)
          if(stack[i]=='(' || stack[i]==')')
              count++;
          else
              break;
      return count;
  }

  public static void main(String[] args) {
      String text = "()()";
      System.out.println(bracketMatch(text));
  }

}