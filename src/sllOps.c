#include <stdio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *next;
}*head,*p,*new;
void printList(struct node *head) {
    struct node *temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
}
void solve(struct node *head)
{
    int ind,val;
    scanf("%d", &ind);
    scanf("%d", &val);
        if(ind == 0){
            struct node *temp = (struct node *)malloc(sizeof(struct node));
            temp->data = val;
            temp->next = head;
            head = temp;
        }
        else if(ind == -1){
            //insert in middle
            struct node *slow = head, *fast = head, *loc = head;
            while(fast != NULL && fast->next != NULL){
                loc = slow;
                slow = slow->next;
                fast = fast->next->next;
            }
            struct node *temp = (struct node *)malloc(sizeof(struct node));
            temp->data = val;
            temp->next = slow;
            loc->next = temp;
        }
        else if(ind == 1){
            //insert at end
            struct node *temp = (struct node *)malloc(sizeof(struct node));
            temp->data = val;
            temp->next = NULL;
            if(head == NULL){
                head = temp;
            }
            else{
                struct node *last = head;
                while(last->next != NULL){
                    last = last->next;
                }
                last->next = temp;
            }
        }
        printList(head);
}
int main()
{
    int n,i;
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        int v;
        scanf("%d",&v);
        if(head==NULL)
        {
            head=(struct node*)malloc(sizeof(struct node));
            p=head;
            head->next=NULL;
            p->data=v;
        }
        else
        {
            new=(struct node*)malloc(sizeof(struct node));
            new->data=v;
            new->next=NULL;
            p->next=new;
            p=new;
        }
    }
    
    solve(head);
        return 0;
}
