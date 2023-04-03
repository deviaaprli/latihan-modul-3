package latihan2;

import java.util.LinkedList;
import java.util.Queue;

public class MainQueue {
    public void queueExample(){
        Queue queue = new LinkedList();
        queue.add("Java");
        queue.add("DotNet");
        queue.offer("PHP");
        queue.offer("HTML");
        System.out.println("Remove : " +queue.remove());
        System.out.println("elemet : " +queue.element());
        System.out.println("poll : " +queue.poll());
        System.out.println("peek : " +queue.peek());
    }

    public static void main(String[] args) {
        new MainQueue().queueExample();
    }
}
