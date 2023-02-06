// Zach Williams
// 1/30/23
public class ParkingLot {
	ParkingSpot[] spots;
	Car car;
	public int ncounter = 0;
	public int hcounter = 0;
	public ParkingLot(){
		// creates and fills an array of spots with booleans for handicap.
		spots = new ParkingSpot[20];
		for (int i = 0; i < 20; i++) {
			if (i < 4) {
				spots[i] = new ParkingSpot(true);
			}
			else {
				spots[i] = new ParkingSpot(false);
			}
		}
	}
	public int ParkCar(Car car) {
		if (car.handicap == true) {
			// parks car in handicap if available
			for (int x = 0; x<4; x++) {
				if (spots[x] != null) {
					hcounter--;
					spots[x].equals(null);
					return x;
				}
			}
		}
		else if (car.handicap == false){
			// parks non-handicap car in non-handicap spot
			for (int y = 4;(y < 20); y++) {
				if (spots[y] != null) {
					ncounter--;
					spots[y].equals(null);
					return y;
				}
			}
		}
		return 0;
	}
	public int RemoveCar(int a, Car car) {
		// pulls the int assigned to the car and if it is handicap
		// it allows it to reopen the spot.
		if (a < 4) {
			spots[a] = null;
			hcounter++;
		}
		else if (a > 4) {
			spots[a] = null;
			ncounter++;
		}
		return 0;
	}
	//@Override possibly not needed anymore.
	public String ToString() {
		// for loop needed here
		// if (is a spot null or not)
		//		if (is a spot handicap or not)
		// keep two separate counters
		// convert to string ("" + number)
		if (hcounter == 0 && ncounter == 0) {
			for (int j = 0; j < 20; j++) {
				if (spots[j] != null) {
					if (spots[j].handicap == true) {
						hcounter++;
					}
					else if (spots[j].handicap == false) {
						ncounter++;
					}
				}
			}
		}
		return "" + hcounter + " " + ncounter;

	}
}

