class CircularLinkedList{
    CircularLinkedList head = null;
    CircularLinkedList next = null;
    CircularLinkedList tail = null;
    int data;

    public void insertStart(int data){
        CircularLinkedList node = new CircularLinkedList();
        node.data = data;
        if(head == null){
            head = node;
            tail = node;
            node.next = head;
        }
        else{
            node.next = head;
            head = node;
            tail.next = head;
        }
    }

    public void insertEnd(int data){
        CircularLinkedList node = new CircularLinkedList();
        node.data = data;
        if(head==null){
            head = tail = node;
            node.next = head;
        }
        else{
            tail.next = node;
            node.next = head;
            tail = node;
        }
    }
}

class CLL{
    public static void main(String[]args){
        CircularLinkedList cll = new CircularLinkedList();
        cll.insertStart(1);
        cll.insertStart(2);
        cll.insertStart(3);
        cll.insertEnd(4);
        cll.insertEnd(5);
        cll.insertEnd(6);

        CircularLinkedList temp = cll.head;
        do{
            System.out.print(temp.data+" ");
            temp = temp.next;
        }while(temp!=cll.head);
    }
}