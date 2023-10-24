from django.shortcuts import render


def startup(request):
 return render(request,'home.html')
def about(request):
 return render(request,'about.html')
def contact(request):
  return render(request,'contact.html')
def work(request):
 return render(request,'work.html')