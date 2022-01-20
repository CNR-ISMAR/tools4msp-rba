from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import ObjectDoesNotExist
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .models import CS, DocPage


class CsList(ListView):
    
    model = CS
    template_name = 'rba/cs_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cs'] =  [(s.title ) for s in CS.objects.all()]
        return context


class CSDetailView(DetailView):
    model = CS
    template_name = 'rba/cs_detail.html'
    slug_field = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context
    
    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return redirect("/login.html")
        return super(CSDetailView, self).get(request, *args, **kwargs)


class baseDetailView(DetailView):

    model = CS
    template_name = 'base.html'
    slug_field = 'id'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cs'] =  [(s.title ) for s in CS.objects.all()]
        return context


def index(request):
    if request.user.is_anonymous:
        return redirect("/login.html")
    return redirect( "/rba/list")



def html(request, filename):
    context = {"filename": filename,
               "collapse": ""}
    if request.user.is_anonymous and filename != "login":
        return redirect("/login.html")
    if filename == "logout":
        logout(request)
        return redirect("/")
    if filename == "login" and request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            if "@" in username:
                user = User.objects.get(email=username)
            else:
                user = User.objects.get(username=username)
            user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                context["error"] = "Wrong password"
        except ObjectDoesNotExist:
            context["error"] = "User not found"

        print("login")
        print(username, password)
    print(filename, request.method)
    if filename in ["buttons", "cards"]:
        context["collapse"] = "components"
    if filename in ["utilities-color", "utilities-border", "utilities-animation", "utilities-other"]:
        context["collapse"] = "utilities"
    if filename in ["404", "blank"]:
        context["collapse"] = "pages"

    return render(request, f"{filename}.html", context=context)


class DocListView(ListView):
    model = DocPage
    template_name = 'rba/doc.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context