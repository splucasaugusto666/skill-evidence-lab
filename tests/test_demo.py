import unittest
import demo


class DemoTest(unittest.TestCase):
    def test_isolated_demo(self):
        result = demo.run()
        self.assertIn('Dry run: no files created', result)
        self.assertIn('Modified copy: checksum mismatch detected', result)
        self.assertIn('Temporary workspace removed; no agent executed', result)
