class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        # Queue to store all available slots.
        self.slots_available_queue = deque(range(maxNumbers))

        # List to mark if a slot is available.
        self.is_slot_available = [True] * maxNumbers

    def get(self) -> int:
        # If the queue is empty, it means no slot is available.
        if not self.slots_available_queue:
            return -1

        # Otherwise, get the first available slot from the queue,
        # mark that slot as not available and return the slot.
        slot = self.slots_available_queue.popleft()
        self.is_slot_available[slot] = False
        return slot

    def check(self, number: int) -> bool:
        # Check if the slot at index 'number' is available or not.
        return self.is_slot_available[number]

    def release(self, number: int) -> None:
        # If the slot is already present in the queue, we don't do anything.
        if self.is_slot_available[number]:
            return

        # Otherwise, mark the slot 'number' as available.
        self.slots_available_queue.append(number)
        self.is_slot_available[number] = True


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
