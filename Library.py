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

# static const float3x3 XYZ_2_sRGB_MAT =
# {
# 	 3.2409699419, -1.5373831776, -0.4986107603,
# 	-0.9692436363,  1.8759675015,  0.0415550574,
# 	 0.0556300797, -0.2039769589,  1.0569715142,
# };

# static const float3x3 sRGB_2_XYZ_MAT =
# {
# 	0.4124564, 0.3575761, 0.1804375,
# 	0.2126729, 0.7151522, 0.0721750,
# 	0.0193339, 0.1191920, 0.9503041,
# };

def XYZ_2_sRGB(x, y, z):
    r = 3.2409699419 * x + -1.5373831776 * y + -0.4986107603 * z
    g = -0.9692436363 * x + 1.8759675015 * y + 0.0415550574 * z
    b = 0.0556300797 * x + -0.2039769589 * y + 1.0569715142 * z
    # r = 3.2409699419 * x + -0.9692436363 * y + 0.0556300797 * z
    # g = -1.5373831776 * x + 1.8759675015 * y + -0.2039769589 * z
    # b = -0.4986107603 * x + 0.0415550574 * y + 1.0569715142 * z
    return [r, g, b]