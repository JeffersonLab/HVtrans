import translationLayer
import triggerPulseSimulation
import transientSimulation
import matplotlib.pyplot as plt

graph_time_interval = translationLayer.graph_time_interval
generation_resolution = translationLayer.generation_resolution
BCM_resolution = translationLayer.BCM_resolution

helicity_asymmetry = translationLayer.helicity_asymmetry

trigger = triggerPulseSimulation.trigger
storage = transientSimulation.storage

triggerPulseSimulation.calc_trigger()
print('Trigger Pulse Generation Finished')
transientSimulation.calc_wave()
print('Light Beam Generation Finished')

import samplingSimulation
import deadtimeCalculator

BCM_storage = samplingSimulation.BCM_storage
deadtime_detector = deadtimeCalculator.deadtime_detector
deadtime_BCM = deadtimeCalculator.deadtime_BCM

samplingSimulation.calc_wave_BCM()
print('BCM Sampling Finished')
deadtimeCalculator.calc_deadtime_detector()
deadtimeCalculator.calc_deadtime_BCM()
print('Deadtime Simulation Finished')

seconds_in_wave = len(storage) * generation_resolution #number of seconds in the entire generated wave

import asymmetryCalculator

asymmetryCalculator.BCM_transient_voltage_calculator()
asymmetryCalculator.detector_transient_voltage_calculator()

systematic_error_maybe = asymmetryCalculator.calc_total_asymmetry()
total_asymmetry = systematic_error_maybe + helicity_asymmetry

print(total_asymmetry)

#x-axis labeling:
tick_location_trigger = [] #list to store the x-axis tick locations on the trigger graph
tick_label_trigger = [] #list to store the x-axis tick labels on the trigger graph
num_of_microseconds_trigger = (len(trigger) * generation_resolution)
int_num_of_microseconds_trigger = 0
while (int_num_of_microseconds_trigger < (num_of_microseconds_trigger + 1)):
    tick_location_trigger.append(int_num_of_microseconds_trigger * (len(trigger) / num_of_microseconds_trigger))
    tick_label_trigger.append(round(int_num_of_microseconds_trigger , 4))
    int_num_of_microseconds_trigger = int_num_of_microseconds_trigger + graph_time_interval

tick_location_detector = [] #list to store the x-axis tick locations on the detector graph
tick_label_detector = [] #list to store the x-axis tick labels on the detector graph
num_of_microseconds_detector = (len(storage) * generation_resolution)
int_num_of_microseconds_detector = 0
while (int_num_of_microseconds_detector < (num_of_microseconds_detector + 1)):
    tick_location_detector.append(int_num_of_microseconds_detector * (len(storage) / num_of_microseconds_detector))
    tick_label_detector.append(round(int_num_of_microseconds_detector , 4))
    int_num_of_microseconds_detector = int_num_of_microseconds_detector + graph_time_interval

tick_location_BCM = [] #list to store the x-axis tick locations on the BCM graph
tick_label_BCM = [] #list to store the x-axis tick labels on the BCM graph
num_of_microseconds_BCM = (len(BCM_storage) * BCM_resolution)
int_num_of_microseconds_BCM = 0
while (int_num_of_microseconds_BCM < (num_of_microseconds_BCM + 1)):
    tick_location_BCM.append(int_num_of_microseconds_BCM * (len(BCM_storage) / num_of_microseconds_BCM))
    tick_label_BCM.append(round(int_num_of_microseconds_BCM , 4))
    int_num_of_microseconds_BCM = int_num_of_microseconds_BCM + graph_time_interval

#graphs:
fig, axs = plt.subplots(5)

fig.tight_layout()

axs[0].set_xticks(tick_location_trigger)
axs[0].set_xticklabels(tick_label_trigger)
axs[0].set_ylabel('Voltage')
axs[0].set_xlabel('Seconds')
axs[0].plot(trigger)
axs[0].set_title('Trigger Pulse')

# axs[1].set_xticks(tick_location_detector)
# axs[1].set_xticklabels(tick_label_detector)
axs[1].set_ylabel('Voltage')
axs[1].set_xlabel('Seconds')
axs[1].plot(storage)
axs[1].set_title('Detector')

# axs[2].set_xticks(tick_location_BCM)
# axs[2].set_xticklabels(tick_label_BCM)
axs[2].set_ylabel('Voltage')
axs[2].set_xlabel('Seconds')
axs[2].plot(BCM_storage)
axs[2].set_title('BCM')

axs[3].set_xticks(tick_location_detector)
axs[3].set_xticklabels(tick_label_detector)
axs[3].plot(deadtime_detector)
axs[3].set_title('Detector Deadtime')

axs[4].set_xticks(tick_location_detector)
axs[4].set_xticklabels(tick_label_detector)
axs[4].plot(deadtime_BCM)
axs[4].set_title('BCM Deadtime')

plt.show()