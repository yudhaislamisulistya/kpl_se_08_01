from enum import Enum

class JenisKelamin(Enum):
    PRIA = 1
    WANITA = 2
    
patients = []

def addPatient(name: str, gender: JenisKelamin):
    if not isinstance(gender, JenisKelamin):
        raise ValueError("Gender harus berupa instance dari JenisKelamin Enum")

    patients.append({
        "name": name,
        "gender": gender.name
    })
    
    print(f"Patient {name} dengan jenis kelamin {gender.name} berhasil ditambahkan.")


addPatient("John Doe", JenisKelamin.PRIA)
addPatient("Jane Doe", JenisKelamin.WANITA)
addPatient("Alex Smith", JenisKelamin.PRIA)

for patient in patients:
    print(f"Nama: {patient['name']}, Jenis Kelamin: {patient['gender']}")