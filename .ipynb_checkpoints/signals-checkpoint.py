import numpy as np
import matplotlib.pyplot as plt

#File dedicated to creating the following waves:
# - sine wave
# - cossine wave
# - sinc wave
# - unit step function
# - Dirac Delta function



                                                                    # Sine function

#Defining the sine function:
def create_sine_wave(frequency, duration):
    t = np.linspace(-10, 10, 1000)                  #Defines the horizontal time axis 
    y = np.sin(2 * np.pi * frequency * t)           #Defines the sin function
    return t, y

tsin, ysin = create_sine_wave(1, 2)       

#Plotting the function:
plt.plot(tsin, ysin)
plt.xlabel("t")
plt.ylabel("sin(t)")
plt.title("Sine Wave")
plt.show()


                                                                    # Cossine function

#Defining the cossine function: 
def create_cossine_wave(frequency, duration):
    t = np.linspace(-10, 10, 1000)                     #Defines the horizontal time axis
    y = np.cos(2*np.pi*frequency*t)                    #Defines the cos function
    return t, y
    
tcos, ycos = create_cossine_wave(1, 2)

#Plotting the function:
plt.plot(tcos, ycos)
plt.xlabel("t")
plt.ylabel("cos(t)")
plt.title("Cossine Wave")
plt.show()


                                                                    # Sinc function
def sinc_function(tsinc):
# Horizontal time axis:
    tsinc = np.linspace(-10, 10, 1000)   #tsinc --> t for sinc function

# Defining the sinc function:
    ysinc = np.sinc(tsinc)             # NumPy uses the normalized definition by default, sinc(t) = sin(pi*t)/(pi*t)                    
                                       # It means that the zeros of the function will be on the integers different than zero 
    return tsinc,ysinc
tsinc,ysinc = sinc_function(1)
# Plotting the function: 
plt.plot(tsinc, ysinc)
plt.title("Normalized Sinc Function: sinc(t) = sin(πt)/(πt)")
plt.xlabel("t")
plt.ylabel("sinc(t)")
plt.grid(True)
plt.show()




                                                                    # Unit step function

def usf_function(tusf):
# Continuous time axis: 
    tusf = np.linspace(-1, 1, 1000)     #tusf --> t for unit step function

# Defining the unit step function:
    u = np.where(tusf >= 0, 1, 0)  # Refered as u(t) by standart 
    return tusf,u
tusf, u = usf_function(1)
# Plotting the function: 
plt.plot(tusf, u)
plt.title("Unit Step Function")
plt.xlabel("t")
plt.ylabel("u(t)")
plt.grid(True)
plt.show()



    
                                                                    # - Dirac-Delta function
#Defining the Dirac-Delta function: 
# By definition, it is a function that is equal to zero everywhere except for x=0, and its integral value is equal to 1. And it is the derivative of the unit step function. 
def dirac_delta(n):
# Creating a discrete time axis:
    n = np.arange(-10, 11)

# Create unit pulse:
    delta = np.where(n == 0, 1, 0)  # Refered as δ(t) as standart
    return n, delta
n, delta = dirac_delta(1)
# Plotting the function:
plt.stem(n, delta)
plt.title("Unit Pulse (Discrete-Time)")
plt.xlabel("n") # discrete time horizontal axis
plt.ylabel("δ[n]") # continuous vertical axis
plt.grid(True)
plt.show()
                                                                