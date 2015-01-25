from numpy import *


# random array
randomArr = random.rand(4, 4)
print(type(randomArr))
print(randomArr)

# matrix
randomMat = mat(randomArr)
print(type(randomMat))
print(randomMat)

# reverse matrix
reverseMat = randomMat.I
print(reverseMat)
print(randomMat * reverseMat)

