import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]


# mean
x = numpy.mean(speed)

print('Mean {0}'.format(x))
print(f'Mean ',x)

#MEdian
import numpy

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.median(speed)

print('Median {0}'.format(x))
print(f'Median ',x)

#Mode
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)
print('Mode {0}'.format(x))
print(f'Mode',x)