from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

def home(request):
    blogs= Blog.objects
    blog_list = Blog.objects.all()    #블로그의 모든 글을 대상으로
    paginator= Paginator(blog_list, 2)  #블로그 객체 2개를 한 페이지로 자르기
    page= request.GET.get('page') #request 된 페이지가 뭔지를 알아내고(request페이지를 변수에 담아내고)
    posts= paginator.get_page(page) #request된 페이지를 얻어온 뒤 이후 리턴
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts} )

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html 띄워주는 함수
    return render(request, 'new.html')

def create(request):  #입력받은 내용을 데이터베이스에 넣어주는 함수
    blog =Blog()
    blog.title= request.GET['title']
    blog.body= request.GET['body']
    blog.pub_date= timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))  #이 URL로 이동

def blogpost(request):
    #1. 입력된 내용을 처리하는 기능 -> POST
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    
    #2. 빈 페이지를 띄워주는 기능 -> GET
    else :
        form = BlogPost()
        return render(request, 'new.html', {'form':form})