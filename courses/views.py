from django.shortcuts import render
from django.views.generic import ListView,DetailView,View
from .models import Course




class CourseListView(ListView):
    model = Course
    
    context_object_name="courses"
    

class CourseDetailView(DetailView):
    model = Course
    
    context_object_name="course"


class LessonDetailView(View):
    
    def get(self,request,course_slug,lesson_slug,*args, **kwargs):

        course_qs = Course.objects.filter(slug=course_slug)
        if course_qs.exists():
            course = course_qs.first()


        lesson_qs = course.lessons.filter(slug=lesson_slug)
        if lesson_qs.exists():
            lesson = lesson_qs.first()

        context = {
            'lesson':lesson

        }

        return render(request,"courses/lesson_detail.html",context)




