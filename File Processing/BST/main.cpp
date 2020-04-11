//
// Created by Sujin Kim
//
#include "BST.h"

using namespace std;

int main() {
    BST bst;
    Node *T;

    vector<int> v = {40, 11, 77, 33, 20, 90, 99, 70, 88, 80, 66, 10, 22, 30, 44, 55, 50, 60, 100};
    vector<int>::iterator it;
    vector<int>::reverse_iterator rit;

    // 삽입
    for (it = v.begin(); it != v.end(); it++) {
        T = bst.insertBST(bst.getRoot(), *it);
        cout << "insert " << *it << ": ";
        bst.inorderBST(bst.getRoot());
        cout << endl;
    }
    cout << endl;

    // 삭제1
    for (it = v.begin(); it != v.end(); it++) {
        T = bst.deleteBST(bst.getRoot(), *it);
        cout << "delete " << *it << ": ";
        bst.inorderBST(T);
        cout << endl;
    }
    cout << endl;

    T = 0;

    // 재삽입
    for (it = v.begin(); it != v.end(); it++) {
        T = bst.insertBST(bst.getRoot(), *it);
        cout << "insert " << *it << ": ";
        bst.inorderBST(T);
        cout << endl;
    }
    cout << endl;

    // 삭제2
    for (rit = v.rbegin(); rit != v.rend(); rit++) {
        T = bst.deleteBST(bst.getRoot(), *rit);
        cout << "delete " << *rit << ": ";
        bst.inorderBST(T);
        cout << endl;
    }
    cout << endl;
}
