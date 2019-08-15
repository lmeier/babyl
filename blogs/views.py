# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
#from blogs.core.forms import SignUpForm
from .models import Blog, Post
from .forms import NewPostForm, NewBabylForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.timezone import activate

def index(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        return render(request, 'index.html')

def home(request):
    if request.user.is_authenticated:
        blogs = request.user.blog_set.all()
        print(blogs)
        context = {
            'blogs': blogs
        }
        return render(request, 'home.html', context=context)
    else:
        return redirect('/')

def new_babyl(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewBabylForm(request.POST)
            if form.is_valid():
                blog = form.save(commit=False)
                blog.owner = request.user
                blog.published_date = timezone.now()
                blog.save()
                slug = blog.slug
                return redirect('view_blog', blog_slug=slug)
                # return redirect('some-view-name', foo='bar')

        else:
            form = NewBabylForm
        #add blog.slug to model in the blog thing below
        # return render(request, '.html', {'form': form})
        return render(request, 'new_babyl.html', {'form': form})

    else:
        return redirect('/login/')

def view_blog(request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = blog.post_set.all()
    context = {
    'blog_name': blog.name,
    'blog_slug': blog.slug,
    'blog_description': blog.description,
    'posts': posts,
    'blog': blog,
        }
    if request.user == blog.owner:
        context['owner'] = True
    else:
        context['owner'] = False
    return render(request, 'view_blog.html', context=context)

def view_post(request, blog_slug, post_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    post = get_object_or_404(Post, blog=blog, slug=post_slug)
    context = {
        'blog': blog,
        'post': post,
        'blog_name': blog.name,
        'title': post.title,
        'body': post.body,
        'created_at': post.created_at,
    }
    return render(request, 'view_post.html', context=context)

@login_required
def settings(request):
    #much to be filled in here
    context ={}
    return render(request, 'settings.html', context=context)

def new_post(request, blog_slug):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                # blog = get_object_or_404(Blog, slug=blog_slug)
                blog = Blog.objects.get(slug=blog_slug)
                # >>> one_entry = Entry.objects.get(pk=1)
                post.blog = blog
                post.created_at = timezone.now()
                post.save()
                slug = post.slug
                return redirect('view_post', blog_slug=blog.slug, post_slug=slug)
                # return redirect('some-view-name', foo='bar')
            
        else:
            form = NewPostForm
        #add blog.slug to model in the blog thing below
        # return render(request, '.html', {'form': form})
        return render(request, 'new-post.html', {'form': form, 'blog_slug': blog_slug})
        # return redirect('view_blog', blog_slug=slug)
        #return render(request, 'new_babyl.html', {'form': form})
    else:
        return redirect('/login/')




#  def new_post(request,):
#     #blog = get_object_or_404(Blog, pk=pk)
#     #user = User.objects.first()  # TODO: get the currently logged in user
#     #TODO implement logic to check if user lines up to blog
#     if request.method == 'POST':
#         form = NewPostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             #post.blog = blog
#             #post.starter = user
#             post.save()
#             xpost = Post.objects.create(
#                 message=form.cleaned_data.get('message'),
#                 post=post,
#                 #created_by=user
#             )
#             return HttpResponse("hey")
#             #return redirect('blog_posts', pk=board.pk)  # TODO: redirect to the created post page
#     else:
#         form = NewPostForm()
#     return HttpResponse("no success")
#     #return render(request, 'new_post.html', {'blog': blog, 'form': form})

####
#everything beloew to be deleted eventually



# def posts_temp(request):
#     posts = Post.objects.all()
#     return render(request, 'posts_temp.html', {'posts': posts})


# def profile(request, username):
#     user = get_object_or_404(User, username=username)
#     return render(request, 'userapp/profile.html', {'profile_user': user})

# def blog_home(request):
#     posts = Post.objects.all()
#     post_titles = list()

#     for post in posts:
#         post_titles.append(post.title)

#     response_html = '<br>'.join(post_titles)

#     return HttpResponse(response_html)

