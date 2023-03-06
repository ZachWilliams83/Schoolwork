import java.util.ArrayList;

public class PatientManager {
	public ArrayList<Patient> patientList = new ArrayList<Patient>();

	public PatientManager() {
		//
	}

	public int PatientPlace(Patient patient) {
		int IdNumber = patient.IdNumber;
		patientList.add(IdNumber-1,patient);

		return IdNumber;
	}
	public void removePatientWithHighestCaffeine() {
		int maxIndex = 0;
		double maxCaffeine = 0;
		for (int i = 0; i < patientList.size(); i++) {
			Patient currentPatient = patientList.get(i);
			if (currentPatient.caffeine > maxCaffeine) {
				maxCaffeine = currentPatient.caffeine;
				maxIndex = i;
			}
		}
		patientList.remove(maxIndex);
	}

	public void caffeineAbsorption() {
		for (int j = 0; j < patientList.size(); j++) {
			Patient activePatient = patientList.get(j);
			if (activePatient.caffeine >= 130) {
				activePatient.caffeine = activePatient.caffeine - 130;
			}
			else {
				patientList.remove(activePatient);
				j--;
			}
		}
	}


	public String ToString() {
		StringBuilder sb = new StringBuilder();
		for (Patient p : patientList) {
			sb.append(p.IdNumber).append(" ").append(p.caffeine).append("\n");
		}
		return sb.length() == 0 ? "Empty" : sb.toString();
	}

}