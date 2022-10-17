class SinglyLinkedList{
    int data;
    SinglyLinkedList next;
    SinglyLinkedList head = null;

    public void add(int data){
        SinglyLinkedList newNode = new SinglyLinkedList();
        newNode.data = data;
        newNode.next = null;

        if(head == null){
            head = newNode;
        }
        else{
            SinglyLinkedList temp = head;
            while(temp.next != null){
                temp = temp.next;
            }
            temp.next = newNode;
        }
    }

    public void print(){
        SinglyLinkedList temp = head;
        while(temp != null){
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }
    public void reverse(){
        SinglyLinkedList prev = null;
        SinglyLinkedList current = head;
        SinglyLinkedList next = null;
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
        SinglyLinkedList sll = new SinglyLinkedList();
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
