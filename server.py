import time
from concurrent import futures

import grpc

from dummy_data import comments, posts
from helper import expand_comment_branch, retrive_top_n_comments
from Reddit_pb2 import (
    Comment,
    CommentBranchRequest,
    CommentBranchResponse,
    CommentResponse,
    Post,
    PostResponse,
    UpdatesRequest,
    UpdatesResponse,
    UpvotedCommentsResponse,
)
from Reddit_pb2_grpc import RedditServiceServicer, add_RedditServiceServicer_to_server


class RedditServicer(RedditServiceServicer):
    def CreatePost(self, request, context):
        # Assuming a unique post_id is generated for each post
        post_id = str(len(posts) + 1)
        # print(request)
        request.post_id = post_id
        posts[post_id] = request
        return request

    def RetrieveAllPosts(self, request, context):
        # print(posts)
        return PostResponse(posts=[post for post in posts.values()])

    def UpvotePost(self, request, context):
        # print(request)
        post = posts[request.post_id]
        post.score += 1
        return post

    def DownvotePost(self, request, context):
        post = posts[request.post_id]
        post.score -= 1
        return post

    def RetrievePostContent(self, request, context):
        return posts[request.post_id]

    def CreateComment(self, request, context):
        # Assuming a unique comment_id is generated for each comment
        comment_id = str(len(comments) + 1)
        request.comment_id = comment_id
        comments[comment_id] = request
        return request

    def RetrieveAllComments(self, request, context):
        return CommentResponse(comments=[comment for comment in comments.values()])

    def UpvoteComment(self, request, context):
        comment = comments[request.comment_id]
        comment.score += 1
        return comment

    def DownvoteComment(self, request, context):
        comment = comments[request.comment_id]
        comment.score -= 1
        return comment

    def RetrieveUpvotedComments(self, request, context):
        # Retrieve list of comments under post
        l = [
            comment
            for comment in comments.values()
            if comment.parent_post_id == request.post_id
        ]
        # print(bubble_sort(l, 2))
        return UpvotedCommentsResponse(
            upvoted_comments=retrive_top_n_comments(l, int(request.n))
        )

    def ExpandCommentBranch(self, request, context):
        return expand_comment_branch(request.comment_id, int(request.n))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RedditServiceServicer_to_server(RedditServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started. Listening on port 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
