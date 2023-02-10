
public class Tree {
	public int idNumber;
	public int age;
	public String species;

	public int getIdNumber() {
		return idNumber;
	}

	public void setIdNumber(int idNumber) {
		this.idNumber = idNumber;
	}

	public Tree(int idNumber, int age, String species) {
		this.idNumber = idNumber;
		this.age = age;
		this.species = species;
	}
}
