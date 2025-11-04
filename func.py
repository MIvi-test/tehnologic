from math import pow, sqrt, pi,exp


def find_sigma(sum_time, ln = 50):
    '''sum_time (ti - tsr)**2'''

    sigma = sqrt(sum_time / ln)
    return round(sigma, 6)


def P(t, sr, sigma):
    kof = 1 / (sqrt(2*pi) * sigma)
    power = (-pow((t - sr),2)) / (2 * pow(sigma,2))
    res = kof * exp(power)
    return round(res, 5)

def sr_sigma(sigma, N = 50):
    return round(sigma / sqrt(N-1), 5)

