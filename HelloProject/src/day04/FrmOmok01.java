package day04;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class FrmOmok01 extends JFrame {

	private JPanel contentPane;
	private JLabel[][] arr2d = new JLabel[10][10]; 
	private Integer[][] arrResult = new Integer[10][10];
	private ImageIcon iie = new ImageIcon(FrmOmok01.class.getResource("/day04/0.jpg")); // 자주사용하는것 전역변수
	private ImageIcon iiw = new ImageIcon(FrmOmok01.class.getResource("/day04/1.jpg")); // 자주사용하는것 전역변수
	private ImageIcon iib = new ImageIcon(FrmOmok01.class.getResource("/day04/2.jpg")); // 자주사용하는것 전역변수
	//private int count;
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrmOmok01 frame = new FrmOmok01();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public FrmOmok01() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 750, 750);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		
		for (int i = 0; i < arr2d.length; i++) { // i는 y축을 관여
			
			for (int j = 0; j < arr2d[i].length; j++) { // j는 x축을 관여
				
				JLabel lbl = new JLabel("New label");
				
				lbl.setIcon(iie);
				lbl.setText(i+","+j);
				lbl.setBounds((j*75), (i*75), 75, 75);
				
				//int y = i;
				//int x = j;
				
				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {
						
						JLabel temp = (JLabel) e.getComponent();
						System.out.println(temp.getText());
						
						/*if(count%2 != 1) {
							
							lbl.setIcon(iiw);
							arrResult[y][x] = 1;
							count += 1;
						} else {
							
							lbl.setIcon(iib);
							arrResult[y][x] = 2;
							count += 1;
						}*/
						
						
					}
					
				});
				
				
				contentPane.add(lbl);
				
				arr2d[i][j] = lbl;
				
				
			}
			
		}
		
	}
}
