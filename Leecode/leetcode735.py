asteroids =  [-2,1,-2,2]

def asteroidCollision(asteroids):
    i = 0
    while i < len(asteroids)-1:
        if asteroids[i] * asteroids[i+1] < 0:
            if abs(asteroids[i]) > abs(asteroids[i+1]):
                asteroids.remove(asteroids[i+1])
            elif abs(asteroids[i]) < abs(asteroids[i+1]):
                asteroids.remove(asteroids[i])
            else:
                asteroids.remove(asteroids[i])
                asteroids.remove(asteroids[i])
            if i > 2 :
                i -= 2
            else:
                i = -1
        i += 1

    return asteroids


print(asteroidCollision(asteroids))