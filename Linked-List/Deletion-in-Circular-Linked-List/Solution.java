class Solution {
    Node deleteNode(Node head, int key) {
        if (head == null) {
            return null;
        }

        if (head.data == key) {
            if (head.next == head) {
                return null;
            }

            Node last = head;
            while (last.next != head) {
                last = last.next;
            }

            last.next = head.next;
            return head.next;
        }

        Node prev = head;
        Node curr = head.next;

        while (curr != head) {
            if (curr.data == key) {
                prev.next = curr.next;
                return head;
            }

            prev = curr;
            curr = curr.next;
        }

        return head;
    }
}
