from Reddit_pb2 import Comment, Post

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
comments = {
    "1": Comment(
        text="This is the first comment",
        author="user1",
        score=0,
        comment_state=Comment.NORMAL,
        comment_id="1",
        parent_post_id="1",
        parent_comment_id="none",
    ),
    "2": Comment(
        text="This is the second comment",
        author="user2",
        score=5,
        comment_state=Comment.NORMAL,
        comment_id="2",
        parent_post_id="1",
        parent_comment_id="none",
    ),
    "3": Comment(
        text="This is the third comment",
        author="user3",
        score=10,
        comment_state=Comment.NORMAL,
        comment_id="3",
        parent_post_id="1",
        parent_comment_id="1",
    ),
    "4": Comment(
        text="This is the forth comment",
        author="user3",
        score=10,
        comment_state=Comment.NORMAL,
        comment_id="4",
        parent_post_id="1",
        parent_comment_id="3",
    ),
}
