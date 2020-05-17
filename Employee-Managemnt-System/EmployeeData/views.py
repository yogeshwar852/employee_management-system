from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import EmpData
from .forms import OrderForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class StaffLogin(View):  # login class
    def get(self, request, *args, **kwargs):  # if request is get
        return render(request, "EmployeeData/stafflogin.html")

    def post(self, request, *args, **kwargs):  # if request is post
        uname = request.POST.get('username')
        password = request.POST.get('password')
        # print(uname,password)
        staff = authenticate(request, username=uname, password=password)
        if staff:
            login(request, staff)
            # print(uname,password)
            return redirect(EmpReg)  # redirect page to home page or registration page
        else:
            return render(request, "EmployeeData/StaffLogin.html", {'error': "Wrong username or password"})
            # return same page if invalid credential


@login_required(login_url="StaffLogin")  # decorator foruser is login or not
def EmpReg(request, id=0):
    # Showing registration page
    if request.method == "GET":
        if id == 0:
            form = 'registration.html'
        else:
            all_Emp_data = EmpData.objects.all(pk=id)
            form = 'registration.html'(instance=all_Emp_data)
        return render(request, "EmployeeData/registration.html", {'form': 'registration.html'})

    else:
        form = EmpData(request.POST)
        if form.is_valid():
            form.save()
        return redirect("EmployeeData/EmployeesData.html")
    # return render(request,"EmployeeData/registration.html")


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class DisplayEmpData(LoginRequiredMixin, View):
    # print(user.username)
    login_url = "StaffLogin"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):  # for displaying employee detail from database get request
        # print("HHHHHHHHH")
        all_Emp_data = EmpData.objects.all()
        SerNo = len(all_Emp_data)
        # return all employee data which will be stored till now
        return render(request, "EmployeeData/EmployeesData.html", {'Emp_savedData': all_Emp_data, 'serno': SerNo})


class SaveEmpData(View):  # for saving employee data into database
    # if (request.method=='POST'):
    def post(self, request, *args, **kwargs):  # save data if request is post
        try:
            empName = request.POST.get('emp_name', 'NA')
            emailadd = request.POST.get('email', 'NA')
            phoneNo = request.POST.get('mob_no', '00')
            department = request.POST.get('department', 'NA')
            if (request.POST.get('department', 'NA') == ""):
                department = "NA"
            # print(empName,emailadd,phoneNo,department)
            obj = EmpData(Emp_name=empName, Emp_email=emailadd, Emp_phonNO=phoneNo,
                          Emp_dept=department)  # database object
            obj.save()
            return redirect("empData")

        except:
            return HttpResponse("Try again")

    def get(self, request, *args, **kwargs):  # get request
        return redirect("EmpReg")


def updateOrder(request, pk):
    order = EmpData.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("empData")

    context = {'form': form}
    return render(request, 'EmployeeData/order_form.html', context)

def deleteOrder(request, pk):
	order = EmpData.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect("empData")

	context = {'item':order}
	return render(request, 'EmployeeData/delete.html', context)

@login_required(login_url="StaffLogin")  # decorator
def logout1(request):  # for logout
    logout(request)
    return redirect("StaffLogin")
