package day09;

import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import java.awt.Color;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

public class Tetris02 extends JFrame {

	private JPanel contentPane;

	public int[][] block2D = new int[20][10];
	public int[][] stack2D = new int[20][10];
	public int[][] scrin2D = new int[20][10];

	public Block block = new Block();
	
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					Tetris02 frame = new Tetris02();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	public Tetris02() {
		addKeyListener(new KeyAdapter() {
			@Override
			public void keyPressed(KeyEvent e) {
				myPress(e);
			}
		});

		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 265, 538);
		contentPane = new JPanel();
		contentPane.setBackground(new Color(192, 192, 192));
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);

		setBlock2DWithBlock();
		
		stack2D[19][0] = 11;
		stack2D[19][1] = 11;
		stack2D[19][2] = 11;
		stack2D[19][3] = 11;

		for (int i = 0; i < 20; i++) {
			for (int j = 0; j < 10; j++) {

				JLabel lbl = new JLabel("");
				lbl.setBackground(new Color(0, 100, 150));
				lbl.setBounds((j * 25), (i * 25), 24, 24);
				lbl.setOpaque(true); 
				contentPane.add(lbl);

			}
		}

		System.out.println(block);
		
		printBlock2D();
		printStack2D();

	}

	public void myPress(KeyEvent e) {

		int keycode = e.getKeyCode();
		
		// 38:ю╖, 40:╢ы©Н, 37:аб, 39:©Л
		if (keycode == 38) {

		}
		if (keycode == 40) {
			block.i++;
		}
		if (keycode == 37) {
			block.j--;
		}
		if (keycode == 39) {
			block.j++;
		}
		setBlock2DWithBlock();
		printBlock2D();
		
	}

	public void setBlock2DWithBlock() {
		for (int i = 0; i < block2D.length; i++) {
			for (int j = 0; j < block2D[i].length; j++) {
				block2D[i][j] = 0;
			}
		}
		block2D[block.i-1][block.j] = block.kind;
		block2D[block.i][block.j] = block.kind;
		block2D[block.i+1][block.j] = block.kind;
		block2D[block.i+1][block.j-1] = block.kind;
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

	public void printBlock2D() {
		System.out.println("---------------------------block2D");
		for (int i = 0; i < block2D.length; i++) {
			for (int j = 0; j < block2D[i].length; j++) {
				System.out.print(block2D[i][j]);
			}
			System.out.println();
		}
	}

}
