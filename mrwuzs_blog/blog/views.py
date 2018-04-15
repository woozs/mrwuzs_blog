from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType
from django.core.paginator import Paginator
from django.conf import settings
# Create your views here.

def get_blog_list_common_data(requset,blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.EACH_PAGE_BLOGS_NUMBER)
    page_num = requset.GET.get("page", 1)
    page_of_blogs = paginator.get_page(page_num)
    current_page_num = page_of_blogs.number  # 获取当前页码
    # 获取当前页前后2页
    page_range = list(range(max(current_page_num - 2, 1), current_page_num)) + \
                 list(range(current_page_num, min(current_page_num + 2, paginator.num_pages) + 1))
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)
    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['blogs_count'] = Blog.objects.all().count()
    context['blog_types'] = BlogType.objects.all()
    context['page_range'] = page_range
    context['num_pages'] = paginator.num_pages
    context['blog_dates'] = Blog.objects.dates('created_time', 'month', order='DESC')
    return context



def blog_list(requset):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(requset,blogs_all_list)
    return  render_to_response('blog/blog_list.html', context)




def blog_detail(requset,blog_pk):
    blogs_all_list = Blog.objects.all()
    context = get_blog_list_common_data(requset, blogs_all_list)
    blog = get_object_or_404(Blog,pk=blog_pk)
    context['previous_blog'] = Blog.objects.filter(created_time__gt=blog.created_time).last()
    context['next_blog'] = Blog.objects.filter(created_time__lt= blog.created_time).first()
    context['blog'] = blog
    return render_to_response('blog/blog_detail.html', context)



def blogs_with_type(requset,type_pk):
    blog_type = get_object_or_404(BlogType,pk=type_pk)
    blogs_all_list = Blog.objects.filter(blog_type = blog_type)
    context = get_blog_list_common_data(requset, blogs_all_list)
    context['blog_type'] = blog_type
    return render_to_response('blog/blogs_with_type.html', context)


def blogs_with_date(requset,year,month):
    blogs_all_list = Blog.objects.filter(created_time__year=year,created_time__month=month)
    context = get_blog_list_common_data(requset, blogs_all_list)
    context['blogs_with_date'] = ' %s 年 %s 月'%(year,month)
    return render_to_response('blog/blogs_with_date.html', context)



