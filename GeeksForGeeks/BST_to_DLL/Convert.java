import java.util.*;
import java.lang.*;
import java.io.*;

class Convert
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

    void inorder(Node root)
    {
        if(root != null)
        {
            inorder(root.left);
            System.out.printf("%d", root.key);
            inorder(root.right);
        }
    }

    Node GiveMeRoot()
    {
        return root;
    }
    
    public static void main(String[] args)
    {
        Convert tree = new Convert();
        tree.insert(5);
        tree.insert(3);
        tree.insert(2);
        tree.insert(4);
        tree.insert(1);
        tree.insert(8);
        tree.insert(9);

        Node root = tree.GiveMeRoot();

        System.out.printf("This is from the tree");
        tree.inorder(root);
        Node root1 = ChangeToTree(root,null);

        while(root1!=null)
        {
            System.out.printf("%d->>", root1.key);
            root1 = root1.left;
        }

        tree.inorder(root);
    }

    static Node ChangeToTree(Node present, Node up)
    {  
        

    

       



    
        
    }

}