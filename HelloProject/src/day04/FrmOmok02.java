package day04;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.ImageIcon;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class FrmOmok02 extends JFrame {

	private boolean flagTurn = true;
	private JPanel contentPane;
	private JLabel[][] arr2d = new JLabel[10][10];
	private int[][] int2d = new int[10][10];
	private ImageIcon iie = new ImageIcon(FrmOmok02.class.getResource("/day04/0.jpg")); // 자주사용하는것 전역변수
	private ImageIcon iiw = new ImageIcon(FrmOmok02.class.getResource("/day04/1.jpg")); // 자주사용하는것 전역변수
	private ImageIcon iib = new ImageIcon(FrmOmok02.class.getResource("/day04/2.jpg")); // 자주사용하는것 전역변수

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FrmOmok02 frame = new FrmOmok02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public void showInt2d() {

		for (int i = 0; i < int2d.length; i++) {
			for (int j = 0; j < int2d[i].length; j++) {
				System.out.print(int2d[i][j]);
			}
			System.out.println();
		}

	}

	public void myRender() {

		for (int i = 0; i < int2d.length; i++) {
			for (int j = 0; j < int2d[i].length; j++) {

				if (int2d[i][j] == 0) {
					arr2d[i][j].setIcon(iie);

				} else if (int2d[i][j] == 1) {
					arr2d[i][j].setIcon(iiw);

				} else {
					arr2d[i][j].setIcon(iib);

				}
			}
		}

	}


	public FrmOmok02() {

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
				lbl.setText(i + "," + j);
				lbl.setBounds((j * 75), (i * 75), 75, 75);

				lbl.addMouseListener(new MouseAdapter() {
					@Override
					public void mouseClicked(MouseEvent e) {

						JLabel temp = (JLabel) e.getComponent();
						System.out.println(temp.getText());

						String a = temp.getText();

						String[] arr = a.split(",");

						int ii = Integer.parseInt(arr[0]);
						int jj = Integer.parseInt(arr[1]);

						if (int2d[ii][jj] > 0) {
							return;
						}
						
						int cnt_stone = 1;
						if (flagTurn) {
							int2d[ii][jj] = 1;
							cnt_stone = 1;
						} else {
							int2d[ii][jj] = 2;
							cnt_stone = 2;
						}

						myRender();
						
						int up_cnt = getUp(ii,jj,cnt_stone);
						System.out.println(up_cnt);
						flagTurn = !flagTurn;

					}

				});

				contentPane.add(lbl);
				arr2d[i][j] = lbl;

			}

		}

		showInt2d();
		myRender();

	}

	public int getUp(int ii, int jj, int cnt_stone) {
		int cnt = 0;
		
		int i = ii;
		int j = jj;
		
		while(true) {
			
			
			if(cnt_stone == int2d[i][j]) {
				cnt++;
				i--;
				j--;
			} else {
				break;
			}
		}
		
		return cnt;
	}

}
