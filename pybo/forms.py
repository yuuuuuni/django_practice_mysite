from django import forms
from pybo.models import Question, Answer


class QuestionForm(forms.ModelForm):  # QuestionForm은 모델 폼을 상속함 # 외워야함
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']
        labels = {  # 질문등록화면에 표시되는 subject, content를 영문이 아닌 한글로 표시하고 싶은 경우 아래처럼 labels 속성 지정해주기
            'subject': '제목',
            'content': '내용',
        }


# Question의 속성 id, subject, content, create_date중 질문등록글을 작성할 때 빈칸
# 이어서는 안될 속성인, subject와 content를 fields에 포함시켜주면
# 서버 접속 창에서 둘 중에 하나라도 안적었을 시 "이 입력란을 적어주세요"라며 안내창이 뜸
# 즉, form은 우리가 저런 것들을 스스로 구현하지 않아도 fields에 해당 속성을 넣어주기만
# 하면 둘 중에 하나라도 빈칸으로 저장할 수 없도록 하는 기능을 제공함
# (둘 다 무조건 입력하도록 필수 기재사항을 만들어놓는 기능 제공)

class AnswerForm(forms.ModelForm):  # QuestionForm은 모델 폼을 상속함 # 외워야함
    class Meta:
        model = Answer  # 사용할 모델
        fields = ['content']
        labels = {  # 답변등록화면에 표시되는 content를 영문이 아닌 한글로 표시하고 싶은 경우 아래처럼 labels 속성 지정해주기
            'content': '답변내용',
        }
