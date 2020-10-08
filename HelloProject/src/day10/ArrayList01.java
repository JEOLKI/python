package day10;

import java.util.ArrayList;

public class ArrayList01 {
	public static void main(String[] args) {
		
		ArrayList<String> arr = new ArrayList<>();
		
		arr.add("사과");
		arr.add("귤");
		arr.add("배");
		arr.add(0, "포도");
		
		for (int i = 0; i < arr.size(); i++) {
			System.out.println(arr.get(i));
		}
		
		
	}
}
