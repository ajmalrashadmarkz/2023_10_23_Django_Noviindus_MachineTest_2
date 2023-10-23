from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import ShortTermCourse
# from django.core.paginator import Paginator, EmptyPage
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

# class MyPaginator(Paginator):
#     def validate_number(self, number):
#         try:
#             return super().validate_number(number)
#         except EmptyPage:
#             if int(number) > 1:
#                 # return the last page
#                 return self.num_pages
#             elif int(number) < 1:
#                 # return the first page
#                 return 1
#             else:
#                 raise

class ShortTermCourseListView(LoginRequiredMixin, ListView):
    model = ShortTermCourse
    template_name = "shorttermcourse_list.html"

    # paginator_class = MyPaginator
    context_object_name = "shorttermcourse_list"    #default is object_list as well as model's_verbose_name_list and/or model's_verbose_name_plural_list, if defined in the model's inner Meta class
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super(ShortTermCourseListView, self).get_context_data(**kwargs) 
        list_courses = ShortTermCourse.objects.all()
        paginator = Paginator(list_courses, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            courses = paginator.page(page)
        except PageNotAnInteger:
            courses = paginator.page(1)
        except EmptyPage:
            courses = paginator.page(paginator.num_pages)
        
        context['list_courses'] = courses
        return context
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     page = self.request.GET.get('page', 1)
    #     users = ShortTermCourse.objects.all()
    #     paginator = self.paginator_class(users, self.paginate_by)
        
    #     users = paginator.page(page)
        
    #     context['users'] = users
    #     return context
    
class ShortTermCourseDetailView(LoginRequiredMixin, DetailView):  # new
    model = ShortTermCourse
    template_name = "shorttermcourse_detail.html"
    
class ShortTermCourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):  # new
    model = ShortTermCourse
    template_name = "shorttermcourse_delete.html"
    success_url = reverse_lazy("shorttermcourse_list")
    
    def test_func(self):  # new
        obj = self.get_object()
        return obj.user == self.request.user
    
class ShortTermCourseCreateView(LoginRequiredMixin, CreateView):  # new
    model = ShortTermCourse
    template_name = "shorttermcourse_new.html"
    fields = (
        "title",
        "subtitle",
        "description",
        "image",
        "status",
        "amount",
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


    

