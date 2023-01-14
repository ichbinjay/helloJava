//HEAD

#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "math.h"

//BODY

struct stackNode{
    int val;
    struct stackNode* next;
};
typedef struct stackNode stackNode;
stackNode* stackHead = NULL;// - Head Pointer for stack LinkedList
void push(int x){
    stackNode* newNode = (stackNode*)malloc(sizeof(stackNode));
    newNode->val = x;
    newNode->next = stackHead;
    stackHead = newNode;
    }// - Insert an element onto the top of the stack
int peek(){
    return stackHead->val;
}// - Return the topmost element of the stack
void pop(){
    stackNode* temp = stackHead;
    stackHead = stackHead->next;
    free(temp);
}// - Remove the topmost element of the stack
int empty(){
    if(stackHead == NULL) return 1;
    return 0;
}// - Return 1 if the stack is empty, 0 otherwise


//TAIL

int main()
{
    int n;
    stackHead = NULL;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        int t, x;
        scanf("%d", &t);
        if (t == 1) {
            scanf("%d", &x);
            push(x);
        }
        else if (t == 2) {
            if (empty()) {
                printf("Invalid\n");
            }
            else {
                pop();
            }
        }
        else if (t == 3){
            if (empty()) {
                printf("Invalid\n");
                continue;
            }
            stackNode* j = stackHead;
            while (j) {
                printf("%d ", j->val);
                j = j->next;
            }
            printf("\n");
        }
        else {
            if (empty()) {
                printf("Invalid\n");
                continue;
            }
            printf("%d\n", peek());
        }
    }
    return 0;
}