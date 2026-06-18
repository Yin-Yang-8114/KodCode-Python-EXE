# section 1 and 2.
agent_name = str(input('Enter your agent name: '))
mission_code = int (input('Enter your mission code: '))
distance_to_target = float(input('Enter your distance to target: '))
mission_active_status = bool(int(input('Enter your mission status: ')))
# section 3.
print(f'You are {agent_name} the spisel agent  \nmission code {mission_code}  \ndistance to target {distance_to_target} KM  \nmission status : {mission_active_status}')
# section 4
print(f'agent name type is : {(type(agent_name))} \n mission active status type: {(type(mission_active_status))}\ndistance to target type: {(type(distance_to_target))}\n mission status type: {(type(mission_active_status))}')
# section 5
travel_distance_feature = distance_to_target * 2
# section 6
print(f'the all distance there and back is : {travel_distance_feature}')
fuel_usage_per_KM = 1.5
fuel_estimation = fuel_usage_per_KM * travel_distance_feature
print(f'you used {fuel_estimation} liters fuel ')
# section 7
total_fuel = 1000
remaining_fuel = total_fuel - fuel_estimation
print(f'fuel remines in your tank is {remaining_fuel} ')
# section 8
countdown_conversion = int(input('Enter conversion time in SEC : '))
print(f'Conversion time in seconds is {countdown_conversion}\n conversition time in minutes is {(countdown_conversion/60)}\n conversetion time in hours is {(int(countdown_conversion/60/60))}')
# section 9
distance_in_miles = distance_to_target * 0.621371192
print(f'distance to target in miles is {distance_in_miles} miles')
# section 10
old_agent_name = agent_name
agent_name = str(input('Enter your NEW agent name: '))
print(f'old agent name is {old_agent_name}\nnew agent name is {agent_name}')