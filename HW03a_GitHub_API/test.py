import unittest
from unittest.mock import patch, Mock
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
    
    @patch('input.requests.get')
    def test_successful_repo_and_commits_retrieval(self, mock_get):
        """Test successful retrieval of repos and commits"""
        # Mock response for repos list
        mock_repos_response = Mock()
        mock_repos_response.json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        
        # Mock response for commits (3 commits for repo1, 5 for repo2)
        mock_commits_repo1 = Mock()
        mock_commits_repo1.json.return_value = [
            {"sha": "abc123"},
            {"sha": "def456"},
            {"sha": "ghi789"}
        ]
        
        mock_commits_repo2 = Mock()
        mock_commits_repo2.json.return_value = [
            {"sha": "111"},
            {"sha": "222"},
            {"sha": "333"},
            {"sha": "444"},
            {"sha": "555"}
        ]
        
        # Set up the order of the responses (repos first, commits after)
        mock_get.side_effect = [
            mock_repos_response,
            mock_commits_repo1,
            mock_commits_repo2
        ]
        
        result = getRepoInformationByID("testuser")
        
        # Verify the result
        expected_output = "Repo: repo1 Number of commits: 3\nRepo: repo2 Number of commits: 5"
        self.assertEqual(result, expected_output)
        
        # Verify API calls were made correctly
        self.assertEqual(mock_get.call_count, 3)
    
    @patch('input.requests.get')
    def test_single_repo_single_commit(self, mock_get):
        """Test with single repo having single commit"""
        mock_repos_response = Mock()
        mock_repos_response.json.return_value = [
            {"name": "single-repo"}
        ]
        
        mock_commits_response = Mock()
        mock_commits_response.json.return_value = [
            {"sha": "xyz789"}
        ]
        
        mock_get.side_effect = [mock_repos_response, mock_commits_response]
        
        result = getRepoInformationByID("singleuser")
        
        expected_output = "Repo: single-repo Number of commits: 1"
        self.assertEqual(result, expected_output)
    
    @patch('input.requests.get')
    def test_empty_repos_list(self, mock_get):
        """Test with user having no repositories"""
        mock_response = Mock()
        mock_response.json.return_value = []
        mock_get.return_value = mock_response
        
        result = getRepoInformationByID("emptyuser")
        
        self.assertEqual(result, "")
        mock_get.assert_called_once()


if __name__ == '__main__':
    unittest.main()