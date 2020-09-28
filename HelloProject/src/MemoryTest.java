
public class MemoryTest {
	public static void main(String[] args) {
		
		// 메모리 영역을 나누어 줌으로 같은 이름의 변수를 사용 할 수 있다. 전역변수를 많이 사용하면 로드가 크다
		{
		int a = 1;
		System.out.println(a);
		}
		
		{
		int a = 1;
		System.out.println(a);
		}
		
	}
}
