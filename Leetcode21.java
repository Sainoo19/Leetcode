import java.util.Collections;
import java.util.List;
import java.util.ArrayList;

public class Leetcode21 {

    // public List<Integer> mergeTwoLists(List<Integer> list1, List<Integer> list2)
    // {
    // List<Integer> resultList = new ArrayList<Integer>();;
    // if (list1 == null && list2 == null) {
    // return resultList;
    // }
    // else if (list1 == null ) {
    // Collections.sort(list2);
    // resultList = list2;
    // }
    // else if (list2 == null ) {
    // Collections.sort(list1);
    // resultList = list1;
    // }
    // else{
    // resultList.addAll(list1);
    // resultList.addAll(list2);
    // Collections.sort(resultList);

    // }

    // return resultList;
    // }

    public class ListNode {
        int val;
        ListNode next;

        ListNode() {
        }

        ListNode(int val) {
            this.val = val;
        }

        ListNode(int val, ListNode next) {
            this.val = val;
            this.next = next;
        }
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        // Tạo một node giả để bắt đầu danh sách gộp
        ListNode dummy = new ListNode(-1);
        ListNode current = dummy;

        // Duyệt qua cả hai danh sách
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                current.next = list1; // Thêm node từ list1 vào danh sách gộp
                list1 = list1.next; // Di chuyển con trỏ list1
            } else {
                current.next = list2; // Thêm node từ list2 vào danh sách gộp
                list2 = list2.next; // Di chuyển con trỏ list2
            }
            current = current.next; // Di chuyển con trỏ current đến node mới
        }

        // Một trong hai danh sách đã hết node
        // Thêm trực tiếp danh sách còn lại vào danh sách gộp
        if (list1 != null) {
            current.next = list1;
        } else {
            current.next = list2;
        }

        // Trả về danh sách gộp bắt đầu từ dummy.next
        return dummy.next;
    }

    public static void main(String[] args) {

    }
}
