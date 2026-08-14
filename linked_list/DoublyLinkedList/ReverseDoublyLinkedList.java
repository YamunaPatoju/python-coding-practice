class Solution {
    public Node reverse(Node head) {
        Node curr = head;
        Node newHead = null;

        while (curr != null) {
            Node temp = curr.next;
            curr.next = curr.prev;
            curr.prev = temp;

            newHead = curr;
            curr = curr.prev;
        }

        return newHead;
    }
}
