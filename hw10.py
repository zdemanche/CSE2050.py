class Patient:
    def __init__(self, name, severity):
        self.name = name
        self.severity = severity

    def __str__(self):
        return f"Patient-{self.name} with severity {self.severity}"

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, patient):
        self.queue.append(patient)
        self._upheap(len(self.queue) - 1)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty priority queue")
        self.queue[0], self.queue[-1] = self.queue[-1], self.queue[0]
        patient = self.queue.pop()
        self._downheap(0)
        return patient

    def _upheap(self, idx):
        parent = (idx - 1) // 2
        if idx > 0 and self.queue[idx].severity > self.queue[parent].severity:
            self.queue[idx], self.queue[parent] = self.queue[parent], self.queue[idx]
            self._upheap(parent)

    def _downheap(self, idx):
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2
        if left < len(self.queue) and self.queue[left].severity > self.queue[largest].severity:
            largest = left
        if right < len(self.queue) and self.queue[right].severity > self.queue[largest].severity:
            largest = right
        if largest != idx:
            self.queue[idx], self.queue[largest] = self.queue[largest], self.queue[idx]
            self._downheap(largest)

    def is_empty(self):
        return len(self.queue) == 0

class EmergencyRoom:
    def __init__(self):
        self.waiting_room = PriorityQueue()

    def admit_patient(self, patient):
        self.waiting_room.push(patient)
        print(f"{patient} admitted to the emergency room")

    def treat_patient(self):
        if self.waiting_room.is_empty():
            raise IndexError("No patients to treat.")
        patient = self.waiting_room.pop()
        print(f"Treating {patient}")
