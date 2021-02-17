var removeNthFromEnd = function(head, n) {
   let ahead = head;
   let behind = head;
   let prev = new ListNode(val = null, next = behind);
   let newHead = prev;

   // make ahead lead by n;
   for (let i = 0; i < n; i ++){
       ahead = ahead.next;
   }


   while(1){
       if (ahead == null){
           prev.next = behind.next;
           return newHead.next;
       }
       ahead = ahead.next;
       prev = prev.next;
       behind = behind.next;

   }
};
