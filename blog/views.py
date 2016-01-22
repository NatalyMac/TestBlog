# -*- coding: utf-8 -*-

from django.views.generic import ListView, DetailView, CreateView, FormView
from django import forms
from .models import Post
from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from forms import PostForm
from django.utils import timezone
#from django.contrib.auth.models import User

    
class PostListView(ListView):
    model = Post
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post



class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    





