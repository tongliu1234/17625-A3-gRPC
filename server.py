import time
from concurrent import futures

import grpc

from Reddit_pb2 import (
    Comment,
    CommentBranchRequest,
    CommentBranchResponse,
    Post,
    PostResponse,
    UpdatesRequest,
    UpdatesResponse,
    UpvotedCommentsResponse,
)
from Reddit_pb2_grpc import RedditServiceServicer, add_RedditServiceServicer_to_server

# Dummy in-memory storage
posts = {
    "1": Post(
        title="First post(Default)",
        text="This is the first post",
        author="user1",
        video_url="#",
        score=0,
        post_state=Post.NORMAL,
        post_id="1",
    ),
}
comments = {}


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


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_RedditServiceServicer_to_server(RedditServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started. Listening on port 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
