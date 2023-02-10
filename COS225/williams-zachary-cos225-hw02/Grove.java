import java.util.ArrayList;

public class Grove {
	ArrayList<Tree> trees;
	String groveName;

	// Constructs an empty grove of trees.
	public Grove(String groveName) {
		this.groveName = groveName;
		trees = new ArrayList<Tree>();
	}

	// plants a tree and returns the id number of that tree.
	public int plantTree(Tree tree) {
		trees.add(tree);
		int x = tree.getIdNumber();
		return x;
	}
	
	// Removes a tree from the grove by idNumber.
	public int removeTree(int x) {
		for (int k = 0; k < trees.size(); k++) {
			Tree treeRemove = trees.get(k);
			if (treeRemove.getIdNumber() == x) {
				trees.remove(k);
				return treeRemove.getIdNumber();
			}
		}
		return 0;
	}
	
	// Prints count of trees in the grove at time of function call
	// As a string.
	public String toString() {
		int count = trees.size();
		return "" + count;
	}

}

