from django.shortcuts import render,redirect,get_object_or_404,HttpResponse


# Create your views here.
from django.contrib import messages
from .models import Administration,NewsModel,GalleryModel,EnquiryModel,BlogModel,MassesModel,EventModel,AboutModel
from .forms import Administration_Form,NewsForm,GalleryForm,EnquiryForm,BlogForm,MassForm,EventForm,AboutForm
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# def user_login(request):
#     if request.method == "POST":
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('admin_dashboard')
#         else:
#             messages.error(request, "Invalid username or password. Please try again....")
#             print("Invalid login attempt")  
#             return redirect('user_login')
#     return render(request, 'authenticate/login.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)  # Use the alias here
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid username or password. Please try again....")
            print("Invalid login attempt")  # Debug print
            return redirect('user_login')
    return render(request, 'authenticate/login.html')


@login_required(login_url='user_login')
def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin_pages/admin_dashboard.html')
    else:
        return redirect('user_login')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')



def add_administaration(request):
    if request.method == 'POST':
        form = Administration_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_administration') 
    else:
        form = Administration_Form()
    return render(request, 'admin_pages/add_administaration.html', {'form': form})


def view_administration(request):
    administration = Administration.objects.all().order_by('-id')
    return render(request,'admin_pages/view_administration.html',{'administration':administration})


def update_administration(request, pk):
    administration = get_object_or_404(Administration, pk=pk)

    if request.method == 'POST':
        form = Administration_Form(request.POST, request.FILES, instance=administration)
        if form.is_valid():
            form.save()
            return redirect('view_administration')
    else:
        form = Administration_Form(instance=administration)

    return render(request, 'admin_pages/update_administration.html', {'form': form,'administration':administration})



def delete_administration(request,pk):
    administration = Administration.objects.get(pk=pk)
    administration.delete()
    return redirect('view_administration')



def admin_add_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_gallery_view') 
    else:
        form = GalleryForm()

    return render(request, 'admin_pages/admin_add_gallery.html', {'form': form})


def admin_gallery_view(request):
    gallery = GalleryModel.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_gallery_view.html',{'gallery':gallery})


def admin_update_gallery(request, id):
    gallery = get_object_or_404(GalleryModel, id=id)

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('admin_gallery_view')
    else:
        form = GalleryForm(instance=gallery)

    return render(request, 'admin_pages/admin_update_gallery.html', {'form': form,'gallery':gallery})



def admin_delete_gallery(request,id):
    gallery = GalleryModel.objects.get(id=id)
    gallery.delete()
    return redirect('admin_gallery_view')



def create_masses(request):
    if request.method == 'POST':
        form = MassForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('masses_view') 
    else:
        form = MassForm()

    return render(request, 'admin_pages/create_masses.html', {'form': form})


def masses_view(request):
    Masses = MassesModel.objects.all().order_by('-id')
    return render(request,'admin_pages/masses_view.html',{'Masses':Masses})


def update_masses(request, id):
    Masses = get_object_or_404(MassesModel, id=id)

    if request.method == 'POST':
        form = MassForm(request.POST, request.FILES, instance=Masses)
        if form.is_valid():
            form.save()
            return redirect('masses_view')
    else:
        form = MassForm(instance=Masses)

    return render(request, 'admin_pages/update_masses.html', {'form': form,'Masses':Masses})



def delete_masses(request,id):
    Masses = MassesModel.objects.get(id=id)
    Masses.delete()
    return redirect('masses_view')


def admin_view_comments(request):
    comments = EnquiryModel.objects.all()
    return render(request,'admin_pages/admin_view_comments.html',{'comments':comments})

def admin_delete_comments(request,id):
    comments = EnquiryModel.objects.get(id=id)
    comments.delete()
    return redirect('admin_view_comments')

def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_view') 
    else:
        form = NewsForm()

    return render(request, 'admin_pages/create_news.html', {'form': form})

def news_view(request):
    news = NewsModel.objects.all().order_by('-id')
    return render(request,'admin_pages/news_view.html',{'news':news})

