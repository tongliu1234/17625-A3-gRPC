import unittest
from unittest.mock import Mock, patch

from client import RedditApiClient
from Reddit_pb2 import Comment, CommentBranchResponse, Post, UpvotedCommentsResponse
from test_high_level_func import retrieve_most_upvoted_reply


class TestRetrieveMostUpvotedReply(unittest.TestCase):
    @patch("client.RedditApiClient")
    def test_retrieve_most_upvoted_reply(self, mock_api_client):
        # Set up mock responses for the API client
        post_id = "123"
        mock_post = Post(text="Mock post content", score=10, post_id=post_id)
        mock_upvoted_comments_response = UpvotedCommentsResponse(
            upvoted_comments=[Comment(comment_id="1", score=5)]
        )
        mock_comment_branch_response = CommentBranchResponse(
            comment_threads=[
                {
                    "main_comment": Comment(comment_id="1", score=5),
                    "replies": [
                        Comment(comment_id="2", score=8),
                        Comment(comment_id="3", score=7),
                    ],
                }
            ]
        )

        mock_api_instance = Mock(spec=RedditApiClient)
        mock_api_instance.retrieve_post_content.return_value = mock_post
        mock_api_instance.retrieve_upvoted_comments.return_value = (
            mock_upvoted_comments_response
        )
        mock_api_instance.expand_comment_branch.return_value = (
            mock_comment_branch_response
        )

        # Set the mock instance as the return value when the RedditApiClient is instantiated
        mock_api_client.return_value = mock_api_instance

        # Call the function with the mock API client
        result = retrieve_most_upvoted_reply(mock_api_instance, post_id)

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(
            result.comment_id, "2"
        )  # Assuming comment_id="2" is the most upvoted reply

        print("Test passed")


if __name__ == "__main__":
    unittest.main()
