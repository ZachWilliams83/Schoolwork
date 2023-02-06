// Zach Williams
// 1/30/23
// taken from live coding in class.
public class Car {
	String manufacturer;
	String color;
	boolean handicap;
	
	public Car(String manufacturer, String color, boolean handicap) {
		//this.color = color; grabs color from the object to update the parameter, only needed if named the same
		this.color = color; // option to rename parameter and declare as such.
		this.manufacturer = manufacturer;
		this.handicap = handicap;
		// no return needed for constructors.
	}
}
