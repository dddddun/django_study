from django.db import models


# Question 모델의 속성 = 제목(subject), 내용(content), 작성일시(create_date)
class Question(models.Model):
    # 글자수의 길이가 제한된 텍스트 = CharField 메서드 사용
    subject = models.CharField(max_length=200)
    # 글자수의 길이가 제한되지 않은 텍스트 = TextField 메서드 사용
    content = models.TextField()
    # 날짜와 시간에 관계된 속성은 DateTimeField 메서드 사용
    create_date = models.DateTimeField()

    # 아이디값 대신 제목을 표시하기
    def __str__(self):
        return self.subject


class Answer(models.Model):
    # 질문에 대한 답변에 관한 모델이므로 Question 모델을 속성으로 가져가야 한다.
    # 기존 모델을 속성으로 연결하려면 ForeignKey를 사용해야 한다.
    # ForeignKey는 다른 모델과 연결하기 위해 사용
    # on_delete=models.CASCADE :  이 답변과 연결된 질문이 삭제될 경우 답변도 함께 삭제된다는 의미
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
