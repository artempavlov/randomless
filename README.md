# Randomless
A python module which provides a True Random Number Generator (TRNG) based on the electronic noise captured by your webcam. The api is mostly compatible with Python's default random module.
## Requirements
Python 3 \
opencv-python==4.4.0 \
numpy==1.19.1
## Installation
Install requirements by executing the following command.
```sh
pip install -r requirements.txt
```
Place the folder containing file "\_\_init\_\_.py" into your project directory or into the default python module installation directory.
## Usage
Import.
```python
from randomless import Random
```
Create a Random class instance.
```python
random = Random()
````
Generate a random number just like you would with Python's default random module.
```python
random.random()
```
Use any other random method the same way as it is with Python's RNG.
```python
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
```
Stop the process of collecting noise from your webcam.
```python
random.release()
````