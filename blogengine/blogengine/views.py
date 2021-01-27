from django.shortcuts import redirect, render


def redirect_blog(request):
	return redirect('posts_list_url', permanent=True)

def page_404_not_found(request, exception):
	return render(request, '404_not_found.html')

def page_403_forbidden(request, exception):
	return render(request, '403_forbidden.html')