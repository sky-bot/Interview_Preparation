// Find the number of islands | Set 1 (Using DFS)
// Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island. For example, the below matrix contains 5 islands

// Example:

// Input : mat[][] = {{1, 1, 0, 0, 0},
//                    {0, 1, 0, 0, 1},
//                    {1, 0, 0, 1, 1},
//                    {0, 0, 0, 0, 0},
//                    {1, 0, 1, 0, 1} 
// Output : 5

import java.util.*;
import java.io.*;
import java.lang.*;

class Max
{
    public static void main(String str[]) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter Your N");
        int row = Integer.parseInt(br.readLine());
        int col = row;

        //Intialization
        String s[];
        int mat[][] = new int[row][col];
        boolean visit[][] = new boolean[row][col];
        int count=0;
        System.out.println("Enter your Matrix");
        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                mat[i][j] = Integer.parseInt(br.readLine());
                visit[i][j] = false;
            }
        }

        for(int i=0;i<row;i++)
        {
            for(int j=0;j<col;j++)
            {
                if(mat[i][j]==1 && visit[i][j]==false)
                {
                    count++;
                    visit = dfs(mat, visit, i, j);
                }
            }
        }

        System.out.printf("\nNumber of region : %d", count); 

    }
    public static boolean[][] dfs(int mat[][], boolean visit[][], int row, int col)
    {
        if(row<0 || row==mat[0].length || col<0 || col==mat[0].length || visit[row][col]==true || mat[row][col]==0) return visit;

        visit[row][col] = true;
        visit = dfs(mat, visit, row, col+1);
        visit = dfs(mat, visit, row+1,col);
        visit = dfs(mat, visit, row, col-1);
        visit = dfs(mat, visit, row-1, col);

        return visit; 
        
    }
}
