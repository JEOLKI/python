package day11;

public class ThreadTest01 {
	public static void main(String[] args) {
		
		Thread a = new Thread() {
			@Override
			public void run() {
				try {
					Thread.sleep(5000);
				} catch (InterruptedException e) {
					e.printStackTrace();
				}
				System.out.println("hello");
			}
		};
		
		a.start();
		
		
	}
}
