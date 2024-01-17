from LinkedList import LLNode, LinkedList
import unittest

class TestLinkedList(unittest.TestCase):
    def test_dosctrings(self):
        """Searches for docstrings"""

        # note the use of subTest, a nice way of generating multiple unittests
        # with minor changes
        for method in [LLNode.add_last, LLNode.sum_all, LLNode.reverse]:
            with self.subTest(method=method):
                self.assertIsNotNone(method.__doc__, f"{method.__name__} missing a docstring")

    def test_init_with_items(self):
        """Tests that we can initialize with or without items"""
        # init empty
        LL1 = LinkedList()
        self.assertEqual(repr(LL1), repr(None))
        self.assertEqual(len(LL1), 0)

        # init w/ string
        LL2 = LinkedList("abcde")
        self.assertEqual(repr(LL2), "a ->b ->c ->d ->e")
        self.assertEqual(len(LL2), 5)

        # init w/ list of objects
        LL3 = LinkedList(['hello', 'goodbye', (1, 2, 3), 4.7])
        self.assertEqual(repr(LL3), "hello ->goodbye ->(1, 2, 3) ->4.7")
        self.assertEqual(len(LL3), 4)

    def test_af_len_repr(self):
        """Ensures add_first works and updates len appropriately"""
        # Set up
        n = 10
        LL = LinkedList()

        # Create list
        for i in range(n):
            self.assertEqual(len(LL), i)
            LL.add_first(i)

        # Test
        self.assertEqual(repr(LL), "9 ->8 ->7 ->6 ->5 ->4 ->3 ->2 ->1 ->0")

    def test_get_tail(self):
        """Should return item in tail node"""
        LL1 = LinkedList()
        self.assertIsNone(LL1.get_tail())

        LL2 = LinkedList("abcde")
        self.assertEqual(LL2.get_tail(), "e")

    def test_al_len_repr(self):
        """Ensures add_last works and updates len appropriately"""
        # Set up
        n = 10
        LL = LinkedList()

        # Create list
        for i in range(n):
            self.assertEqual(len(LL), i)
            LL.add_last(i)

        # Test
        self.assertEqual(repr(LL), "0 ->1 ->2 ->3 ->4 ->5 ->6 ->7 ->8 ->9")

    def test_afrf_len(self):
        """Sequentially adds first, then removes first"""
        # Set up
        n = 10
        LL = LinkedList()

        # Create list
        for i in range(n):
            self.assertEqual(len(LL), i)
            LL.add_first(i)

        # Test repr
        self.assertEqual(repr(LL), "9 ->8 ->7 ->6 ->5 ->4 ->3 ->2 ->1 ->0")
        
        # Test remove_fist
        for i in range(n):
            self.assertEqual(len(LL), n-i)
            self.assertEqual(LL.remove_first(), n-1-i)

    def test_alrf_len(self):
        """Sequentially adds last, then removes first"""
        # Set up
        n = 10
        LL = LinkedList()

        # Create list
        for i in range(n):
            self.assertEqual(len(LL), i)
            LL.add_last(i)

        # Test repr
        self.assertEqual(repr(LL), "0 ->1 ->2 ->3 ->4 ->5 ->6 ->7 ->8 ->9")
        
        # Test remove_fist
        for i in range(n):
            self.assertEqual(len(LL), n-i)
            self.assertEqual(LL.remove_first(), i)

    def test_sum_all(self):
        """tests that we can sum as expected"""
        # setup
        # note that we can pass any iterator to init, including a range() object
        # this is an example of python's polymorphism - the same for loop
        # works on any object that supports iteration
        LL = LinkedList(range(10))

        # test
        self.assertEqual(LL.sum_all(), 45)

    def test_reverse(self):
        """tests reverse method"""
        # Set up
        n = 10
        LL = LinkedList()

        # Create list
        for i in range(n):
            self.assertEqual(len(LL), i)
            LL.add_first(i)

        # Test
        self.assertEqual(repr(LL), "9 ->8 ->7 ->6 ->5 ->4 ->3 ->2 ->1 ->0")

        # Reverse
        LL.reverse()
        self.assertEqual(len(LL), n)
        self.assertEqual(repr(LL), "0 ->1 ->2 ->3 ->4 ->5 ->6 ->7 ->8 ->9")



unittest.main()