package day03;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame01 extends JFrame {

	private JPanel contentPane;
	JLabel lbl;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() { // 쓰레드
				try {
					MyFrame01 frame = new MyFrame01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public MyFrame01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300); // size : x, y, width, height
		contentPane = new JPanel(); // JPanel // 화면 앞
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane); // JFrame의 속성
		contentPane.setLayout(null); // absolutlayout으로 변경시 
		
		lbl = new JLabel("hello");
		lbl.setBounds(27, 28, 114, 16);
		contentPane.add(lbl);
		
		JButton btnNewButton = new JButton("click");
		btnNewButton.addMouseListener(new MouseAdapter() {
			
			// 익명의 이너 클래스
			@Override
			public void mouseClicked(MouseEvent e) {
				
				lbl.setText("good morining");
				
			}
			
		});
		btnNewButton.setBounds(153, 25, 97, 23);
		contentPane.add(btnNewButton);
	}
	
}
