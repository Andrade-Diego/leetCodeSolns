var removeElements = function(head, val) {
    //get rid of leading nodes with val===val
    while (head && head.val === val){
        head = head.next;
    }


    let i = head;
    let prev = new ListNode(null, i);
    while (i !== null){
       if (i.val === val){
           prev.next = i.next;
           i = i.next;
           continue;
        }
        prev = i;
        i = i.next;
    }
    return head;
};
