import translationLayer
import triggerPulseSimulation
import transientSimulation
import samplingSimulation
import deadtimeCalculator
import systematicErrorCalculator
import matplotlib.pyplot as plt

collision_asymmetry = translationLayer.collision_asymmetry

graph_time_interval = translationLayer.graph_time_interval
generation_resolution = translationLayer.generation_resolution
BCM_resolution = translationLayer.BCM_resolution
BCM_min_bandpass = translationLayer.BCM_min_bandpass
BCM_bandpass_interval = translationLayer.BCM_bandpass_interval

trigger = triggerPulseSimulation.trigger
storage = transientSimulation.storage
BCM_storage = samplingSimulation.BCM_storage
deadtime_detector = deadtimeCalculator.deadtime_detector
deadtime_BCM = deadtimeCalculator.deadtime_BCM
length_deadtime_detector = deadtimeCalculator.length_deadtime_detector
length_deadtime_BCM = deadtimeCalculator.length_deadtime_BCM
epsilon_vs_BCM_resolution_array = systematicErrorCalculator.epsilon_vs_BCM_resolution_array

triggerPulseSimulation.calc_trigger()
transientSimulation.calc_wave()

seconds_in_wave = len(storage) * generation_resolution #number of seconds in the entire generated wave

deadtimeCalculator.calc_length_deadtime_detector()
systematicErrorCalculator.epsilon_vs_BCM_resolution(storage , seconds_in_wave , length_deadtime_detector)

BCM_storage.clear()
deadtime_BCM.clear()
length_deadtime_BCM.clear()

samplingSimulation.calc_wave_BCM(storage , seconds_in_wave , BCM_resolution)
deadtimeCalculator.calc_length_deadtime_BCM(BCM_resolution)

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

BCM_resolution = 1 / BCM_resolution

tick_location_BCM = [] #list to store the x-axis tick locations on the BCM graph
tick_label_BCM = [] #list to store the x-axis tick labels on the BCM graph
num_of_microseconds_BCM = (len(BCM_storage) * BCM_resolution)
int_num_of_microseconds_BCM = 0
while (int_num_of_microseconds_BCM < (num_of_microseconds_BCM + 1)):
    tick_location_BCM.append(int_num_of_microseconds_BCM * (len(BCM_storage) / num_of_microseconds_BCM))
    tick_label_BCM.append(round(int_num_of_microseconds_BCM , 4))
    int_num_of_microseconds_BCM = int_num_of_microseconds_BCM + graph_time_interval

tick_location_epsilon_resolution = [] #list to store the x-axis tick locations on the epsilon vs. BCM bandpass graph
tick_label_epsilon_resolution = [] #list to store the x-axis tick labels on the epsilon vs. BCM bandpass graph
num_of_intervals_epsilon_resolution = (len(epsilon_vs_BCM_resolution_array) * BCM_bandpass_interval)
int_num_of_intervals_epsilon_resolution = 0
while (int_num_of_intervals_epsilon_resolution < (num_of_intervals_epsilon_resolution + BCM_bandpass_interval)):
    tick_location_epsilon_resolution.append(int_num_of_intervals_epsilon_resolution * (len(epsilon_vs_BCM_resolution_array) / num_of_intervals_epsilon_resolution))
    tick_label_epsilon_resolution.append(int_num_of_intervals_epsilon_resolution + BCM_min_bandpass)
    int_num_of_intervals_epsilon_resolution = int_num_of_intervals_epsilon_resolution + (5 * BCM_bandpass_interval)

#graphs:
fig, axs = plt.subplots(6)

fig.tight_layout()

axs[0].set_xticks(tick_location_trigger)
axs[0].set_xticklabels(tick_label_trigger)
axs[0].set_ylabel('Voltage')
axs[0].set_xlabel('Seconds')
axs[0].plot(trigger)
axs[0].set_title('Trigger Pulse')

axs[1].set_xticks(tick_location_detector)
axs[1].set_xticklabels(tick_label_detector)
axs[1].set_ylabel('Voltage')
axs[1].set_xlabel('Seconds')
axs[1].plot(storage)
axs[1].set_title('Detector')

axs[2].set_xticks(tick_location_BCM)
axs[2].set_xticklabels(tick_label_BCM)
axs[2].set_ylabel('Voltage')
axs[2].set_xlabel('Seconds')
axs[2].plot(BCM_storage)
axs[2].set_title('BCM')

axs[3].set_xticks(tick_location_detector)
axs[3].set_xticklabels(tick_label_detector)
axs[3].plot(deadtime_detector)
axs[3].set_title('Detector Deadtime')

axs[4].set_xticks(tick_location_BCM)
axs[4].set_xticklabels(tick_label_BCM)
axs[4].plot(deadtime_BCM)
axs[4].set_title('BCM Deadtime')

axs[5].set_xticks(tick_location_epsilon_resolution)
axs[5].set_xticklabels(tick_label_epsilon_resolution)
axs[5].set_ylabel('Epsilon')
axs[5].set_xlabel('BCM Bandpass (10^5)')
axs[5].plot(epsilon_vs_BCM_resolution_array)
axs[5].set_title('BCM Bandpass vs. Systematic Error')

plt.show()