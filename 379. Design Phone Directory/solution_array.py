class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # List to mark if a slot is available.
        self.is_slot_available = [True] * maxNumbers

    def get(self) -> int:
        # Find an empty slot and return the respective index.
        index = next((i for i, available in enumerate(self.is_slot_available) if available), -1)
        if index != -1:
            self.is_slot_available[index] = False
        return index

    def check(self, number: int) -> bool:
        # Check if the slot at index 'number' is available or not.
        return self.is_slot_available[number]

    def release(self, number: int) -> None:
        # Mark the slot at index 'number' as available.
        self.is_slot_available[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
