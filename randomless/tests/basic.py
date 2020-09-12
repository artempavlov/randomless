from ..randomless import Random


random = Random()

print('randrange:', random.randrange(0, 5, 1))

print('randint:', random.randint(0, 5))

print('choice:', random.choice([1, 2, 3, 4, 5]))

l = [1, 2, 3, 4, 5]
random.shuffle(l)
print('shuffle:', l)

print('sample:', random.sample([1, 2, 3, 4, 5], 3))

print('random:', random.random())

print('uniform:', random.uniform(0, 5))

print('triangular:', random.triangular(0, 1, 0.5))

print('betavariate:', random.betavariate(1, 1))

print('expovariate:', random.expovariate(5))

print('gammavariate:', random.gammavariate(1, 1))

print('gauss:', random.gauss(1, 1))

print('lognormvariate:', random.lognormvariate(1, 1))

print('normalvariate:', random.normalvariate(1, 1))

print('vonmisesvariate:', random.vonmisesvariate(1, 1))

print('paretovariate:', random.paretovariate(1))

print('weibullvariate:', random.weibullvariate(1, 1))

random.release()