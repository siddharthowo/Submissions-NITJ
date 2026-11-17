class Node:
    def __init__(self, key):
        self.data=key
        self.right=None
        self.left=None
        self.height=0

class AVL():
    def get_height(self,node):
        return node.height if node else -1

    def get_balance(self,node):
        if not node:
            return 0    
        return self.get_height(node.left)-self.get_height(node.right)
    
    def right_rot(self,z):
        x=z.left
        x_TR=x.right
        x.right=z
        z.left=x_TR

        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))

        return x

    def left_rot(self,z):
        x=z.right
        x_TL=x.left
        x.left=z
        z.right=x_TL

        z.height=1+max(self.get_height(z.left),self.get_height(z.right))
        x.height=1+max(self.get_height(x.left),self.get_height(x.right))

        return x

    def insert(self,root,key):
        if root==None:
            return Node(key)
        elif root.data>key:
            root.left=self.insert(root.left,key)
        elif root.data<key:
            root.right=self.insert(root.right,key)
        else:
            return root

        root.height=1+max(self.get_height(root.left),self.get_height(root.right))
        balance=self.get_balance(root)

        if balance>1 and key<root.left.data:
            return self.right_rot(root)
        if balance>1 and key>root.left.data:
            root.left=self.left_rot(root.left)
            return self.right_rot(root)
        if balance<-1 and key<root.right.data:
            root.right=self.right_rot(root.right)
            return self.left_rot(root)
        if balance<-1 and key>root.right.data:
            return self.left_rot(root)

        return root

    def inorder_succ(self,node):
        x=node
        while(x.left):
            x=x.left
        return x

    def delete(self,root,key):
        if not root:
            return root
        elif key<root.data:
            root.left=self.delete(root.left,key)
        elif key>root.data:
            root.right=self.delete(root.right,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp=self.inorder_succ(root.right)
            root.data=temp.data
            root.right=self.delete(root.right,temp.data)
        
        root.height=1+max(self.get_height(root.left), self.get_height(root.right))
        balance=self.get_balance(root)
        
        if balance>1 and self.get_balance(root.left)>=0:
            return self.right_rot(root)
        if balance>1 and self.get_balance(root.left)<0:
            root.left=self.left_rot(root.left)
            return self.right_rot(root)
        if balance<-1 and self.get_balance(root.right)<=0:
            return self.left_rot(root)
        if balance<-1 and self.get_balance(root.right)>0:
            root.right=self.right_rot(root.right)
            return self.left_rot(root)
        
        return root

    def inorder_trav(self,root):
        if root:
            self.inorder_trav(root.left)
            print(root.data,end="->")
            self.inorder_trav(root.right)

avl=AVL()
l=[3,6,1,2,8,9,77,5,22,17,89,66,34]
root=None
for i in l:
    root=avl.insert(root,i)

avl.inorder_trav(root)
avl.delete(root,22)
avl.delete(root,17)
avl.delete(root,34)
print("\n")
avl.inorder_trav(root)