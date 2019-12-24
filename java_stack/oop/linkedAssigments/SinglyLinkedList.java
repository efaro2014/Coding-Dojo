public class SinglyLinkedList {
    public Node head;
    public SinglyLinkedList() {
        this.head = null;
        // your code here
    }
    // SLL methods go here. As a starter, we will show you how to add a node to the list.
    public void add(int value) {
        Node newNode = new Node(value);
        if(head == null) {
            head = newNode;
        } else {
            Node runner = head;
            while(runner.next != null) {
                runner = runner.next;
            }
            runner.next = newNode;
        }
    }    
    public void remove(){
        if (head == null){
            System.out.println("Nothing to remove");
        }
        else if (head.next == null){
            Node head = null;
        }
        else{
            Node runner = head;
            while(runner.next.next != null) {
                runner = runner.next;
            }
            runner.next = null;
        }
    }
    public void printValues(){
        if(head == null){
            System.out.println("No thing Body!! please add something first!");
        }
        else{
            Node runner = head;
            while(runner.next != null) {
                System.out.print(runner.value);
                runner = runner.next;
            }
        }
    }
  public int find(int val){
        Node runner = head;
        while (runner != null){
            if (runner.value == val){
                return runner.value;}
            else{
                runner = runner.next;
            }
            }
        Node empty = new Node(0);
        System.out.println("Value "+val+" not found.");
        return empty.value;
        }
    public void removeAt(int n){
        // Node runner = head;
         if(head == null){
            System.out.println("Nothing Body!! please add something first!");
        }
        else if(n ==0){
            head = head.next;
        }
        else{
            Node runner = head;
            int count = 0;
            while(count < (n-1)){
                runner = runner.next;
                count = count + 1;
            }
            runner.next = runner.next.next;
        }
    }
}