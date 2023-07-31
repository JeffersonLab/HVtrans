import translationLayer

generation_resolution = translationLayer.generation_resolution
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
num_of_radians_bounded = translationLayer.num_of_radians_bounded
switching_period = translationLayer.switching_period
num_of_modules = translationLayer.num_of_modules

gate_timing_lower_bound = translationLayer.gate_timing_lower_bound
gate_timing_upper_bound = translationLayer.gate_timing_upper_bound
gate_timing_bound_offset = translationLayer.gate_timing_bound_offset
gate_timing_length_offset = translationLayer.gate_timing_length_offset
gate_timing_length = translationLayer.gate_timing_length

deadtime_rising_phase_seconds = translationLayer.deadtime_rising_phase_seconds
deadtime_intermediate_phase_seconds = translationLayer.deadtime_intermediate_phase_seconds
deadtime_falling_phase_seconds = translationLayer.deadtime_falling_phase_seconds

deadtime_rising_phase_radians = translationLayer.deadtime_rising_phase_radians
deadtime_intermediate_phase_radians = translationLayer.deadtime_intermediate_phase_radians
deadtime_falling_phase_radians = translationLayer.deadtime_falling_phase_radians

deadtime = [] #list used for deadtimeSimulation generation

def calc_deadtime_module():
    time = 0 
    while(time < deadtime_rising_phase_radians):
        deadtime.append(0)
        time = time + generation_resolution
    time = 0 
    while(time < deadtime_intermediate_phase_radians):
        deadtime.append(1)
        time = time + generation_resolution
    time = 0 
    while(time < deadtime_falling_phase_radians):
        deadtime.append(0)
        time = time + generation_resolution 

def calc_deadtime():
    int_num_of_modules = 0
    while(int_num_of_modules < num_of_modules):
        calc_deadtime_module()
        int_num_of_modules = int_num_of_modules + 1