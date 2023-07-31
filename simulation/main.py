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

#---------------------------------------------------------------------------------------------------------------#

#uncomment this block to graph the triggerPulse, transientSimulation, BCMSimulation, detectorSimulation, and deadtimeSimulation

# def set_time_resolution(lower_bound , upper_bound , interval , array , identifier): #sets the time resolution for the x-axis of the graph in seconds, parameters interval in seconds, array in format list, and identifier in scalar
#     tick_location = [] #list to store the tick locations on the graph
#     tick_label = [] #list to store the tick labels on the graph
#     int_counter = lower_bound
#     while (int_counter < (upper_bound + interval)):
#         tick_location.append(int_counter * (len(array) / (upper_bound - lower_bound)))
#         num_of_decimal_places = 5 #sets the number of decimal places in graph labels
#         rounded_label = round(int_counter, num_of_decimal_places)
#         tick_label.append(rounded_label)
#         int_counter += interval
#     axs[identifier].set_xticks(tick_location)
#     axs[identifier].set_xticklabels(tick_label)

# fig, axs = plt.subplots(5)
# fig.tight_layout()

# triggerPulseSimulation.calc_trigger()
# transientSimulation.calc_wave(lower_bound_limit_radian , upper_bound_limit_radian)
# BCMSimulation.calc_bcm()
# detectorSimulation.calc_detector()
# deadtimeSimulation.calc_deadtime()

# axs[0].set_title('Trigger Pulse')
# axs[0].set_ylabel('Voltage')
# axs[0].set_xlabel('Seconds')
# axs[0].plot(trigger)
# set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , trigger , 0)
# axs[1].set_title('Light State Generation')
# axs[1].set_ylabel('Voltage')
# axs[1].set_xlabel('Seconds')
# axs[1].plot(storage)
# set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , storage , 1)
# axs[2].set_title('Beam Current Monitor')
# axs[2].set_ylabel('Voltage')
# axs[2].set_xlabel('Seconds')
# axs[2].plot(bcm)
# set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , bcm , 2)
# axs[3].set_title('Detector')
# axs[3].set_ylabel('Voltage')
# axs[3].set_xlabel('Seconds')
# axs[3].plot(detector)
# set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , detector , 3)
# axs[4].set_title('Deadtime')
# axs[4].set_ylabel('State')
# axs[4].set_xlabel('Seconds')
# axs[4].plot(deadtime)
# set_time_resolution(lower_bound_limit , upper_bound_limit, graph_time_interval , deadtime , 4)

#---------------------------------------------------------------------------------------------------------------#

#uncomment this block to graph a predefined variable, set in asymmetryCalculation, vs. asymmetry

def set_time_resolution(lower_bound , upper_bound , interval , array): #sets the time resolution for the x-axis of the graph in seconds, parameters interval in seconds, array in format list, and identifier in scalar
    tick_location = [] #list to store the tick locations on the graph
    tick_label = [] #list to store the tick labels on the graph
    int_counter = lower_bound
    while (int_counter < (upper_bound + interval)):
        tick_location.append(int_counter * (len(array) / (upper_bound - lower_bound)))
        num_of_decimal_places = 5 #sets the number of decimal places in graph labels
        rounded_label = round(int_counter, num_of_decimal_places)
        tick_label.append(rounded_label)
        int_counter += interval
    plt.xticks(tick_location , tick_label)
    
bcm_resolution_lower_bound = 0 #lower bound of the bcm_resolution iteration, measured in hertz
bcm_resolution_upper_bound = 1000000 #upper bound of the bcm_resolution iteration, measured in hertz
bcm_resolution_interval = 10000 #increment value of the bcm_resolution calculation, measured in hertz
bcm_resolution_graph_interval = 100000 #graph interval for the bcm_resolution vs. asymmetry graph, measured in hertz

bcm_sampling_rate = translationLayer.bcm_sampling_rate
detector_sampling_rate = translationLayer.detector_sampling_rate

asymmetryCalculation.calc_asymmetry(bcm_resolution_lower_bound , bcm_resolution_upper_bound , bcm_resolution_interval)
plt.title('BCM Resolution vs. Asymmetry')
plt.ylabel('Asymmetry')
plt.xlabel('BCM Resolution')
plt.plot(asymmetry)
set_time_resolution(bcm_resolution_lower_bound , bcm_resolution_upper_bound , bcm_resolution_graph_interval , asymmetry)

total_asymmetry = asymmetryCalculation.read_current_asymmetry(bcm_sampling_rate , bcm_resolution_lower_bound , bcm_resolution_upper_bound , bcm_resolution_interval)
physics_asymmetry = translationLayer.input_asymmetry
systematic_asymmetry = total_asymmetry - physics_asymmetry

print('physics asymmetry: ' + str(physics_asymmetry))
print('systematic asymmetry: ' + str(systematic_asymmetry))
print('total asymmetry: ' + str(total_asymmetry))

#---------------------------------------------------------------------------------------------------------------#

plt.show()