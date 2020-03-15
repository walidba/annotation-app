from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import AnnotationForm
from .models import Comment,Annotation



@login_required
def home(request):
    # context = {
    #     'posts': Post.objects.all()
    # }
    return render(request, 'blog/home.html')

@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

@login_required
def annotate(request):
    comment_to_annotate = getNext(request.user)
    if request.method =='POST':
        aform = AnnotationForm(request.POST)
        an = aform.save(commit=False)
        an.annotator=request.user
        an.comment = comment_to_annotate
        an.save()

        return redirect('annotate')
    else:
        aform = AnnotationForm()
        if comment_to_annotate.__class__.__name__=='Comment':
            return render(request, 'blog/annotate.html',context={'aform':aform,'comm':comment_to_annotate})
        # else:
        #     return render(request, 'blog/annotate.html',context={'comm':'Vous avez annoté 5000 commentaires. Merci pour votre collaboration!'})


def getNext(u):
    # comments = [ c for c in Comment.objects.all()]
    # ann= [ c.comment_id for c in Annotation.objects.filter(annotator_id=u.id)]
    # i=0
    # if ann:
    #     if len(ann)>1:
    #         return 'a'
    #     while comments[i].comment_id in ann:
    #         i+=1
    #     return comments[i]
    # else: return comments[0]
    comments = [ c for c in Comment.objects.all()]
    an= [a.comment_id for a in Annotation.objects.filter(annotator_id=u.id)]
    ann= Annotation.objects.all()
        
    for c in comments:
        if c.comment_id in an:
            continue
        elif ann.filter(comment_id=c.comment_id).count() <3:
            return c
    


