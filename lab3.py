import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Create antecedents and consequents
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
food = ctrl.Antecedent(np.arange(0, 11, 1), 'food')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Define membership functions for antecedents and consequents
service['poor'] = fuzz.trimf(service.universe, [0, 0, 5])
service['good'] = fuzz.trimf(service.universe, [0, 5, 10])
service['excellent'] = fuzz.trimf(service.universe, [5, 10, 10])

food['poor'] = fuzz.trimf(food.universe, [0, 0, 5])
food['good'] = fuzz.trimf(food.universe, [0, 5, 10])
food['excellent'] = fuzz.trimf(food.universe, [5, 10, 10])

tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

# Visualize membership functions
service.view()
food.view()
tip.view()

# Define rules
rule1 = ctrl.Rule(service['poor'] | food['poor'], tip['low'])
rule2 = ctrl.Rule(service['good'], tip['medium'])
rule3 = ctrl.Rule(service['excellent'] | food['excellent'], tip['high'])

# Create control system and simulation
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping_sim = ctrl.ControlSystemSimulation(tipping_ctrl)

# Input values for antecedents
tipping_sim.input['service'] = 8.5
tipping_sim.input['food'] = 6.7

# Compute output
tipping_sim.compute()

# Print output
print(tipping_sim.output['tip'])
tip.view(sim=tipping_sim)
