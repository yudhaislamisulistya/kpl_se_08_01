import time
from enum import Enum

class TrafficLightState(Enum):
    MERAH = "Merah"
    KUNING = "Kuning"
    HIJAU = "Hijau"
    
state_transitions = {
    TrafficLightState.HIJAU: TrafficLightState.KUNING,
    TrafficLightState.KUNING: TrafficLightState.MERAH,
    TrafficLightState.MERAH: TrafficLightState.HIJAU
}

state_durations = {
    TrafficLightState.HIJAU: 4,
    TrafficLightState.KUNING: 2,
    TrafficLightState.MERAH: 5
}

def traffic_light_fsm():
    current_state = TrafficLightState.HIJAU
    while True:
        print(f": Lampu lalu lintas saat ini: {current_state.value} - Durasi: {state_durations[current_state]} detik")
        time.sleep(state_durations[current_state])
        current_state = state_transitions[current_state]

if __name__ == "__main__":
    traffic_light_fsm()