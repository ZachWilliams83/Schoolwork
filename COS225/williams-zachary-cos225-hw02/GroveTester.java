
public class GroveTester {
	public static void main(String[] args) {

		Grove grove1 = new Grove("Grove One");
		System.out.println(grove1.toString());
		for (int j = 0; j < 7; j++) {
			Tree tree = new Tree(j, 37, "Pine");
			grove1.plantTree(tree);
		}
		System.out.println(grove1.toString());
		grove1.removeTree(3);
		grove1.removeTree(5);
		System.out.println(grove1.toString());
		Tree tree1 = new Tree(0, 13, "Spruce");
		grove1.plantTree(tree1);
		System.out.println(grove1.toString());
	}
}

