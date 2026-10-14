class accountpinsafetychecker:
    def __init__(self, owner: str, pin: str):
        self.owner = owner
        # Private attribute using double underscore name mangling
        self.__pin = pin

    # Setter method to update the private PIN safely
    def set_pin(self, old_pin: str, new_pin: str):
        if old_pin == self.__pin:
            if len(new_pin) == 4 and new_pin.isdigit():
                self.__pin = new_pin
                print("pin successfully updated.")
            else:
                print("error: new pin must be a 4-digit number.")
        else:
            print("error: old pin is incorrect.")

    # Getter method if you need to check safety/length without exposing raw PIN recklessly
    def get_pin_length(self):
        return len(self.__pin)

    # Special __str__ function to control how the object displays with print()
    def __str__(self):
        return f"account Owner: {self.owner} | pin Status: [protected]"


# --- Testing the Implementation ---

# 1. Create account data with a private PIN
account = accountpinsafetychecker("Alice", "1234")

# 2. Test how private attributes behave outside the class
try:
    print(account.__pin)  # This will raise an AttributeError
except AttributeError as e:
    print(f"direct access attempt failed: {e}")

# (Optional note: Python mangles private attributes to _ClassName__pin)
print("accessed via name mangling (not recommended):", account._accountpinsafetychecker__pin)

# 3. Update private data safely using the setter method
account.set_pin("1234", "5678")  # Valid update
account.set_pin("9999", "1111")  # Invalid old PIN test

# 4. Use the __str__ special function with print()
print(account)