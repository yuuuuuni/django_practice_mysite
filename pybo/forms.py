from django import forms
from pybo.models import Question


class QuestionForm(forms.ModelForm): # QuestionForm은 모델 폼을 상속함
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject', 'content'] # QuestionForm에서 사용할 Question 모델의 속성
# QuestionForm은 Question 모델과 연결된 폼이며, 속성으로 subject와 content를 사용한다고 정의