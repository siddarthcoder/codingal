class accountpinsafetychecker:
    def __init__(self, owner: str, pin: str):
        self.owner = owner
        self.__pin = pin

    def set_pin(self, old_pin: str, new_pin: str):
        if old_pin == self.__pin:
            if len(new_pin) == 4 and new_pin.isdigit():
                self.__pin = new_pin
                print("pin successfully updated.")
            else:
                print("error: new pin must be a 4-digit number.")
        else:
            print("error: old pin is incorrect.")

    def get_pin_length(self):
        return len(self.__pin)

    def __str__(self):
        return f"account Owner: {self.owner} | pin Status: [protected]"


account = accountpinsafetychecker("Alice", "1234")

try:
    print(account.__pin)  
except AttributeError as e:
    print(f"direct access attempt failed: {e}")

print("accessed via name mangling (not recommended):", account._accountpinsafetychecker__pin)

account.set_pin("1234", "5678")  
account.set_pin("9999", "1111")  

print(account)