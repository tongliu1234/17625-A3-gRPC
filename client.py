import grpc

from Reddit_pb2 import (
    Comment,
    CommentBranchRequest,
    CommentBranchResponse,
    CommentRequest,
    Post,
    PostRequest,
    UpdatesRequest,
    UpdatesResponse,
    UpvotedCommentsResponse,
)
from Reddit_pb2_grpc import RedditServiceStub


class RedditApiClient:
    def __init__(self, server_address):
        self.channel = grpc.insecure_channel(server_address)
        self.stub = RedditServiceStub(self.channel)

    def create_post(self, post_data):
        return self.stub.CreatePost(post_data)

    def upvote_post(self, post_id):
        return self.stub.UpvotePost(post_id)

    def downvote_post(self, post_id):
        return self.stub.DownvotePost(post_id)

    def retrieve_post_content(self, post_id):
        return self.stub.RetrievePostContent(post_id)

    def create_comment(self, comment_data):
        return self.stub.CreateComment(comment_data)

    def upvote_comment(self, comment_id):
        return self.stub.UpvoteComment(comment_id)

    def downvote_comment(self, comment_id):
        return self.stub.DownvoteComment(comment_id)

    def retrieve_upvoted_comments(self, post_request_2):
        return self.stub.RetrieveUpvotedComments(post_request_2)

    def expand_comment_branch(self, comment_branch_request):
        return self.stub.ExpandCommentBranch(comment_branch_request)

    def monitor_updates(self, updates_request):
        return self.stub.MonitorUpdates(updates_request)

    def close(self):
        self.channel.close()


if __name__ == "__main__":
    client = RedditApiClient("localhost:50051")

    # Create a post
    post_data = Post(title="Sample Post", text="This is a sample post.", author="user1")
    created_post = client.create_post(post_data)
    print("Created Post:", created_post)

    # Upvote the created post
    upvoted_post = client.upvote_post(PostRequest(post_id=created_post.post_id))
    print("Upvoted Post:", upvoted_post)

    # Downvote the created post
    downvoted_post = client.downvote_post(PostRequest(post_id=created_post.post_id))
    print("Downvoted Post:", downvoted_post)

    # Retrieve post content
    retrieved_post = client.retrieve_post_content(
        PostRequest(post_id=created_post.post_id)
    )
    print("Retrieved Post:", retrieved_post)

    # Create a comment
    comment_data = Comment(
        text="Great post!", author="sample_user", parent_post_id=created_post.post_id
    )
    created_comment = client.create_comment(comment_data)
    print("Created Comment:", created_comment)

    # Upvote the created comment
    upvoted_comment = client.upvote_comment(
        CommentRequest(comment_id=created_comment.comment_id)
    )
    print("Upvoted Comment:", upvoted_comment)

    # Downvote the created comment
    downvoted_comment = client.downvote_comment(
        CommentRequest(comment_id=created_comment.comment_id)
    )
    print("Downvoted Comment:", downvoted_comment)

    # Close the client channel when done
    client.close()
