# -*- coding: utf-8 -*-
from tornado.web import url

from apps.community.handler import *

urlpatterns = (
    url("/groups/", CommunityGroupHandler),
    url("/groups/([0-9]+)/", GroupDetailHandler),
    url("/groups/([0-9]+)/members/", GroupMemberHandler),
    url("/groups/([0-9]+)/posts/", PostHandler),

    # 申请信息获取
    url("/replys", ReplyHandler),
    # 申请消息处理
    url("/members/([0-9]+)/", HandleReplyHandler),

    # 帖子详细
    url("/posts/([0-9]+)/", PostDetailHandler),

    # 评论
    url("/posts/([0-9]+)/comments/", PostCommentHandler),
    # 评论回复
    url("/comments/([0-9]+)/replys/", CommentReplyHandler),
    url("/comments/([0-9]+)/likes/", CommentLikeHandler),
)
