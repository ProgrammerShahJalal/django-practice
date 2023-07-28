from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse('''
                        <h2> This is my contact page</h2>
                        <a href='/first_app/about/'>About</a>
                        <a href='/second_app/feedback'>Feedback</a>
                        <a href='/second_app/course'>Course</a>
                        ''')

def about(request):
    return HttpResponse('''
                        <h2> This is my about page</h2>
                        <a href='/first_app/contact/'>Contact</a>
                           <a href='/second_app/feedback'>Feedback</a>
                        <a href='/second_app/course'>Course</a>
                        ''')


