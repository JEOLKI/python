package day03;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MyFrame03 extends JFrame {

	private JPanel contentPane;
	private JTextField num1;
	private JTextField num2;
	private JTextField result;

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					MyFrame03 frame = new MyFrame03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
			
		});
	}

	public MyFrame03() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		num1 = new JTextField();
		num1.setBounds(48, 116, 71, 21);
		contentPane.add(num1);
		num1.setColumns(10);
		
		JLabel lbl = new JLabel("+");
		lbl.setBounds(131, 119, 11, 15);
		contentPane.add(lbl);
		
		num2 = new JTextField();
		num2.setBounds(154, 116, 71, 21);
		contentPane.add(num2);
		num2.setColumns(10);
		
		JButton btn = new JButton("=");
		btn.addMouseListener(new MouseAdapter() {
			
			@Override
			public void mouseClicked(MouseEvent e) {
				
				int x = Integer.parseInt(num1.getText());
				int y = Integer.parseInt(num2.getText());
				
				result.setText(Integer.toString(x+y));
				
			}
			
		});
		btn.setBounds(237, 115, 50, 23);
		contentPane.add(btn);
		
		result = new JTextField();
		result.setText("");
		result.setBounds(299, 116, 71, 21);
		contentPane.add(result);
		result.setColumns(10);
	}
}
