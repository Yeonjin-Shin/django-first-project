from django.db import models
from user.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # user_id ()
    title = models.CharField(max_length=100)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)
    img_url = models.URLField(null=True)

    class Meta:
        # 만약 테이블 이름을 지정하지 않으면 app_model (ex: board_post)
        db_table="post"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # post_id(1)
    content = models.TextField()
    reg_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="comment"