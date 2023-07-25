import translationLayer

generation_resolution = translationLayer.generation_resolution
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
num_of_radians_bounded = translationLayer.num_of_radians_bounded

gate_timing_lower_bound = translationLayer.gate_timing_lower_bound
gate_timing_upper_bound = translationLayer.gate_timing_upper_bound
gate_timing_bound_offset = translationLayer.gate_timing_bound_offset
gate_timing_length_offset = translationLayer.gate_timing_length_offset
gate_timing_length = translationLayer.gate_timing_length

deadtime_rising_phase_seconds = gate_timing_lower_bound
deadtime_intermediate_phase_seconds = gate_timing_length
deadtime_trailing_phase_seconds =  (num_of_seconds_bounded - (gate_timing_lower_bound + gate_timing_length))

deadtime_rising_phase_radians = ((deadtime_rising_phase_seconds / num_of_seconds_bounded) * num_of_radians_bounded)
deadtime_intermediate_phase_radians = ((deadtime_intermediate_phase_seconds / num_of_seconds_bounded) * num_of_radians_bounded)
deadtime_trailing_phase_radians = ((deadtime_trailing_phase_seconds / num_of_seconds_bounded) * num_of_radians_bounded)

deadtime = [] #list used for deadtimeSimulation generation

def calc_deadtime():
    time = 0 
    while(time < deadtime_rising_phase_radians):
        deadtime.append(0)
        time = time + generation_resolution
    time = 0 
    while(time < deadtime_intermediate_phase_radians):
        deadtime.append(1)
        time = time + generation_resolution
    time = 0 
    while(time < deadtime_trailing_phase_radians):
        deadtime.append(0)
        time = time + generation_resolution