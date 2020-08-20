import math
import numpy as np

def color_match_x(wave):
    t1 = (wave-442.0)*(0.0624 if (wave<442.0) else 0.0374)
    t2 = (wave-599.8)*(0.0264 if (wave<599.8) else 0.0323)
    t3 = (wave-501.1)*(0.0490 if (wave<501.1) else 0.0382)
    return 0.362*math.exp(-0.5*t1*t1) + 1.056*math.exp(-0.5*t2*t2) - 0.065*math.exp(-0.5*t3*t3)

def color_match_y(wave):
    t1 = (wave-568.8)*(0.0213 if (wave<568.8) else 0.0247)
    t2 = (wave-530.9)*(0.0613 if (wave<530.9) else 0.0322)
    return 0.821*math.exp(-0.5*t1*t1) + 0.286*math.exp(-0.5*t2*t2)

def color_match_z(wave):
    t1 = (wave-437.0)*(0.0845 if (wave<437.0) else 0.0278)
    t2 = (wave-459.0)*(0.0385 if (wave<459.0) else 0.0725)
    return 1.217*math.exp(-0.5*t1*t1) + 0.681*math.exp(-0.5*t2*t2)

def spectrum_range(step):
    return np.arange(380.0, 760.0, step)

class Chromaticities:
    def __init__(self, Red, Green, Blue, White):
        super().__init__()
        self.Red = Red
        self.Green = Green
        self.Blue = Blue
        self.White = White

sRGB = Chromaticities(np.array([0.64000, 0.33000]), np.array([0.30000, 0.60000]), np.array([0.15000, 0.06000]), np.array([0.31270, 0.32900]))
Rec2020 = Chromaticities(np.array([0.70800, 0.29200]), np.array([0.17000, 0.79700]), np.array([0.13100, 0.04600]), np.array([ 0.31270, 0.32900]))
