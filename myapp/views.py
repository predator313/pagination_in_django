from django.shortcuts import render
# from django.core.paginator import Paginator
from .models import Post
# # Create your views here.
# def post_list(request):
#     all_post=Post.objects.all().order_by('pk')
#     paginator=Paginator(all_post,3)
#     page_number=request.GET.get('page')
#     page_obj=paginator.get_page(page_number)
#     return render(request,'myapp/home.html',{'posts':page_obj})

#now convert above to the class based view 
from django.views.generic import ListView
class PostListView(ListView):
    model=Post
    template_name='myapp/home.html'
    ordering=['id']
    paginate_by=3
