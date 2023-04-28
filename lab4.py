import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input variables
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')
humidity = ctrl.Antecedent(np.arange(0, 101, 1), 'humidity')

# Define the output variable
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), 'fan_speed')

# Define the membership functions for each input variable
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])
temperature['moderate'] = fuzz.trimf(temperature.universe, [0, 50, 100])
temperature['hot'] = fuzz.trimf(temperature.universe, [50, 100, 100])

humidity['low'] = fuzz.trimf(humidity.universe, [0, 0, 50])
humidity['moderate'] = fuzz.trimf(humidity.universe, [0, 50, 100])
humidity['high'] = fuzz.trimf(humidity.universe, [50, 100, 100])

# Define the membership functions for the output variable
fan_speed['low'] = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed['medium'] = fuzz.trimf(fan_speed.universe, [0, 50, 100])
fan_speed['high'] = fuzz.trimf(fan_speed.universe, [50, 100, 100])

# Define the rules
rule1 = ctrl.Rule(temperature['cold'] & humidity['low'], fan_speed['low'])
rule2 = ctrl.Rule(temperature['cold'] & humidity['moderate'], fan_speed['medium'])
rule3 = ctrl.Rule(temperature['cold'] & humidity['high'], fan_speed['high'])
rule4 = ctrl.Rule(temperature['moderate'] & humidity['low'], fan_speed['medium'])
rule5 = ctrl.Rule(temperature['moderate'] & humidity['moderate'], fan_speed['medium'])
rule6 = ctrl.Rule(temperature['moderate'] & humidity['high'], fan_speed['high'])
rule7 = ctrl.Rule(temperature['hot'] & humidity['low'], fan_speed['medium'])
rule8 = ctrl.Rule(temperature['hot'] & humidity['moderate'], fan_speed['high'])
rule9 = ctrl.Rule(temperature['hot'] & humidity['high'], fan_speed['high'])

# Define the control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])

# Create a simulation
fan_speed_sim = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# Set the inputs
fan_speed_sim.input['temperature'] = 60
fan_speed_sim.input['humidity'] = 80

# Compute the output
fan_speed_sim.compute()

# Print the output
print(fan_speed_sim.output['fan_speed'])
