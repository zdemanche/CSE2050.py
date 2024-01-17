import unittest
from hw10 import Patient, PriorityQueue, EmergencyRoom

class TestEmergencyRoomSimulation(unittest.TestCase):
    def test_patient_creation(self):
        patient = Patient("1", 5)
        self.assertEqual(patient.name, "1")
        self.assertEqual(patient.severity, 5)

    def test_priority_queue_push_pop(self):
        queue = PriorityQueue()
        patient1 = Patient("1", 5)
        patient2 = Patient("2", 7)
        queue.push(patient1)
        queue.push(patient2)
        self.assertEqual(queue.pop(), patient2)
        self.assertEqual(queue.pop(), patient1)

    def test_emergency_room_simulation(self):
        er = EmergencyRoom()
        patient1 = Patient("1", 5)
        patient2 = Patient("2", 7)
        er.admit_patient(patient1)
        er.admit_patient(patient2)
        er.treat_patient()
        er.treat_patient()
        with self.assertRaises(IndexError):
            er.treat_patient()

if __name__ == '__main__':
    unittest.main()
