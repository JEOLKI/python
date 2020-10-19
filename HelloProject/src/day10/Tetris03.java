package day10;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import javax.swing.JLabel;
import javax.swing.JOptionPane;

import java.awt.Color;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;
import java.util.ArrayList;

public class Tetris03 extends JFrame {

	private JPanel contentPane;
	private JLabel lblRow;
	private JLabel[][] lbl2D = new JLabel[20][10];
	private boolean flagIng = true; // true면 게임중
	
	public int[][] block2D = new int[20][10];
	public int[][] stack2D = new int[20][10];
	public int[][] scrin2D = new int[20][10];

	public Block block = new Block();

	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tetris03 frame = new Tetris03();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public Tetris03() {
		addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				myPress(e);
			}
		});

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 265, 575);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(0, 0, 0));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblDisp = new JLabel("\uC9C0\uC6CC\uC57C\uD560 \uD589 :");
		lblDisp.setForeground(Color.WHITE);
		lblDisp.setBounds(79, 511, 81, 15);
		contentPane.add(lblDisp);
		
		lblRow = new JLabel("10");
		lblRow.setForeground(Color.WHITE);
		lblRow.setBounds(158, 511, 39, 15);
		contentPane.add(lblRow);

		setBlock2DWithBlock();

		for (int i = 0; i < lbl2D.length; i++) {
			for (int j = 0; j < lbl2D[i].length; j++) {

				JLabel lbl = new JLabel("");
				lbl.setBackground(new Color(64, 64, 64));
				lbl.setBounds((j * 25), (i * 25), 24, 24);
				lbl.setOpaque(true);
				contentPane.add(lbl);
				lbl2D[i][j] = lbl;

			}
		}

		System.out.println(block);

		print2D(block2D);
		print2D(stack2D);

		new Thread() {
			@Override
			public void run() {
				
				while (true) {
					try {
						Thread.sleep(1000);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
					
					realPress(40);
				}
			}
		}.start();


	}

	public void myrender() {

		for (int i = 0; i < scrin2D.length; i++) {
			for (int j = 0; j < scrin2D[i].length; j++) {

				if (scrin2D[i][j] == 0) {
					lbl2D[i][j].setBackground(new Color(64, 64, 64));
				}
				if (scrin2D[i][j] == 1) {
					lbl2D[i][j].setBackground(new Color(255, 102, 102));
				}
				if (scrin2D[i][j] == 2) {
					lbl2D[i][j].setBackground(new Color(255, 178, 102));
				}
				if (scrin2D[i][j] == 3) {
					lbl2D[i][j].setBackground(new Color(255, 255, 102));
				}
				if (scrin2D[i][j] == 4) {
					lbl2D[i][j].setBackground(new Color(178, 255, 102));
				}
				if (scrin2D[i][j] == 5) {
					lbl2D[i][j].setBackground(new Color(102, 178, 102));
				}
				if (scrin2D[i][j] == 6) {
					lbl2D[i][j].setBackground(new Color(102, 102, 255));
				}
				if (scrin2D[i][j] == 7) {
					lbl2D[i][j].setBackground(new Color(102, 255, 255));
				}

				if (scrin2D[i][j] == 11) {
					lbl2D[i][j].setBackground(new Color(255, 204, 204));
				}
				if (scrin2D[i][j] == 12) {
					lbl2D[i][j].setBackground(new Color(255, 229, 204));
				}
				if (scrin2D[i][j] == 13) {
					lbl2D[i][j].setBackground(new Color(255, 255, 204));
				}
				if (scrin2D[i][j] == 14) {
					lbl2D[i][j].setBackground(new Color(229, 255, 204));
				}
				if (scrin2D[i][j] == 15) {
					lbl2D[i][j].setBackground(new Color(204, 255, 204));
				}
				if (scrin2D[i][j] == 16) {
					lbl2D[i][j].setBackground(new Color(204, 204, 255));
				}
				if (scrin2D[i][j] == 17) {
					lbl2D[i][j].setBackground(new Color(204, 255, 255));
				}
			}
		}
	}

	public void moveStackBlock2Scrin() {
		for (int i = 0; i < scrin2D.length; i++) {
			for (int j = 0; j < scrin2D[i].length; j++) {
				scrin2D[i][j] = stack2D[i][j] + block2D[i][j];
			}
		}
	}

	public void myPress(KeyEvent e) {
		realPress(e.getKeyCode());
	}
	
	public void realPress(int keycode) {
		
		if(!flagIng) {
			return;
		}

		// 벽과 충돌을 판별
		boolean flag_col_bound = false;

		// 방향키 아래 눌렀을때의 충돌체크
		boolean flag_down = false;

		// 충돌전의 값을 저장
		int pre_status = block.status;
		int pre_i = block.i;
		int pre_j = block.j;

		// 38:위, 40:다운, 37:좌, 39:우
		if (keycode == 38) {
			changeBlockStatus();
		}
		if (keycode == 40) {
			block.i++;
			flag_down = true;
		}
		if (keycode == 37) {
			block.j--;
		}
		if (keycode == 39) {
			block.j++;
		}

		System.out.println(block);

		try {
			setBlock2DWithBlock();
		} catch (Exception e2) {
			flag_col_bound = true;
		}

		moveStackBlock2Scrin();

		boolean flag_collision = isCollision();
		if (flag_collision || flag_col_bound) {
			block.status = pre_status;
			block.i = pre_i;
			block.j = pre_j;
			setBlock2DWithBlock();
			moveStackBlock2Scrin();

			// 블록끼리 충돌하면
			if (flag_down) {
				moveBlock2Stack();
				
				// 사라지고 난후의 배열 
				// ArrayList : 큐와 스택모두가능 , String : value값 정확한값으로 운용하기 위해
				ArrayList<String> notFullStack = getNotFullStack();
				
				// 사라질 층의 갯수 구하기
				int cnt10 = 20 - notFullStack.size();

				int cnt = Integer.parseInt(lblRow.getText());
				int cnt_setting = cnt - cnt10;
				
				if(cnt_setting<=0) {
					JOptionPane.showMessageDialog(null, "clear");
					flagIng = false;
					return;
				}
				
				if (
						stack2D[5][0] > 0 ||
						stack2D[5][1] > 0 ||
						stack2D[5][2] > 0 ||
						stack2D[5][3] > 0 ||
						stack2D[5][4] > 0 ||
						
						stack2D[5][5] > 0 ||
						stack2D[5][6] > 0 ||
						stack2D[5][7] > 0 ||
						stack2D[5][8] > 0 ||
						stack2D[5][9] > 0 
						) {

					JOptionPane.showMessageDialog(null, "gameover");
					flagIng = false;
					return;
				}
				
				
				lblRow.setText( cnt_setting + "");

				System.out.println("cnt10 : " + cnt10);
				
				// 사라진 층 수 만큼 notFullStack의 위쪽으로 삽입
				for (int i = 0; i < cnt10; i++) {
					notFullStack.add(0, "0,0,0,0,0,0,0,0,0,0");
				}
				
				// notFullstack을 stack2D에 대입
				for (int i = 0; i < notFullStack.size(); i++) {
					String line = notFullStack.get(i);
					String[] data = line.split(",");
					
					stack2D[i][0] = Integer.parseInt(data[0]);
					stack2D[i][1] = Integer.parseInt(data[1]);
					stack2D[i][2] = Integer.parseInt(data[2]);
					stack2D[i][3] = Integer.parseInt(data[3]);
					stack2D[i][4] = Integer.parseInt(data[4]);
					
					stack2D[i][5] = Integer.parseInt(data[5]);
					stack2D[i][6] = Integer.parseInt(data[6]);
					stack2D[i][7] = Integer.parseInt(data[7]);
					stack2D[i][8] = Integer.parseInt(data[8]);
					stack2D[i][9] = Integer.parseInt(data[9]);
				}
				
				block.init();
				setBlock2DWithBlock();
				moveStackBlock2Scrin();

			}

		}

		System.out.println("flag_collision : " + flag_collision);
		System.out.println("flag_col_bound : " + flag_col_bound);

		myrender();

		print2D(scrin2D);
		
	}
	
	/**
	 *  완성된 열이 사라진 후의 배열구하기
	 */
	public ArrayList<String> getNotFullStack() {
		ArrayList<String> stack_temp = new ArrayList<String>();

		for (int i = 0; i < stack2D.length; i++) {
			int[] temp = stack2D[i];
			// 한줄이 꽉 차있으면 
			if (
				temp[0] > 0 &&
				temp[1] > 0 &&
				temp[2] > 0 &&
				temp[3] > 0 &&
				temp[4] > 0 &&
				temp[5] > 0 &&
				temp[6] > 0 &&
				temp[7] > 0 &&
				temp[8] > 0 &&
				temp[9] > 0 
					) {
			
			} 
			// 한줄이 꽉 차지 않았을때
			else {
				
				String str_line = temp[0] + "," +
								  temp[1] + "," + 
							      temp[2] + "," + 
							      temp[3] + "," + 
							      temp[4] + "," + 
							      temp[5] + "," + 
							      temp[6] + "," + 
							      temp[7] + "," + 
							      temp[8] + "," + 
							      temp[9];
				
				stack_temp.add(str_line);
			}

		}

		return stack_temp;

	}

	public void moveBlock2Stack() {
		for (int i = 0; i < block2D.length; i++) {
			for (int j = 0; j < block2D[i].length; j++) {

				if (block2D[i][j] > 0) {
					stack2D[i][j] = block2D[i][j] + 10;
				}

			}
		}

	}

	public boolean isCollision() {

		for (int i = 0; i < scrin2D.length; i++) {
			for (int j = 0; j < scrin2D[i].length; j++) {

				if (stack2D[i][j] > 0 && block2D[i][j] > 0) {
					return true;
				}
			}
		}

		return false;
	}

	public void changeBlockStatus() {
		if (block.kind == 1) {

		}
		if (block.kind == 2 || block.kind == 3 || block.kind == 4) {
			if (block.status == 1) {
				block.status = 2;
			} else if (block.status == 2) {
				block.status = 1;
			}
		}
		if (block.kind == 5 || block.kind == 6 || block.kind == 7) {
			if (block.status == 1) {
				block.status = 2;
			} else if (block.status == 2) {
				block.status = 3;
			} else if (block.status == 3) {
				block.status = 4;
			} else if (block.status == 4) {
				block.status = 1;
			}
		}
	}

	public void setBlock2DWithBlock() {
		for (int i = 0; i < block2D.length; i++) {
			for (int j = 0; j < block2D[i].length; j++) {
				block2D[i][j] = 0;
			}
		}

		if (block.kind == 1) {
			block2D[block.i][block.j] = block.kind;
			block2D[block.i][block.j + 1] = block.kind;
			block2D[block.i + 1][block.j] = block.kind;
			block2D[block.i + 1][block.j + 1] = block.kind;
		}

		if (block.kind == 2) {
			if (block.status == 1) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
				block2D[block.i + 2][block.j] = block.kind;
			}
			if (block.status == 2) {
				block2D[block.i][block.j - 2] = block.kind;
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
			}
		}

		if (block.kind == 3) {
			if (block.status == 1) {
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
				block2D[block.i + 1][block.j + 1] = block.kind;
			}
			if (block.status == 2) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i + 1][block.j - 1] = block.kind;
			}
		}

		if (block.kind == 4) {
			if (block.status == 1) {
				block2D[block.i][block.j + 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
				block2D[block.i + 1][block.j - 1] = block.kind;
			}
			if (block.status == 2) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
				block2D[block.i + 1][block.j + 1] = block.kind;
			}
		}

		if (block.kind == 5) {
			if (block.status == 1) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
			}
			if (block.status == 2) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
			}
			if (block.status == 3) {
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
			}
			if (block.status == 4) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
			}
		}

		if (block.kind == 6) {
			if (block.status == 1) {
				block2D[block.i - 1][block.j - 1] = block.kind;
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
			}
			if (block.status == 2) {
				block2D[block.i - 1][block.j + 1] = block.kind;
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
			}
			if (block.status == 3) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
				block2D[block.i + 1][block.j + 1] = block.kind;
			}
			if (block.status == 4) {
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
				block2D[block.i + 1][block.j - 1] = block.kind;
			}
		}

		if (block.kind == 7) {
			if (block.status == 1) {
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
				block2D[block.i + 1][block.j - 1] = block.kind;
			}
			if (block.status == 2) {
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i - 1][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
			}
			if (block.status == 3) {
				block2D[block.i - 1][block.j + 1] = block.kind;
				block2D[block.i - 1][block.j] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i + 1][block.j] = block.kind;
			}
			if (block.status == 4) {
				block2D[block.i][block.j - 1] = block.kind;
				block2D[block.i][block.j] = block.kind;
				block2D[block.i][block.j + 1] = block.kind;
				block2D[block.i + 1][block.j + 1] = block.kind;
			}
		}
	}

	public void printStack2D() {
		System.out.println("---------------------------stack2D");
		for (int i = 0; i < stack2D.length; i++) {
			for (int j = 0; j < stack2D[i].length; j++) {
				System.out.print(stack2D[i][j]);
			}
			System.out.println();
		}
	}

	public void print2D(int[][] arr2D) {
		System.out.println("---------------------------");
		for (int i = 0; i < arr2D.length; i++) {
			for (int j = 0; j < arr2D[i].length; j++) {
				System.out.print(arr2D[i][j]);
			}
			System.out.println();
		}
	}

}
