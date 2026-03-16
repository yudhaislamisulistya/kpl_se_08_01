from enum import Enum

class StudentState(Enum):
    TERDAFTAR = "Terdafar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"
    
class Trigger(Enum):
    CETAK_KSM = "Cetak KSM"
    LULUS = "Menyelesaikan Kuliah"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"

transitions = {
    StudentState.TERDAFTAR: {
        Trigger.CETAK_KSM: StudentState.AKTIF,
        Trigger.MENGAJUKAN_CUTI: StudentState.CUTI
    },
    StudentState.AKTIF: {
        Trigger.LULUS: StudentState.LULUS,
        Trigger.MENGAJUKAN_CUTI: StudentState.CUTI
    },
    StudentState.CUTI: {
        Trigger.MENYELESAIKAN_CUTI: StudentState.AKTIF
    }
}

def change_state(current_state, trigger):
    if current_state in transitions and trigger in transitions[current_state]:
        return transitions[current_state][trigger]
    
    return "Transisi tidak valid"

current_state = StudentState.TERDAFTAR
print(f"Status awal: {current_state.value}")

next_state = change_state(current_state, Trigger.MENGAJUKAN_CUTI)
print(f"State Setelah transisi : {next_state}")

next_state = change_state(current_state, Trigger.CETAK_KSM)
print(f"State Setelah transisi : {next_state}")