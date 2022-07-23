from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from requests import request
from accounts.models import Movies
from .forms import MovieForm, RegistrationForm
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


@login_required()
def dashboard(request):
    context = {}
    if request.method == 'GET' and request.GET.get('search'):
        query=request.GET.get('search')
        context['movies'] = Movies.objects.filter(Q(title__contains=query) | Q(description__contains=query) )
        context['query'] = query
    else:
        context['movies'] = Movies.objects.all().order_by('-created_at')
    return render(request,'dashboard.html',context)


class FavMovies(LoginRequiredMixin,ListView):
    model = Movies
    template_name = 'fav-movies.html'

    def get_queryset(self):
        return Movies.objects.filter(user=self.request.user)




class AddMovie(LoginRequiredMixin,CreateView):
    model = Movies
    form_class = MovieForm
    template_name = 'add_movie.html'
    success_url = reverse_lazy('list_movies')

    def form_valid(self, form):
        movie = form.save(commit=False)
        movie.user = self.request.user
        return super(AddMovie, self).form_valid(form)



# @login_required()
# def add_movie(request):
#     return render(request,'add_movie.html')

# @login_required()
# def movies(request):
#     return render(request,'movies.html')



def registration(request):
    context = {}
    context['form'] = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')
        else:
            context['form'] = form
    return render(request,'registration/signup.html',context)
