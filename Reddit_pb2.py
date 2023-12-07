# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Reddit.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cReddit.proto\"\x17\n\x04User\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\xe1\x01\n\x04Post\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x11\n\tvideo_url\x18\x03 \x01(\t\x12\x11\n\timage_url\x18\x04 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x05 \x01(\t\x12\r\n\x05score\x18\x06 \x01(\x05\x12\x1f\n\npost_state\x18\x07 \x01(\x0e\x32\x0b.Post.State\x12\x18\n\x10publication_date\x18\x08 \x01(\x03\x12\x0f\n\x07post_id\x18\t \x01(\t\"+\n\x05State\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06LOCKED\x10\x01\x12\n\n\x06HIDDEN\x10\x02\"\x98\x01\n\x07\x43omment\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x02 \x01(\t\x12\r\n\x05score\x18\x03 \x01(\x05\x12%\n\rcomment_state\x18\x04 \x01(\x0e\x32\x0e.Comment.State\x12\x18\n\x10publication_date\x18\x05 \x01(\x03\"\x1f\n\x05State\x12\n\n\x06NORMAL\x10\x00\x12\n\n\x06HIDDEN\x10\x01\"\x85\x01\n\tSubreddit\x12\x0c\n\x04name\x18\x01 \x01(\t\x12)\n\nvisibility\x18\x02 \x01(\x0e\x32\x15.Subreddit.Visibility\x12\x0c\n\x04tags\x18\x03 \x03(\t\"1\n\nVisibility\x12\n\n\x06PUBLIC\x10\x00\x12\x0b\n\x07PRIVATE\x10\x01\x12\n\n\x06HIDDEN\x10\x02\"\x1e\n\x0bPostRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\"$\n\x0cPostResponse\x12\x14\n\x05posts\x18\x01 \x03(\x0b\x32\x05.Post\"=\n\x17UpvotedCommentsResponse\x12\"\n\x10upvoted_comments\x18\x01 \x03(\x0b\x32\x08.Comment\"9\n\x14\x43ommentBranchRequest\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\"\xa2\x01\n\x15\x43ommentBranchResponse\x12=\n\x0f\x63omment_threads\x18\x01 \x03(\x0b\x32$.CommentBranchResponse.CommentThread\x1aJ\n\rCommentThread\x12\x1e\n\x0cmain_comment\x18\x01 \x01(\x0b\x32\x08.Comment\x12\x19\n\x07replies\x18\x02 \x03(\x0b\x32\x08.Comment\"6\n\x0eUpdatesRequest\x12\x0f\n\x07post_id\x18\x01 \x01(\t\x12\x13\n\x0b\x63omment_ids\x18\x02 \x03(\t\"\x92\x01\n\x0fUpdatesResponse\x12\x12\n\npost_score\x18\x01 \x01(\x05\x12\x37\n\x0f\x63omment_updates\x18\x02 \x03(\x0b\x32\x1e.UpdatesResponse.CommentUpdate\x1a\x32\n\rCommentUpdate\x12\x12\n\ncomment_id\x18\x01 \x01(\t\x12\r\n\x05score\x18\x02 \x01(\x05\x32\xfa\x03\n\rRedditService\x12\x1a\n\nCreatePost\x12\x05.Post\x1a\x05.Post\x12!\n\nUpvotePost\x12\x0c.PostRequest\x1a\x05.Post\x12#\n\x0c\x44ownvotePost\x12\x0c.PostRequest\x1a\x05.Post\x12/\n\x10RetrieveAllPosts\x12\x0c.PostRequest\x1a\r.PostResponse\x12#\n\x13RetrievePostContent\x12\x05.User\x1a\x05.Post\x12#\n\rCreateComment\x12\x08.Comment\x1a\x08.Comment\x12#\n\rUpvoteComment\x12\x08.Comment\x1a\x08.Comment\x12%\n\x0f\x44ownvoteComment\x12\x08.Comment\x1a\x08.Comment\x12\x41\n\x17RetrieveUpvotedComments\x12\x0c.PostRequest\x1a\x18.UpvotedCommentsResponse\x12\x44\n\x13\x45xpandCommentBranch\x12\x15.CommentBranchRequest\x1a\x16.CommentBranchResponse\x12\x35\n\x0eMonitorUpdates\x12\x0f.UpdatesRequest\x1a\x10.UpdatesResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Reddit_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_USER']._serialized_start=16
  _globals['_USER']._serialized_end=39
  _globals['_POST']._serialized_start=42
  _globals['_POST']._serialized_end=267
  _globals['_POST_STATE']._serialized_start=224
  _globals['_POST_STATE']._serialized_end=267
  _globals['_COMMENT']._serialized_start=270
  _globals['_COMMENT']._serialized_end=422
  _globals['_COMMENT_STATE']._serialized_start=391
  _globals['_COMMENT_STATE']._serialized_end=422
  _globals['_SUBREDDIT']._serialized_start=425
  _globals['_SUBREDDIT']._serialized_end=558
  _globals['_SUBREDDIT_VISIBILITY']._serialized_start=509
  _globals['_SUBREDDIT_VISIBILITY']._serialized_end=558
  _globals['_POSTREQUEST']._serialized_start=560
  _globals['_POSTREQUEST']._serialized_end=590
  _globals['_POSTRESPONSE']._serialized_start=592
  _globals['_POSTRESPONSE']._serialized_end=628
  _globals['_UPVOTEDCOMMENTSRESPONSE']._serialized_start=630
  _globals['_UPVOTEDCOMMENTSRESPONSE']._serialized_end=691
  _globals['_COMMENTBRANCHREQUEST']._serialized_start=693
  _globals['_COMMENTBRANCHREQUEST']._serialized_end=750
  _globals['_COMMENTBRANCHRESPONSE']._serialized_start=753
  _globals['_COMMENTBRANCHRESPONSE']._serialized_end=915
  _globals['_COMMENTBRANCHRESPONSE_COMMENTTHREAD']._serialized_start=841
  _globals['_COMMENTBRANCHRESPONSE_COMMENTTHREAD']._serialized_end=915
  _globals['_UPDATESREQUEST']._serialized_start=917
  _globals['_UPDATESREQUEST']._serialized_end=971
  _globals['_UPDATESRESPONSE']._serialized_start=974
  _globals['_UPDATESRESPONSE']._serialized_end=1120
  _globals['_UPDATESRESPONSE_COMMENTUPDATE']._serialized_start=1070
  _globals['_UPDATESRESPONSE_COMMENTUPDATE']._serialized_end=1120
  _globals['_REDDITSERVICE']._serialized_start=1123
  _globals['_REDDITSERVICE']._serialized_end=1629
# @@protoc_insertion_point(module_scope)