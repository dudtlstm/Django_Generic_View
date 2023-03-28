from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
# CBV 사용을 위한 코드
from django.views import generic
from django.urls import reverse_lazy, reverse

# FBV - 전체 게시물 보기
# def mainpage(request):
#    blogs = Blog.objects.all()
#    return render(request, 'main/mainpage.html', {'blogs':blogs})

# CBV - 전체 게시물 보기
class BlogListView(generic.ListView):
    model = Blog
    context_object_name = 'blogs' # 객체를 부르는 이름
    template_name = 'main/mainpage.html'
    # queryset = Blog.objects.all()

# FBV - 상세(detail) 내용 보기
# def detail(request, id):
#    blog = get_object_or_404(Blog, pk = id)
#    return render(request, 'main/detail.html',{'blog':blog})

# CBV - 상세(detail) 내용 보기
class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/detail.html'

# FBV - 새 게시물 생성
# def create(request):
#    new_blog = Blog()
#    new_blog.title = request.POST['title']
#    new_blog.writer = request.POST['writer']
#    new_blog.pub_date = timezone.now()
#    new_blog.body = request.POST['body']
#    new_blog.image = request.FILES.get('image')
#    new_blog.save()
#    return redirect('main:detail', new_blog.id)

# CBV - 새 게시물 생성
class BlogCreateView(generic.CreateView):
    model = Blog
    fields = ['title', 'writer', 'body', 'image']
    template_name = 'main/detail.html'

    def get_success_url(self):
        return reverse('main:detail', kwargs={'pk': self.object.pk})

# new.html 가는 코드(고칠 필요 X)
def new(request):
    return render(request, 'main/new.html')

# 수정 화면으로 가는 코드 구현
def edit(request, pk):
    edit_blog = Blog.objects.get(pk=pk)
    return render(request, 'main/edit.html', {'blog' : edit_blog})

# FBV - update(수정) 기능 구현
# def update(request, pk):
#     update_blog = Blog.objects.get(pk=pk)
#     update_blog.title = request.POST['title']
#     update_blog.writer = request.POST['writer']
#     update_blog.pub_date = timezone.now()
#     update_blog.body = request.POST['body']
#     update_blog.save()
#     return redirect('main:detail', update_blog.pk)

# CBV - update(수정) 기능 구현
class BlogUpdateView(generic.UpdateView):
    model = Blog
    fields = ['title', 'writer', 'body', 'image']
    template_name = 'main/edit.html'

    def get_success_url(self):
        return reverse('main:detail', kwargs={'pk': self.object.pk})
    
# FBV - delete(삭제) 기능 구현
# def delete(request, id):
#     delete_blog = Blog.objects.get(id=id)
#     delete_blog.delete()
#     return redirect('main:mainpage')

# CBV - delete(삭제) 기능 구현
class BlogDeleteView(generic.DeleteView):
    model = Blog
    template_name = 'main/delete.html' # 깔끔하게 진행하기 위해 delete.html 페이지 하나 추가
    success_url = reverse_lazy('main:mainpage')