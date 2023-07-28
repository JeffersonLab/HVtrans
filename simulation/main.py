import translationLayer
import triggerPulseSimulation
import transientSimulation
import BCMSimulation
import detectorSimulation
import deadtimeSimulation
import asymmetryCalculation
import matplotlib.pyplot as plt

trigger = triggerPulseSimulation.trigger
storage = transientSimulation.storage
bcm = BCMSimulation.bcm
detector = detectorSimulation.detector
deadtime = deadtimeSimulation.deadtime
asymmetry = asymmetryCalculation.asymmetry

generation_resolution = translationLayer.generation_resolution
graph_time_interval = translationLayer.graph_time_interval
lower_bound_limit = translationLayer.lower_bound_limit
upper_bound_limit = translationLayer.upper_bound_limit
num_of_seconds_bounded = translationLayer.num_of_seconds_bounded
lower_bound_limit_radian = translationLayer.lower_bound_limit_radian
upper_bound_limit_radian = translationLayer.upper_bound_limit_radian

def set_time_resolution(lower_bound , upper_bound , interval , array , identifier): #sets the time resolution for the x-axis of the graph in seconds, parameters interval in seconds, array in format list, and identifier in scalar
    tick_location = [] #list to store the tick locations on the graph
    tick_label = [] #list to store the tick labels on the graph
    int_counter = lower_bound
    while (int_counter < (upper_bound + interval)):
        tick_location.append(int_counter * (len(array) / (upper_bound - lower_bound)))
        num_of_decimal_places = 5 #sets the number of decimal places in graph labels
        rounded_label = round(int_counter, num_of_decimal_places)
        tick_label.append(rounded_label)
        int_counter += interval
    axs[identifier].set_xticks(tick_location)
    axs[identifier].set_xticklabels(tick_label)

fig, axs = plt.subplots(6)
fig.tight_layout()

triggerPulseSimulation.calc_trigger()
transientSimulation.calc_wave(lower_bound_limit_radian , upper_bound_limit_radian)
BCMSimulation.calc_bcm()
detectorSimulation.calc_detector()
deadtimeSimulation.calc_deadtime()

axs[0].set_title('Trigger Pulse')
axs[0].set_ylabel('Voltage')
axs[0].set_xlabel('Seconds')
axs[0].plot(trigger)
set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , trigger , 0)
axs[1].set_title('Light State Generation')
axs[1].set_ylabel('Voltage')
axs[1].set_xlabel('Seconds')
axs[1].plot(storage)
set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , storage , 1)
axs[2].set_title('Beam Current Monitor')
axs[2].set_ylabel('Voltage')
axs[2].set_xlabel('Seconds')
axs[2].plot(bcm)
set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , bcm , 2)
axs[3].set_title('Detector')
axs[3].set_ylabel('Voltage')
axs[3].set_xlabel('Seconds')
axs[3].plot(detector)
set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , detector , 3)
axs[4].set_title('Deadtime')
axs[4].set_ylabel('State')
axs[4].set_xlabel('Seconds')
axs[4].plot(deadtime)
set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , deadtime , 4)

lower_bound = 0
upper_bound = 500000
interval = 5000
graph_interval = 50000

bcm_sampling_rate = translationLayer.bcm_sampling_rate

asymmetryCalculation.calc_asymmetry(lower_bound , upper_bound , interval)
axs[5].set_title('BCM Resolution vs. Asymmetry')
axs[5].set_ylabel('Asymmetry')
axs[5].set_xlabel('BCM Resolution')
axs[5].plot(asymmetry)
set_time_resolution(lower_bound , upper_bound , graph_interval , asymmetry , 5)

total_asymmetry = asymmetryCalculation.read_current_asymmetry(bcm_sampling_rate , lower_bound , upper_bound , interval)
physics_asymmetry = translationLayer.input_asymmetry
systematic_asymmetry = total_asymmetry - physics_asymmetry

print('physics asymmetry: ' + str(physics_asymmetry))
print('systematic asymmetry: ' + str(systematic_asymmetry))
print('total asymmetry: ' + str(total_asymmetry))

plt.show()