package day10;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import javax.swing.JLabel;
import java.awt.Color;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Tetris03 extends JFrame {

	private JPanel contentPane;

	private JLabel[][] lbl2D = new JLabel[20][10];

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
		setBounds(100, 100, 265, 538);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(0, 0, 0));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

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

		// 벽과 충돌을 판별
		boolean flag_col_bound = false;

		// 방향키 아래 눌렀을때의 충돌체크
		boolean flag_down = false;

		// 충돌전의 값을 저장
		int pre_status = block.status;
		int pre_i = block.i;
		int pre_j = block.j;

		int keycode = e.getKeyCode();

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

	public void moveBlock2Stack() {
		for (int i = 0; i < block2D.length; i++) {
			for (int j = 0; j < block2D[i].length; j++) {

				if ( block2D[i][j] > 0 ) {
					stack2D[i][j] = block2D[i][j]+10;
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
