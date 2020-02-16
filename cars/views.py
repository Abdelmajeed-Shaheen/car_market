from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Car
from .forms import CarForm

def car_home(request):
	return render(request,'index.html')
def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):
	form = CarForm()
	if request.method == "POST":
		form = CarForm(request.POST , request.FILES)
		carmake = form
		if form.is_valid():
			form.save()
			messages.success(request, f"{carmake} is added")
			return redirect("car-list")
		else:
			messages.success(request, f"{carmake} is not added")
	context = {
    	"form":form,
    }
	return render(request, 'create.html', context)



def car_update(request, car_id):
	car = Car.objects.get(id= car_id)
	form = CarForm(instance = car)
	if request.method == "POST":
		form = CarForm(request.POST , request.FILES,instance=car)
		if form.is_valid():
			form.save()
			messages.success(request, 'Car updated')
			return redirect("car-detail",car_id)

	context = {
    	"form":form,
		"car":car
    }
	return render(request, 'update.html', context)


def car_delete(request, car_id):
	Car.objects.get(id=car_id).delete()
	messages.success(request, 'Car deleted')
	return redirect('car-list')
