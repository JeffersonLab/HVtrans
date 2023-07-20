#transient simulation:
resistance = 730000000000 #resistance of the RTP crystal, measured in ohms
capacitance = 0.0000000000000006 #capacitance of the RTP crystal, measured in farads
nominal_voltage_positve = 5000 #3000 #positve nominal voltage of the power circuitry, measured in volts
nominal_voltage_negative = 5000 #3000 #negative nominal voltage of the power circuitry, measured in volts
nominal_frequency_positive = 500000 #positive nominal frequency of the power circuitry, measured in hertz
nominal_frequency_negative = 500000 #negative nominal frequency of the power circuitry, measured in hertz
voltage_ripple_positive = 600 #voltage ripple of the power circuitry, measured in volts
voltage_ripple_negative = 600 #voltage ripple of the power circuitry, measured in volts
transient_voltage_positive = 14400 #voltage of the transient, measured in volts
transient_voltage_negative = 14400 #voltage of the transient, measured in volts
transient_frequency_positive = 28114 #98039 #positive frequency of the transient, measured in hertz
transient_frequency_negative = 28114 #98039 #negative frequency of the transient, measured in hertz
transient_rise_time_positive = 0.00000025 #positive period of the transient rise time, measured in seconds
transient_rise_time_negative = 0.00000025 #negative period of the transient rise time, measured in seconds
switching_frequency = 1920 #switching frequency of the power circuitry, measured in hertz

#general:
num_of_modules = 10 #number of simulated voltage transistions
generation_resolution = 0.1 #resolution with which the wave is generated, measured in radians
graph_time_interval = 0.05 #interval for the x-axis on the graph, measured in seconds
lower_bound_limit = 0.25 #horizontal lower bound limit of the graph, measured in seconds
upper_bound_limit = 0.35 #horizontal upper bound limit of the graph, measured in seconds

#trigger pulse:
trigger_duty_cycle = 0.90 #duty cycle of the trigger pulse
trigger_nominal_voltage = 5 #nominal voltage of the trigger pulse 
trigger_latency = 0 #latency of the trigger pulse ahead of the wave generation, measured in seconds
trigger_rise_time = 0.0001 #period of the trigger pulse rise time, measured in seconds

#BCM Simulation
bcm_sampling_rate = 10000 #could approach 150ksps with modification #sampling rate of the beam current monitor, measured in samples per second
bcm_frequency_cutoff = 5000000 #beam current monitor frequency cutoff, measured in hertz

#Detector Simulation
detector_sampling_rate = 50000 #sampling rate of the detector, measured in samples per second
detector_frequency_cutoff = 5000000 #detector frequency cutoff, measured in hertz

#Systematic Effects
gate_timing_offset = 0 #offset in the gate timing when measuring the deadtime