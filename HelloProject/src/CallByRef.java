
public class CallByRef {

	public static void add(int a) {
		a++;
	}

	public static void addRef(int[] a) {
		a[0]++;
	}

	public static void main(String[] args) { // 엔트리포인트 : 프로그램이 들어오는 시점

		int a = 1;
		int[] b = { 3 };

		System.out.println("a : " + a);
		System.out.println("b : " + b[0]);
		
		add(a);
		addRef(b);

		System.out.println("a : " + a);
		System.out.println("b : " + b[0]);
		
	}

}
