from django.shortcuts import render
from django.http import HttpResponse

def course(request):
    return HttpResponse('''
                        <h2> This is my course page</h2>
                        <a href='/second_app/feedback'>Feedback</a>
                        <a href='/first_app/contact'>Contact</a>
                        <a href='/first_app/about'>About</a>
                        ''')

def feedback(request):
    return HttpResponse('''
                        <h2> This is my feedback page</h2>
                        <a href='/second_app/course'>Course</a>
                        <a href='/first_app/contact'>Contact</a>
                        <a href='/first_app/about'>About</a>
                        ''')

