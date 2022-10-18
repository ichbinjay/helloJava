class SinglyLinkedList1{
    int data;
    SinglyLinkedList1 next;
    SinglyLinkedList1 head = null;

    public void add(int data){
        SinglyLinkedList1 newNode = new SinglyLinkedList1();
        newNode.data = data;
        newNode.next = null;

        if(head == null){
            head = newNode;
        }
        else{
            SinglyLinkedList1 temp = head;
            while(temp.next != null){
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    public void print(){
        SinglyLinkedList1 temp = head;
        while(temp != null){
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
    
    public void reverse(){
        SinglyLinkedList1 prev = null;
        SinglyLinkedList1 current = head;
        SinglyLinkedList1 next = null;
        while(current != null){
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }
}
public class reverseSLL {
    public static void main(String[]args){
        SinglyLinkedList1 sll = new SinglyLinkedList1();
        sll.add(1);
        sll.add(2);
        sll.add(3);
        sll.add(4);
        sll.add(5);
        
        sll.print();    
        sll.reverse();
        sll.print();
    }
}
