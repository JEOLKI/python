package day09;

/**
 * @author PC-01
 *
 */
public class Block {
	
	
	public int kind = 1;
	public int status = 1;
	public int i = 1;
	public int j = 5;
	
	public Block() {

	}
	
	public Block(int kind) {
		this.kind = kind;
	}

	@Override
	public String toString() {
		return "Block [kind=" + kind + ", status=" + status + ", i=" + i + ", j=" + j + "]";
	}

}
