from django.shortcuts import render,redirect
from Registration_Login.models import EmployeeRegister_Details,LogRegister_Details

# Create your views here.

def hr_base(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)

        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                }
        return render(request,'hr_profile.html',content)