from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})
	
def index1(request):
    return render(request, 'blog/index1.html', {})