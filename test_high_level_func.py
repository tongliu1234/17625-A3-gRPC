from Reddit_pb2 import (
    CommentBranchRequest,
    CommentBranchResponse,
    PostRequest,
    PostRequest2,
    UpvotedCommentsResponse,
)


def retrieve_most_upvoted_reply(api_client, post_id):
    # Step 1: Retrieve the post
    post = api_client.retrieve_post_content(PostRequest(post_id=post_id))

    if not post:
        return None

    # Step 2: Retrieve most upvoted comments under the post
    upvoted_comments_response = api_client.retrieve_upvoted_comments(
        PostRequest2(post_id=post_id, n="2")
    )
    upvoted_comments = upvoted_comments_response.upvoted_comments

    if not upvoted_comments:
        return None

    # Step 3: Find the most upvoted comment
    most_upvoted_comment = max(upvoted_comments, key=lambda comment: comment.score)

    # Step 4: Expand the most upvoted comment
    comment_branch_request = CommentBranchRequest(
        comment_id=most_upvoted_comment.comment_id, n=1
    )
    comment_branch_response = api_client.expand_comment_branch(comment_branch_request)
    comment_thread = comment_branch_response.comment_threads[0]

    # Step 5: Return the most upvoted reply under the most upvoted comment
    most_upvoted_reply = max(
        comment_thread.replies, key=lambda reply: reply.score, default=None
    )
    return most_upvoted_reply
