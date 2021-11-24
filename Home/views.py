from django.http.response import HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks={
    "1st":"""<li>Basic requirements to build web applications</li>
    <li>Web terminology</li>
    <li>Web server</li>
    <li>Website</li>
    <li>Web Page</li>
    <li> Other Web basic terminology</li>
    """ ,
    "10th":"""<li>HTML tags</li>
    <li>HTML heading</li>
    <li>HTML paragraph and blockquotes</li>
    <li>About HTML lists</li>
    <li>HTML line break,blankspaces and formatted text</li>
    """,   
     "15th":"""<li>HTML links</li>
    <li>HTML Tables</li>
    <li>HTML img,video tags</li>
   <li>About HTML input and forms</li>
    <li>HTML buttons</li>
    """,
    "20th":"""
    <li>CSS concepts</li>
    <li>CSS syntax and background</li>
    <li>CSS styling text and others elements</li>
    <li>CSS Page Backgrounds</li>
    <li>CSS adding borders</li>
    <li>CSS adding icons</li>
     """,
     "25th":""" 
     <li>CSS about display vlaues</li>
     <li>CSS with Positioning HTML elements</li>
     <li>CSS content Overflow</li>
     <li>CSS floating HTML elements</li>
     <li>CSS BOx model</li>
     """,
     "30th":""" 
     <li>CSS box-sizing and shadows</li>
     <li>CSS combiners and Pseudo Classes&Elements</li>
     <li>CSS display-flex</li>
     <li>CSS gird properties</li>
     <li>CSS transform and transitions</li>
     <li>CSS Animations</li>
     """
}

def home(request):
    taskNo=tasks.keys()
    return render(request,'home/home.html',{"taskNo":taskNo})


def task_page(request,no):
    try:
        task=tasks[no]
    except:
        return HttpResponseNotFound('<h1><mark>Invalid Day !! </mark></h1>')
    return render(request,'home/task_page.html',{"task":task,"no":no})