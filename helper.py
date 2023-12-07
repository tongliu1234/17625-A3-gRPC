from dummy_data import comments, posts
from Reddit_pb2 import Comment, CommentBranchResponse


def retrive_top_n_comments(arr, n):
    x = 0
    res = []
    # Bubble sort
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j].score > arr[j + 1].score:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        res.append(arr[len(arr) - i - 1])
        x += 1
        if x == n:
            break
    return res


def expand_comment_branch(comment_id, n):
    response = CommentBranchResponse()

    # Get n top children comments
    n_top_children_comments = retrieve_n_top_comments_with_commentId(comment_id, n)

    # Get n top children comments of each child comment
    for child_comment in n_top_children_comments:
        # Create CommentThread instances and populate them with comments
        comment_thread = response.comment_threads.add()
        comment_thread.main_comment.CopyFrom(child_comment)
        child_child_comments = retrieve_n_top_comments_with_commentId(
            child_comment.comment_id, n
        )
        comment_thread.replies.extend(child_child_comments)
    return response


def retrieve_n_top_comments_with_commentId(comment_id, n):
    children_comments = [
        comment
        for comment in comments.values()
        if comment.parent_comment_id == comment_id
    ]
    n_top_children_comments = retrive_top_n_comments(children_comments, n)
    return n_top_children_comments
