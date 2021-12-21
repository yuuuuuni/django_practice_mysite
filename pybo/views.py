from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


def index(request): # 자바에서 rq와 같은 것
    """
    pybo 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list} # {'값':키} # question_list 변수에 question_list의 값을 넣겠다.
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
     pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


def answer_create(request, question_id):
    """
    pybo 답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid(): # 폼이 유효하면
            # 폼을 먼저 임시저장해서 answer에 넣자 => 임시저장 안하고 그냥 저장해버리면 create_date에 값이 없다는 오류 생김(현재QuestionForm에는 답변등록날짜 속성이 없기 때문에! 그래서 먼저 임시저장 후 answer객체를 리턴받아 create_date에 값을 설정 후 save()로 실제 저장해줌)
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question.id)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)

# redirect(URL로 이동할 경로, 넘겨줄 거 있으면 넘겨줄거 쓰기)
# redirect는 URL로 이동
# URL 로 이동한다는 건 그 URL과 연결된 views 가 다시 실행될테고
# views와 연결된 함수의 return값을 보고 render를 할지 다시 redirect 할지 결정할 것



def question_create(request):
    """
    pybo 질문등록
    """
   # form = QuestionForm()
   # return render(request, 'pybo/question_form.html', {'form':form})
# render는 템플릿을 불러옴
# render(request, 불러오고 싶은 template_name, context는 템플릿인 pybo/question_form.html에 전달할 데이터를 Dictionary로 전달)
# 이때, Dictionary의 key는 pybo/question_form.html에서 사용할 템플릿변수명이 되고,
# value는 전달하는 내용을 넣어주면 됨

# render함수 vs redirect 함수
# 이 두 함수의 차이점은 render의 경우 내가 가진 templates에 data를 넣어 보내고 싶을 때 이용하고,
# redirect는 내가 가진 templates뿐만 아니라 절대 url로 이동하고 싶을 때에도 이용 가능

# question_create 함수를 아래와 같이 수정함
    if request.method == 'POST':
        form = QuestionForm(request.POST)  # request.POST를 인수로 받을 경우에는 request.POST에 담긴 subject와 content의 값이 QuestionForm의 그 둘 속성에 자동으로 저장돼서 객체 생김
        if form.is_valid(): # form이 유효한지를 검사 * valid 뜻 : 유효하다면
            question = form.save(commit=False) # form으로 Question 데이터를 저장하기 위한 코드 * commit=False는 임시저장을 의미
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index') # redirect이므로 별칭 index로 이동하겠다.
    else: # 그게 아니면(즉, request.method가 POST가 아니면 )
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', context) # 질문등록화면을 보여줘라

# GET 방식에서는 form = QuestionForm() 처럼 QuestionForm을 인수 없이 생성함.
# 하지만 POST 방식에서는 form = QuestionForm(request.POST) 처럼 request.POST를
# 인수로 생성함. request.POST를 인수로 QuestionForm을 생성할 경우에는
# request.POST에 담긴 subject, content 값이 QuestionForm의 subject, content 속성에
# 자동으로 저장되어 객체가 생성된다.
# request.POST에는 화면에서 사용자가 입력한 내용들이 담겨있음



