public class ParkingTester {
	
	public static void main(String[] args) {
		int x = 0;
		int y = 0;
		ParkingLot lot = new ParkingLot();
		System.out.println(lot.ToString());
		Car car1 = new Car("Red","Infiniti",true);
		Car car2 = new Car("Gray","Cadillac",false);
		x = lot.ParkCar(car1);
		System.out.println(lot.ToString());
		y = lot.ParkCar(car2);
		System.out.println(lot.ToString());
		lot.RemoveCar(x, car1);
		System.out.println(lot.ToString());
	}
}
