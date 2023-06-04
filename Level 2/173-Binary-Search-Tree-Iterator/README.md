# 173. Binary Search Tree Iterator

Problem Statement: Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):

BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
int next() Moves the pointer to the right, then returns the number at the pointer.
Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order traversal when next() is called.

![image](https://github.com/aryanv175/leetcode/assets/91381804/bc310303-6e43-4b7c-889c-d59e970460b9)

![image](https://github.com/aryanv175/leetcode/assets/91381804/40b5e785-89bc-428c-b95e-82e3ba954a92)
