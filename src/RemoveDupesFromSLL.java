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

    public void sort(){
        SinglyLinkedList temp = head;
        while(temp != null){
            SinglyLinkedList temp2 = temp.next;
            while(temp2 != null){
                if(temp.data > temp2.data){
                    int tempData = temp.data;
                    temp.data = temp2.data;
                    temp2.data = tempData;
                }
                temp2 = temp2.next;
            }
            temp = temp.next;
        }
    }

    public void removeDuplicates(){
        SinglyLinkedList ptr = head;
        while(ptr.next != null){
            if(ptr.data == ptr.next.data) ptr.next = ptr.next.next;
            else ptr = ptr.next;
        }
    }
}

class removeDupesFromSLL {
    public static void main(String[]args){
        SinglyLinkedList sll = new SinglyLinkedList();
        sll.add(2);
        sll.add(3);
        sll.add(4);
        sll.add(1);
        sll.add(4);
        sll.add(5);
        sll.add(5);
        
        sll.print();    
        sll.sort();
        sll.print();
        sll.removeDuplicates();
        sll.print();
    }
}
