import java.util.HashMap;

class Node{
    final private int key, val;
    Node prev, next;
    public Node(int key, int val){
        this.key = key;
        this.val = val;
        prev = next = null;
    }
    public int getKey(){
        return key;
    }

    public int getVal() {
        return val;
    }
}

class LRUCache {
    private final int capacity;
    HashMap<Integer, Node> cache;
    Node left, right;


    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new HashMap<>();
        left = new Node(0, 0);
        right = new Node(0, 0);
        this.left.next = this.right;
        this.right.prev = this.left;
    }

    public void insert(Node node){
        node.next = this.right;
        node.prev = this.right.prev;
        this.right.prev.next = node;
        this.right.prev = node;
    }

    public void remove(Node node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }


    public int get(int key) {
        if(cache.containsKey(key)){
            remove(cache.get(key));
            insert(cache.get(key));
            return cache.get(key).getVal();
        }
        return -1;
    }

    public void put(int key, int val) {
        if(cache.containsKey(key)){
            remove(cache.get(key));
        }
        cache.put(key, new Node(key, val));
        insert(cache.get(key));

        if(cache.size() > capacity){
            Node lru = this.left.next;
            remove(lru);
            cache.remove(lru.getKey());
        }
    }
}