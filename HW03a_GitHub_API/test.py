import unittest
from input import getRepoInformationByID


class TestGetRepoInformationByID(unittest.TestCase):
    
    def test_invalid_input_type(self):
        """Test that function raises error for non string input"""
        with self.assertRaises(TypeError) as context:
            getRepoInformationByID(123)
        self.assertEqual(str(context.exception), "Expected a string. Incorrect Type")
        
        with self.assertRaises(TypeError) as context:
            getRepoInformationByID(['user'])
        self.assertEqual(str(context.exception), "Expected a string. Incorrect Type")
    
    def test_johan0214_actual_response(self):
        """Test with actual GitHub user Johan0214"""
        result = getRepoInformationByID("Johan0214")
        
        # Split the result into lines for easier assertion
        lines = result.split('\n')
        
        # Check that we have the expected number of repositories
        self.assertEqual(len(lines), 2)
        
        # Check that the output contains the expected repositories
        self.assertIn("Repo: CompleteAbstractFactory Number of commits: 2", result)
        self.assertIn("Repo: SSW345 Number of commits: 6", result)
    
    def test_output_format(self):
        """Test that the output format is correct"""
        result = getRepoInformationByID("Johan0214")
        
        # Check that each line follows the expected format
        lines = result.split('\n')
        for line in lines:
            self.assertTrue(line.startswith("Repo: "))
            self.assertIn(" Number of commits: ", line)
            
            # Extract the commit count and verify it's a number
            parts = line.split(" Number of commits: ")
            self.assertEqual(len(parts), 2)
            commit_count = parts[1]
            self.assertTrue(commit_count.isdigit())


if __name__ == '__main__':
    unittest.main()