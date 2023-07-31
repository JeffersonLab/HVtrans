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

import asymmetryCalculator

BCM_sampling_rate_interval = translationLayer.BCM_sampling_rate_interval
BCM_max_sampling_rate = translationLayer.BCM_max_sampling_rate

total_asymmetry = []
BCM_sampling_rate = 1 / BCM_resolution
while (BCM_sampling_rate < BCM_max_sampling_rate):
    samplingSimulation.calc_wave_BCM((1 / BCM_sampling_rate))
    asymmetryCalculator.BCM_transient_voltage_calculator((1 / BCM_sampling_rate) , BCM_storage)
    asymmetryCalculator.detector_transient_voltage_calculator()

    systematic_error = asymmetryCalculator.calc_total_asymmetry()
    total_asymmetry.append(systematic_error + helicity_asymmetry)

    BCM_storage.clear()
    BCM_sampling_rate = BCM_sampling_rate + BCM_sampling_rate_interval

BCM_storage.clear()

samplingSimulation.calc_wave_BCM(BCM_resolution)
print('BCM Sampling Finished')
deadtimeCalculator.calc_deadtime_detector()
deadtimeCalculator.calc_deadtime_BCM()
print('Deadtime Simulation Finished')

#x-axis labeling:
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

tick_location_res_vs_asym = [] #list to store the x-axis tick locations on the BCM graph
tick_label_res_vs_asym = [] #list to store the x-axis tick labels on the BCM graph
num_of_samples_per_second = len(total_asymmetry)
int_num_of_samples_per_second = 0
while (int_num_of_samples_per_second < (num_of_samples_per_second + 1)):
    tick_location_res_vs_asym.append(int_num_of_samples_per_second * (len(total_asymmetry) / num_of_samples_per_second))
    tick_label_res_vs_asym.append((BCM_sampling_rate_interval * int_num_of_samples_per_second) + int(1 / BCM_resolution))
    int_num_of_samples_per_second = int_num_of_samples_per_second + 1

#graphs:
# fig, axs = plt.subplots(2)

# fig.tight_layout()

# axs[0].set_xticks(tick_location_detector)
# axs[0].set_xticklabels(tick_label_detector)
# axs[0].set_ylabel('Voltage')
# axs[0].set_xlabel('Seconds')
# axs[0].plot(trigger)
# axs[0].set_title('Trigger Pulse')

# axs[1].set_xticks(tick_location_detector)
# axs[1].set_xticklabels(tick_label_detector)
# axs[1].set_ylabel('Voltage')
# axs[1].set_xlabel('Seconds')
# axs[1].plot(storage)
# axs[1].set_title('Detector')

# axs[2].set_xticks(tick_location_detector)
# axs[2].set_xticklabels(tick_label_detector)
# axs[2].plot(deadtime_detector)
# axs[2].set_title('Detector Deadtime')

# axs[3].set_xticks(tick_location_BCM)
# axs[3].set_xticklabels(tick_label_BCM)
# axs[3].set_ylabel('Voltage')
# axs[3].set_xlabel('Seconds')
# axs[3].plot(BCM_storage)
# axs[3].set_title('BCM')

# axs[4].set_xticks(tick_location_detector)
# axs[4].set_xticklabels(tick_label_detector)
# axs[4].plot(deadtime_BCM)
# axs[4].set_title('BCM Deadtime')

plt.xticks(tick_location_res_vs_asym , tick_label_res_vs_asym)
plt.ylabel('Asymmetry')
plt.xlabel('Sampling Rate (Samples / Second)')
plt.plot(total_asymmetry)
plt.title('BCM Sampling Rate vs. Total Asymmetry')

plt.show()