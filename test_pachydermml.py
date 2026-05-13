# test_pachydermml.py
"""
Tests for PachydermML module.
"""

import unittest
from pachydermml import PachydermML

class TestPachydermML(unittest.TestCase):
    """Test cases for PachydermML class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PachydermML()
        self.assertIsInstance(instance, PachydermML)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PachydermML()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
