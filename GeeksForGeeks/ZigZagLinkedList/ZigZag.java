import java.util.*;
import java.lang.*;
import java.io.*;

class ZigZag
{
    class Node
    {
        int key;
        Node left, right;

        public Node(int item)
        {
            key = item;
            left = right = null;
        }
    }

    Node root;

    void BinarySearchTree(){
        root = null;
    }

    void insert(int key)
    {
        root = Insert(root, key);
    }

    Node Insert(Node root, int key)
    {
        if(root==null)
        {
            root = new Node(key);
            return root;
        }

        if(key<root.key)
            root.left = Insert(root.left, key);
        else
            root.right = Insert(root.right, key);

        return root;        
    }

    Node GiveMeRoot()
    {
        return root;
    }

    void inorder()
    {
        inorderRec(root);
    }

    void inorderRec(Node root)
    {
        if(root != null)
        {
            inorderRec(root.left);
            System.out.printf("%d", root.key);
            inorderRec(root.right);
        }
    }


    public static void main(String[] args)
    {
        ZigZag tree = new ZigZag();
        tree.insert(50);
        tree.insert(30);
        tree.insert(20);
        tree.insert(40);
        tree.insert(70);
        tree.insert(60);
        tree.insert(80);

        // tree.inorder();
        Node root = tree.GiveMeRoot();
        
        ZigZagPattern(root);
    }

    static void ZigZagPattern(Node root)
    {

        Stack<Node> S = new Stack<Node>();
        Queue<Node> Q = new LinkedList<Node>();
        S.add(root);

        int count=1;
        while(count<4)
        {
            if(count%2!=0)
            {
                while(S.size()!=0)
                {
                    Node temp = S.pop();
                    System.out.printf("%d-->",temp.key);
                    Q.add(temp.right);
                    Q.add(temp.left);
                }
            }
            else
            {
                while(Q.size()!=0)
                {
                    Node temp = Q.remove();
                    System.out.printf("%d-->",temp.key);
                    S.push(temp.right);
                    S.push(temp.left);
                }
            }
            count++;
        }
    }            
}