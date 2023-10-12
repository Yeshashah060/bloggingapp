from django.shortcuts import render , redirect
from django.http import HttpResponse , HttpRequest 
from.models import yesha


# home page function
def home(request):
	return render(request, 'home.html')

def addb(request):
	return render(request, 'add.html')

def save(request):
	writer = request.GET.get("writer")
	blog = request.GET.get("blog")
	price = request.GET.get("price")
	noblog = request.GET.get("noblog")
	b = yesha(writer=writer,blog=blog,price=price,noblog=noblog)
	b.save()

	data = yesha.objects.all()
	return render(request, 'display.html',{'data':data})


def displayy(request):
		data = yesha.objects.all()
		return render(request,'display.html',{'data':data})


def edit(request):
	id=request.GET["id"]
	data = yesha.objects.get(id=id)
	return render(request,'add.html',{'data':data})

def update(request):
	
	id=request.GET["id"]
	data = yesha.objects.get(id=id)
	data.writer = request.GET['writer']
	data.blog = request.GET['blog']
	data.price = request.GET['price']
	data.noblog = request.GET['noblog']
	data.save()

	#data = yesha.objects.all()
	return redirect(displayy)

def delete(request):
	id=request.GET['id']
	data = yesha.objects.get(id=id)
	data.delete()
	data = yesha.objects.all()
	return render(request, 'display.html',{'data':data})

def buy(request):
	id=request.GET['id']
	data = yesha.objects.get(id=id)
	data.noblog = noblog-1
	data.save()
	data = yesha.objects.all()
	return redirect(displayy)


def search(request):
