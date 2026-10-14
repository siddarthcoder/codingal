from abc import ABC, abstractmethod


class SmartDevice(ABC):

  def __init__(self, name: str):
    self.name = name
    self.is_on = False

  @abstractmethod
  def turn_on(self) -> None:
    """Turn on the smart device."""
    pass

  @abstractmethod
  def turn_off(self) -> None:
    """Turn off the smart device."""
    pass


class SmartLight(SmartDevice):

  def __init__(self, name: str, brightness: int = 100):
    super().__init__(name)
    self.brightness = brightness

  def turn_on(self) -> None:
    self.is_on = True
    print(f"[SmartLight] {self.name} is now ON at {self.brightness}% brightness.")

  def turn_off(self) -> None:
    self.is_on = False
    print(f"[SmartLight] {self.name} is now OFF.")


class SmartThermostat(SmartDevice):

  def __init__(self, name: str, temperature: float = 21.0):
    super().__init__(name, temperature)
    self.target_temperature = temperature

  def turn_on(self) -> None:
    self.is_on = True
    print(
        f"[SmartThermostat] {self.name} is active. Target set to"
        f" {self.target_temperature}°C."
    )

  def turn_off(self) -> None:
    self.is_on = False
    print(f"[SmartThermostat] {self.name} has been put to sleep.")


class SmartLock(SmartDevice):

  def __init__(self, name: str):
    super().__init__(name)
    self.locked = True

  def turn_on(self) -> None:
    # In this context, 'turn_on' can unlock the device
    self.is_on = True
    self.locked = False
    print(f"[SmartLock] {self.name} is UNLOCKED and active.")

  def turn_off(self) -> None:
    self.is_on = False
    self.locked = True
    print(f"[SmartLock] {self.name} is LOCKED and secured.")


def command_center_broadcast(devices: list[SmartDevice], action: str) -> None:
  print(f"\n--- Executing Command: {action.upper()} ---")
  for device in devices:
    if action == "on":
      device.turn_on()
    elif action == "off":
      device.turn_off()


if __name__ == "__main__":
  living_room_light = SmartLight("Living Room Light", brightness=80)
  hallway_thermostat = SmartThermostat("Hallway Thermostat", temperature=22.5)
  front_door_lock = SmartLock("Front Door Lock")

  all_devices: list[SmartDevice] = [
      living_room_light,
      hallway_thermostat,
      front_door_lock,
  ]

  command_center_broadcast(all_devices, "on")
  command_center_broadcast(all_devices, "off")