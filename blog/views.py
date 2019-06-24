
from django.shortcuts import render

# Create your views here.
"""definieren wir eine Funktion ( def ) mit dem Namen post_list ,
die den Parameter request entgegen nimmt und die mit return
den Rückgabewert einer anderen Funktion namens render zurück gibt.
Letztere wird unser Template blog/post_list.html "rendern"
(zu einer fertigen HTML-Seite zusammensetzen) """
def post_list(request):
    return render(request, 'blog/post_list.html', {})

from django.shortcuts import render
from .models import Post



from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
