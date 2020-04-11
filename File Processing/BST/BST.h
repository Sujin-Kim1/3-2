//
// Created by Sujin Kim
//

#ifndef ALGORITHM_BST_H
#define ALGORITHM_BST_H

#include <vector>
#include <iostream>

class Node {
private:
    int key;
    Node *left;
    Node *right;
    Node();
    Node(int key);
    friend class BST;
};

class BST {
private:
    Node *root;
public:
    BST();

    void inorderBST(Node *T) const;  // inorder 로 노드의 key 출력

    int height(Node * T) const; // 노드의 height 반환
    int noNodes(Node * T) const; // 노드의 개수 반환

    Node *insertBST(Node * T, int newKey);
    Node *deleteBST(Node * T, int deleteKey);
    Node *maxNode(Node * T) const; // 가장 큰 key 를 갖는 노드 반환
    Node *minNode(Node * T) const; // 가장 작은 key 를 갖는 노드 반환
    Node *getRoot() const;

    void drawTree();
    void drawBSTree(Node *, int);
};


#endif //ALGORITHM_BST_H
