class Reactor:
  def __init__(self, name, max_power, max_temperature, max_coolant, current_power=0, current_temperature=0, current_coolant=0, maintenance_status=False, repair_status=False):
    # Other attributes

    self.maintenance_status = maintenance_status
    self.repair_status = repair_status
    self.name = name
    self.max_power = max_power
    self.max_temperature = max_temperature
    self.max_coolant = max_coolant
    self.current_power = current_power
    self.current_temperature = current_temperature
    self.current_coolant = current_coolant

  # Method to increase the current power of the reactor
  def increase_power(self, amount):
    self.current_power += amount
    if self.current_power > self.max_power:
      self.current_power = self.max_power
    print(f"{self.name} reactor power increased by {amount}. Current power: {self.current_power}")

  # Method to decrease the current power of the reactor
  def decrease_power(self, amount):
    self.current_power -= amount
    if self.current_power < 0:
      self.current_power = 0
    print(f"{self.name} reactor power decreased by {amount}. Current power: {self.current_power}")

  # Method to increase the temperature of the reactor
  # Method to increase the current power of the reactor
  def increase_power(self, amount):
    # Calculate the new temperature if the power is increased
    new_temperature = self.current_temperature + (amount * 0.1)

    # Check if the new temperature would exceed the safety limit
    if new_temperature > self.max_temperature:
      # Reject the increase in power
      print(f"{self.name} reactor power increase rejected. Safety limit exceeded.")
    else:
      # Increase the power and temperature of the reactor
      self.current_power += amount
      self.current_temperature = new_temperature
      print(f"{self.name} reactor power increased by {amount}. Current power: {self.current_power}, Current temperature: {self.current_temperature}")

  # Method to decrease the temperature of the reactor
  def decrease_temperature(self, amount):
    self.current_temperature -= amount
    if self.current_temperature < 0:
      self.current_temperature = 0
    print(f"{self.name} reactor temperature decreased by {amount}. Current temperature: {self.current_temperature}")

  # Method to increase the coolant level of the reactor
  def increase_coolant(self, amount):
    self.current_coolant += amount
    if self.current_coolant > self.max_coolant:
      self.current_coolant = self.max_coolant
    print(f"{self.name} reactor coolant level increased by {amount}. Current coolant level: {self.current_coolant}")

  # Method to decrease the coolant level of the reactor
  def decrease_coolant(self, amount):
    self.current_coolant -= amount
    if self.current_coolant < 0:
      self.current_coolant = 0
    print(f"{self.name} reactor coolant level decreased by {amount}. Current coolant level: {self.current_coolant}")

    def meltdown(self):
        self.current_temperature = self.max_temperature
        print(f"{self.name} reactor has melted down. Current temperature: {self.current_temperature}")

    # Method to schedule maintenance for the reactor
  def schedule_maintenance(self):
    # Check if there are no other reactors offline
    if self.power_plant.check_reactor_status():
      self.maintenance_status = True
      print(f"{self.name} reactor maintenance scheduled.")
    else:
      print(f"{self.name} reactor maintenance not scheduled. Other reactors are offline.")

  # Method to schedule repair for the reactor
  def schedule_repair(self):
    # Check if there are no other reactors offline
    if self.power_plant.check_reactor_status():
      self.repair_status = True
      print(f"{self.name} reactor repair scheduled.")
    else:
      print(f"{self.name} reactor repair not scheduled. Other reactors are offline.")

  # Method to schedule repair for the reactor
  def schedule_repair(self):
    self.repair_status = True
    print(f"{self.name} reactor repair scheduled.")

  # Method to complete repair for the reactor
  def complete_repair(self):
    self.repair_status = False
    print(f"{self.name} reactor repair completed.")


# Define the power plant class
class PowerPlant:
  def __init__(self, reactors):
    self.reactors = reactors

  # Method to increase the power of all the reactors
  def increase_power(self, amount):
    for reactor in self.reactors:
      reactor.increase_power(amount)

  # Method to decrease the power of all the reactors
  def decrease_power(self, amount):
    for reactor in self.reactors:
      reactor.decrease_power(amount)

  def check_reactor_status(self):
    # Loop through the reactors in the power plant
    for reactor in self.reactors:
      # Check if the reactor is currently undergoing maintenance or repair
      if reactor.maintenance_status or reactor.repair_status:
        return False

    return True

class PowerPlantSimulator:
  def __init__(self, power_plant):
    self.power_plant = power_plant
    self.time = 0

  # Method to simulate the passage of time
  def simulate_time(self, time_interval):
    self.time += time_interval
    print(f"Simulated {time_interval} seconds. Current time: {self.time}")

  # Method to increase the power of the reactors
  def increase_power(self, amount):
    self.power_plant.increase_power(amount)

  # Method to decrease the power of the reactors
  def decrease_power(self, amount):
    self.power_plant.decrease_power(amount)

  # Method to monitor the state of the power plant
  def monitor_state(self):
    print("Power plant state:")
    for reactor in self.power_plant.reactors:
      print(f"{reactor.name} - Power: {reactor.current_power}, Temperature: {reactor.current_temperature}, Coolant level: {reactor.current_coolant}")

# Create four reactors
reactor1 = Reactor("Reactor 1", 1000, 1000, 1000)
reactor2 = Reactor("Reactor 2", 1000, 1000, 1000)
reactor3 = Reactor("Reactor 3", 1000, 1000, 1000)
reactor4 = Reactor("Reactor 4", 1000, 1000, 1000)

# Create a power plant with four reactors
power_plant = PowerPlant([reactor1, reactor2, reactor3, reactor4])

# Create a power plant simulator with the power plant
simulator = PowerPlantSimulator(power_plant)

# Simulate the passage of time
simulator.simulate_time(60)

# Increase the power of the reactors
simulator.increase_power(500)

# Simulate the passage of time
simulator.simulate_time(60)

# Decrease the power of the reactors
simulator.decrease_power(250)


# Schedule maintenance for a reactor
reactor1.schedule_maintenance()

# Complete the scheduled maintenance
reactor1.complete_maintenance()

# Schedule repair for a reactor
reactor2.schedule_repair()

# Complete the scheduled repair
reactor2.complete_repair()