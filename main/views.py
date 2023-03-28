from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
# CBV 사용을 위한 코드
from django.views import generic

# FBV - 전체 게시물 보기
# def mainpage(request):
#    blogs = Blog.objects.all()
#    return render(request, 'main/mainpage.html', {'blogs':blogs})

# CBV - 전체 게시물 보기
class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blogs' # 객체를 부르는 이름
    template_name = 'main/mainpage.html'
    queryset = Blog.objects.all()

# FBV - 상세(detail) 내용 보기
# def detail(request, id):
#    blog = get_object_or_404(Blog, pk = id)
#    return render(request, 'main/detail.html',{'blog':blog})

# CBV - 상세(detail) 내용 보기
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/detail.html'

# 새 게시물 생성
def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.writer = request.POST['writer']
    new_blog.pub_date = timezone.now()
    new_blog.body = request.POST['body']
    new_blog.image = request.FILES.get('image')

    new_blog.save()
    
    return redirect('main:detail', new_blog.id)

def new(request):
    return render(request, 'main/new.html')

# 수정 화면으로 가는 코드 구현
def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'main/edit.html', {'blog' : edit_blog})

# update(수정) 기능 구현
def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.pub_date = timezone.now()
    update_blog.body = request.POST['body']
    update_blog.save()
    return redirect('main:detail', update_blog.id)

# delete(삭제) 기능 구현
def delete(request, id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('main:mainpage')