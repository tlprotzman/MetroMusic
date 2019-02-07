import pattern
import unittest


class TestPattern(unittest.TestCase):
    def test_str_conversion(self):
        p = pattern.Pattern(4, 4, 2)
        self.assertEqual(str(p), "000| - - - - - - - - - - - - - - - - ", "Empty Pattern")
        self.assertTrue(p.add_note(0, 0))
        self.assertTrue(p.add_note(0, 4))
        self.assertTrue(p.add_note(0, 8))
        self.assertTrue(p.add_note(0, 12))
        self.assertEqual(str(p), "000| # - - - # - - - # - - - # - - - ", "Empty Pattern")
        p = pattern.Pattern(6, 1, 4)
        self.assertEqual(str(p), "000| - - - - - - ", "Empty Pattern")
        self.assertTrue(p.add_note(0, 0))
        self.assertTrue(p.add_note(1, 0))
        self.assertTrue(p.add_note(2, 0))
        self.assertTrue(p.add_note(3, 0))
        self.assertEqual(str(p), "000| # - - - - - \n001| # - - - - - \n002| # - - - - - \n003| # - - - - - ",
                         "MultiNote test")
        self.assertEqual(repr(p), "000| # - - - - - \n001| # - - - - - \n002| # - - - - - \n003| # - - - - - ",
                         "MultiNote test")

    def test_add_note(self):
        p = pattern.Pattern(4, 4, 2)
        self.assertTrue(p.add_note(0, 0))
        self.assertTrue(p.add_note(1, 0))
        self.assertFalse(p.add_note(0, 0), "Duplicate note")
        self.assertFalse(p.add_note(3, 0), "Note out of range")
        self.assertFalse(p.add_note(0, 99), "Div out of range")
        self.assertFalse(p.add_note(-1, 0), "Negative note")
        self.assertFalse(p.add_note(0, -1), "Negative div")

    def test_remove_note(self):
        p = pattern.Pattern(1, 4, 2)
        self.assertTrue(p.add_note(0, 0))
        self.assertFalse(p.remove_note(2, 0), "Note out of range")
        self.assertFalse(p.remove_note(0, 20), "Div out of range")
        self.assertFalse(p.remove_note(-1, 0), "Negative note")
        self.assertFalse(p.remove_note(0, -1), "Negative div")
        self.assertTrue(p.remove_note(0, 0))
        self.assertFalse(p.remove_note(0, 0), "Note already removed")

    def test_notes_at_div(self):
        p = pattern.Pattern(1, 1, 5)
        self.assertSetEqual(p.notes_at_div(0), set())
        p.add_note(0, 0)
        p.add_note(2, 0)
        p.add_note(4, 0)
        self.assertSetEqual(p.notes_at_div(0), {0, 2, 4})
        self.assertIsNone(p.notes_at_div(1))


if __name__ == '__main__':
    unittest.main()
