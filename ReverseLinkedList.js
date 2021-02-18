var reverseList = function(head) {
    let prev = null;
    let curr = head;
    while (curr != null) {
        let newHead = curr.next;
        curr.next = prev;
        prev = curr;
        curr = newHead;
    }
    return prev;
};
