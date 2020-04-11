//
// Created by Sujin Kim
//

#include "BST.h"

using namespace std;

Node::Node()
        : key(0), left(0), right(0) {
}

Node::Node(int k)
        : key(k), left(0), right(0) {
}

BST::BST()
        : root(0) {
}

void BST::inorderBST(Node *T) const {
    if (T == 0)
        cout << "tree is empty" << endl;
    else {
        if (T->left != 0)
            inorderBST(T->left);
        cout << T->key << " ";
        if (T->right != 0)
            inorderBST(T->right);
    }
}

int BST::height(Node *T) const {
    Node *p = T;
    if (p) {
        int leftHeight = height(p->left);
        int rightHeight = height(p->right);
        if (leftHeight > rightHeight) return leftHeight + 1;
        return rightHeight + 1;
    }
    return 0;
}

int BST::noNodes(Node *T) const {
    Node *p = T;
    int num = 0;
    if (p) {
        num++;
        noNodes(p->left);
        noNodes(p->right);
    }
    return num;
}

Node *BST::insertBST(Node *T, int newKey) {
    // T 가 null 인 경우
    if (T == 0) {
        T = new Node(newKey);
        if (root == 0)
            root = T;
    } // newKey 가 더 작은 경우 왼쪽 트리로 이동
    else if (newKey < T->key) {
        T->left = insertBST(T->left, newKey);
    } // newKey 가 더 큰 경우 오른쪽 트리로 이동
    else if (newKey > T->key) {
        T->right = insertBST(T->right, newKey);
    }
    return T;
}

enum Flag {
    LEFT, RIGHT
};

Node *BST::deleteBST(Node *T, int deleteKey) {
    if (T) {
        // deleteKey 가 더 작은 경우 왼쪽 트리로 이동
        if (deleteKey < T->key) {
            T->left = deleteBST(T->left, deleteKey);
        } // deleteKey 가 더 큰 경우 오른쪽 트리로 이동
        else if (deleteKey > T->key) {
            T->right = deleteBST(T->right, deleteKey);
        } else if (T->left == 0 and T->right == 0) { // leaf node
            if (T == root) // 루트 노드밖에 없을 경우, 트리 삭제
                *&root = 0;
            T = 0;
        } else { // both child exists
            Node *p;
            Flag flag;
            // 왼쪽 트리의 height 가 높으면 왼쪽 하위트리의 max 값으로 대체
            if (height(T->left) > height(T->right)) {
                p = maxNode(T->left);
                flag = LEFT;
            } // 오른쪽 트리의 height 가 높으면 오른쪽 하위트리의 min 값으로 대체
            else if (height(T->left) < height(T->right)) {
                p = minNode(T->right);
                flag = RIGHT;
            } else {
                // height 가 같은 경우 노드 개수 많은 쪽에서 대체
                if (noNodes(T->left) >= noNodes(T->right)) {
                    p = maxNode(T->left);
                    flag = LEFT;
                } else {
                    p = minNode(T->right);
                    flag = RIGHT;
                }
            }
            T->key = p->key;
            if (flag == LEFT) T->left = deleteBST(T->left, T->key);
            else T->right = deleteBST(T->right, T->key);
        }
    }
    return T;
}

Node *BST::maxNode(Node *T) const {
    while (T->right)
        T = T->right;
    return T;
}

Node *BST::minNode(Node *T) const {
    while (T->left)
        T = T->left;
    return T;
}

Node *BST::getRoot() const {
    return root;
}

void BST::drawTree() { drawBSTree(root, 1); }

/* **********************************************************************
 * funtion : drawBSTtree(Node *p, int level)
 * description : BST를 출력한다.
 * variables : level - 트리의 level을 나타냄. level - 1만큼 공백을 추가하는
 *                     데 사용된다.
************************************************************************ */

void BST::drawBSTree(Node *p, int level) {
    if (p != 0 & level <= 7) {
        drawBSTree(p->right, level + 1);
        for (int i = 1; i <= level - 1; i++) {
            cout << "   ";
        }
        cout << p->key;
        if (p->left != 0 && p->right != 0) {
            cout << " <" << endl;
        }
        else if (p->right != 0) {
            cout << " /" << endl;
        }
        else if (p->left != 0) {
            cout << " \\" << endl;
        }
        else {
            cout << endl;
        }
        drawBSTree(p->left, level + 1);
    }
}