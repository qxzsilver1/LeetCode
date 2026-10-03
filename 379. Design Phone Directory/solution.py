class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slots_available = set(range(maxNumbers))

    def get(self) -> int:
        # If the hash set is empty it means no slot is available.
        if not self.slots_available:
            return -1

        # Otherwise, pop and return the first element from the hash set.
        return self.slots_available.pop()

    def check(self, number: int) -> bool:
        # Check if the slot at index 'number' is available or not.
        return number in self.slots_available

    def release(self, number: int) -> None:
        # Mark the slot 'number' as available.
        self.slots_available.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
