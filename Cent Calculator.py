import math


def cent_calc(freq1, freq2):
    ratio = (freq1 / freq2)
    log_result = math.log(ratio, 2)
    print(log_result * 1200)

# cent_calc(440, 445.5)
