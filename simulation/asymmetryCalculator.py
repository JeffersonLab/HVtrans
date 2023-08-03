import translationLayer
import deadtimeCalculator
import numpy

generation_resolution = translationLayer.generation_resolution

pos_detector = deadtimeCalculator.pos_detector
neg_detector = deadtimeCalculator.neg_detector

def calc_asymmetry(BCM_resolution , pos_BCM , neg_BCM):
    integrated_pos_detector = numpy.trapz(y = pos_detector , dx = generation_resolution)
    integrated_neg_detector = abs(numpy.trapz(y = neg_detector , dx = generation_resolution))

    integrated_pos_BCM = numpy.trapz(y = pos_BCM , dx = BCM_resolution)
    integrated_neg_BCM = abs(numpy.trapz(y = neg_BCM , dx = BCM_resolution))

    total_asymmetry = ((integrated_pos_detector / integrated_pos_BCM) - (integrated_neg_detector / integrated_neg_BCM)) / ((integrated_pos_detector / integrated_pos_BCM) + (integrated_neg_detector / integrated_neg_BCM))
    
    return total_asymmetry