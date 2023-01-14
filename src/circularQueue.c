#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "math.h"

struct queueNode{
    int data;
    struct queueNode* next;
};
typedef struct queueNode queueNode;
queueNode* head = NULL;

queueNode* newNode(int val)
{
    queueNode* t = (queueNode*) malloc(sizeof(queueNode));
    t->data = val, t->next = NULL;
    return t;
}

//BODY

void push(int val)
{
    if(head == NULL)
    {
        head = newNode(val);
        head->next = head;
    }
    else
    {
        queueNode* t = head;
        while(t->next != head)
            t = t->next;
        t->next = newNode(val);
        t->next->next = head;
    }
}
void pop()
{
    if(head == NULL)
        return;
    else if(head->next == head)
    {
        free(head);
        head = NULL;
    }
    else
    {
        queueNode* t = head;
        while(t->next != head)
            t = t->next;
        t->next = head->next;
        free(head);
        head = t->next;   
    }
}
int top()
{
    return head->data;
}
int empty()
{
    return head == NULL;
}

// TAIL

int main()
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        char s[50];
        int x;
        scanf(" %s", s);
        if (s[0] == 't')
        {
            if (empty()) printf("Invalid\n");
            else                
                printf("%d\n", top());
        }
        else if (s[0] == 'p' && s[1] == 'o')
        {
            if (empty()) printf("Invalid\n");
            else    pop();
        }
        else
        {
            scanf(" %d", &x);
            push(x);
        }
    }
    return 0;
}