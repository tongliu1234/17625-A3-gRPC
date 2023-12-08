# 17625-A3-gRPC

Name: Tong Liu

AndrewID: tl3

github-link:https://github.com/tongliu1234/17625-A3-gRPC



#### 1. Protocol Buffer definitions

1. User 

   ```protobuf
   message User {
     string user_id = 1;
   }
   ```

   

2. Post

   ```protobuf
   message Post {
     string title = 1;
     string text = 2;
     string video_url = 3;
     string image_url = 4;
     string author = 5;
     int32 score = 6;
     enum State {
       NORMAL = 0;
       LOCKED = 1;
       HIDDEN = 2;
     }
     State post_state = 7;
     int64 publication_date = 8;
     string post_id = 9;
   }
   ```

   

3. Comment

   ```protobuf
   message Comment {
     string text = 1;
     string author = 2;
     int32 score = 3;
     enum State {
       NORMAL = 0;
       HIDDEN = 1;
     }
     State comment_state = 4;
     int64 publication_date = 5;
     string comment_id = 6;
     string parent_post_id = 7;
     st
   ```

   

4. **Subreddit**(extra credit)

   ```protobuf
   message Subreddit {
     string name = 1;
     enum Visibility {
       PUBLIC = 0;
       PRIVATE = 1;
       HIDDEN = 2;
     }
     Visibility visibility = 2;
     repeated string tags = 3;
   }
   ```

   

5. Reddit

```protobuf
message PostRequest {
  string post_id = 1;
}

message PostResponse {
  repeated Post posts = 1;
}

message CommentRequest {
  string comment_id = 1;
}

message CommentResponse {
  repeated Comment comments = 1;
}

message PostRequest2 {
  string post_id = 1;
  string n = 2;
}

message UpvotedCommentsResponse {
  repeated Comment upvoted_comments = 1;
}

message CommentBranchRequest {
  string comment_id = 1;
  int32 n = 2;
}

message CommentBranchResponse {
  repeated CommentThread comment_threads = 1;

  message CommentThread {
    Comment main_comment = 1;
    repeated Comment replies = 2;
  }
}

message UpdatesRequest {
  string post_id = 1;
  repeated string comment_ids = 2;
}

message UpdatesResponse {
  int32 post_score = 1;
  repeated CommentUpdate comment_updates = 2;

  message CommentUpdate {
    string comment_id = 1;
    int32 score = 2;
  }
}
```



#### 2. Service definitions

```protobuf
service RedditService {
  rpc CreatePost(Post) returns (Post);
  rpc UpvotePost(PostRequest) returns (Post);
  rpc DownvotePost(PostRequest) returns (Post);
  rpc RetrieveAllPosts(PostRequest) returns (PostResponse);
  rpc RetrievePostContent(PostRequest) returns (Post);
  rpc CreateComment(Comment) returns (Comment);
  rpc UpvoteComment(CommentRequest) returns (Comment);
  rpc DownvoteComment(CommentRequest) returns (Comment);
  rpc RetrieveAllComments(PostRequest) returns (CommentResponse);
  rpc RetrieveUpvotedComments(PostRequest2) returns (UpvotedCommentsResponse);
  rpc ExpandCommentBranch(CommentBranchRequest) returns (CommentBranchResponse);
  
  // Extra Credit
  rpc MonitorUpdates(UpdatesRequest) returns (stream UpdatesResponse);
}
```



#### 3.Storage backend 

A straightforward in-memory storage approach is employed as the backend for storing entities such as posts, comments, users, and potentially subreddits. The in-memory storage is designed to be simple and suitable for test purposes, as specified in the assignment. Entities are stored within Python dictionaries, where each entity type corresponds to a separate dictionary. This choice facilitates rapid development and testing, as it allows for quick retrieval and manipulation of data during API service interactions. 



#### 4.Links 

Server: 

python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. Reddit.proto

python server.py

