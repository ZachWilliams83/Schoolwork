
public class PatientTester {

	public static void main(String[] args) {
		PatientManager patientManager = new PatientManager();
		System.out.println(patientManager.ToString());
		Patient patient1 = new Patient(1, 100);
		Patient patient2 = new Patient(2, 200);
		Patient patient3 = new Patient(3, 300);
		Patient patient4 = new Patient(4, 400);
		patientManager.PatientPlace(patient1);
		patientManager.PatientPlace(patient2);
		patientManager.PatientPlace(patient3);
		patientManager.PatientPlace(patient4);
		System.out.println(patientManager.ToString());
		patientManager.caffeineAbsorption();
		System.out.println(patientManager.ToString());
		patientManager.removePatientWithHighestCaffeine();
		System.out.println(patientManager.ToString());
		
	}

}