def update_news(request, id):
    news = get_object_or_404(NewsModel, id=id)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_view')
    else:
        form = NewsForm(instance=news)

    return render(request, 'admin_pages/update_news.html', {'form': form,'news':news})

def delete_news(request,id):
    news = NewsModel.objects.get(id=id)
    news.delete()
    return redirect('news_view')


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_event')
        else:
            print(form.errors)  # Print form errors to console
    else:
        form = EventForm()

    return render(request, 'admin_pages/create_event.html', {'form': form})

def view_event(request):
    event = EventModel.objects.all().order_by('-id')
    return render(request,'admin_pages/view_event.html',{'event':event})

def update_event(request, id):
    event = get_object_or_404(EventModel, id=id)

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            return redirect('view_event')
    else:
        form = EventForm(instance=event)

    return render(request, 'admin_pages/update_event.html', {'form': form,'event':event})

def delete_event(request,id):
    event = EventModel.objects.get(id=id)
    event.delete()
    return redirect('view_event')


@login_required(login_url='user_login')
def add_about_video(request):
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_view_video') 
    else:
        form = AboutForm()
    return render(request, 'admin_pages/add_about_video.html', {'form': form})

@login_required(login_url='user_login')
def admin_view_video(request):
    about = AboutModel.objects.all().order_by('-id')
    return render(request,'admin_pages/admin_view_video.html',{'about':about})  


@login_required(login_url='user_login')
def update_video_link(request,id):
    about = get_object_or_404(AboutModel, id=id)
    if request.method == 'POST':
        form = AboutForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('admin_view_video')
    else:
        form = AboutForm(instance=about)
    return render(request, 'admin_pages/update_video_link.html', {'form': form, 'about': about})


@login_required(login_url='user_login')
def delete_video(request,id):
    about = AboutModel.objects.get(id=id)
    about.delete()
    return redirect('admin_view_video')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_view') 
    else:
        form = BlogForm()

    return render(request, 'admin_pages/create_blog.html', {'form': form})

def blog_view(request):
    blog = BlogModel.objects.all().order_by('-id')
    return render(request,'admin_pages/blog_view.html',{'blog':blog})

def update_blog(request, id):
    blog = get_object_or_404(BlogModel, id=id)

    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_view')
    else:
        form = NewsForm(instance=blog)

    return render(request, 'admin_pages/update_blog.html', {'form': form,'blog':blog})

def delete_blog(request,id):
    news = BlogModel.objects.get(id=id)
    news.delete()
    return redirect('blog_view')


def index(request):
    video = AboutModel.objects.all()
    news = NewsModel.objects.all()
    blog = BlogModel.objects.all()
    gallery = GalleryModel.objects.all()
    administration_team = Administration.objects.all()
    masses = MassesModel.objects.all()
    return render(request,'index.html',{'news':news,'video':video,'blog':blog,'gallery':gallery,'administration_team':administration_team,'masses':masses})

def about(request):
    return render(request,'about-us.html')

def gallery(request):
    gallery = GalleryModel.objects.all()
    return render(request,'gallery.html',{'gallery':gallery})

def contact(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Comment Submitted Successfully!!!!!')
    else:
        form = EnquiryForm()
    return render(request,'contact.html',{'form':form})

def administration(request):
    administration_team = Administration.objects.all()
    return render(request,'administration.html',{'administration_team':administration_team})

def blog(request):
    blog = BlogModel.objects.all()
    return render(request,'blog.html',{'blog':blog})

def news_details(request, id):
    news_item = get_object_or_404(NewsModel, id=id)
    return render(request, 'news_details.html', {'news_item': news_item})

def blog_details(request, id):
    blog = get_object_or_404(BlogModel, id=id)
    return render(request, 'blog-details.html', {'blog': blog})


def login(request):
    return render(request,'accounts/login.html')

def mass(request):
    mass = MassesModel.objects.all()
    return render(request,'masses.html',{'mass':mass})

def event(request):
    return render(request,'events.html')

def wish(request):
    return render(request,'wish.html')

