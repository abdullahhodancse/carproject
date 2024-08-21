from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .forms import CarForm,CommentForm
from .models import Car,Comment
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class AddPostCar(CreateView):
    form_class = forms.CarForm  
    model =models. Car  
    success_url = reverse_lazy('addcars')  
    template_name = 'add_car.html'  

    def form_valid(self, form):
        return super().form_valid(form)
    
    
    

class DetailsCarView(DetailView):
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        comment_form = CommentForm(data=request.POST)
        
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
            return redirect('details_car', id=car.id)  # Redirect after POST to avoid form resubmission
        
        context = self.get_context_data()
        context['comment_form'] = comment_form  # Include the form with validation errors
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        
        return context
    

# def buy_car(request, id):
#         car = get_object_or_404(Car, id=id)
#         if car.quantity > 0:
#             car.quantity -= 1
#             car.save()
#         return redirect('details_car', id=car.id)    
        
    
    
# class DetailsCarView(DetailView):
#     model = Car
#     pk_url_kwarg = 'id'
#     template_name = 'car_details.html'

#     def handle_comment_submission(self, request, *args, **kwargs):
#         if request.method == "POST":
#             comment_form = forms.CommentForm(data=request.POST)
#             if comment_form.is_valid():
#                 new_comment = comment_form.save(commit=False)
#                 new_comment.car = self.get_object()
#                 new_comment.save()

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         car = self.object  # Car model object is stored here
#         comments = car.comments.all()  # Fetch related comments
#         comment_form = forms.CommentForm()

#         context['comments'] = comments
#         context['comment_form'] = comment_form
#         return context

#     def get(self, request, *args, **kwargs):
#         self.handle_comment_submission(request, *args, **kwargs)
#         return super().get(request, *args, **kwargs)