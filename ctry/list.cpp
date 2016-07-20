#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    class List{
    private:
    	typedef struct node{
    	    int data;
    	    node* next;
    	}* nodePtr;
    	
    	nodePtr head;
    	nodePtr curr;
    	nodePtr temp;
    public:
        List();
        void AddNode(int addData);
        void DeleteNode(int delData);
        void PrintList();
    }
}
List::List(){
    head = NULL;
    curr = NULL;
    temp = NULL;
}

void List::AddNode(int addData){
    nodePtr n = new node;// new pointer n points to new node
    n->next = NULL;
    n->data = addData;
    
    if(head != NULL){
        curr = head;
        while(curr->next != NULL){
            curr = curr->next;
        }
        curr->next = n;
    }
    else{
        head = n;
    }
}
