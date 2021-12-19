from django.db import models

# Create your models here.
class Question(models.Model): # id는 자동으로 매겨지므로 생성 안해도 됨
    subject = models.CharField('제목', max_length=200)
    content = models.TextField('내용')
    create_date = models.DateTimeField('등록날짜')

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # on_delete=models.CASCADE 이 뜻은 이 답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 뜻
    content = models.TextField('내용')
    create_date = models.DateTimeField('등록날짜')