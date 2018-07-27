from django.shortcuts import render, redirect
from dataStorage.models import EmployeeInfo
from dataStorage.forms import EmployeeInfoForm
#from django.http import HttpResposeRedirect
from django.shortcuts import render_to_response

#from django.core.context_processors import csrf
# Create your views here.

def index(request):

   	context = {}
   	#print ('worked!!')
   	return render(request, "index.html", context)

def list(request):
	context = {}
	#print ('worked!!')
	context['datas'] = EmployeeInfo.objects.all()

	return render(request, "list.html", context)

def add(request):
	context = {}
	#print ('worked!!')
	# email = request.POST['email']
	# if User.objects.filter(username=self.cleaned_data['username']).exists():
	# firstname = request.POST['firstname']
	# lastname = request.POST['lastname']
	# return render(request, "list.html", context)
	if request.method == 'POST':
		form = EmployeeInfoForm(request.POST)
		#print (form)

		#If provided with a valid form
		if form.is_valid():
			form.save(commit=True)

			#The user will be shown the list page
			#return render(request, "list.html", context)
			#return HttpResposeRedirect('/dataStorage/list/')
			return redirect('list')
		else:
			#The supplied form contained error
			#print (form.errors)
			print('Form error')
	else:
		#If the request was not a POST
		form = EmployeeInfoForm()
	#Bad form, or no form supplied
	return render(request, 'add.html', {'form':form}, context)