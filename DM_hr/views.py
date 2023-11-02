from django.shortcuts import render,redirect
from Registration_Login.models import EmployeeRegister_Details,LogRegister_Details
from DM_hr.models import candidateDetails

# Create your views here.

def hr_base(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        all_count=candidateDetails.objects.filter(hr_id=emp_dash).count()
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'n_count':n_count,
                    'w_count':w_count,
                    'a_count':a_count,
                    'all_count':all_count
                }
        return render(request,'hr_dashboard.html',content)
    
def hr_profile(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'n_count':n_count,
                    'w_count':w_count,
                    'a_count':a_count
                }
        return render(request,'hr_profile.html',content)
    
def hr_alldata(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash).order_by('-data_added_date')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'data':data,
                    'n_count':n_count,
                    'w_count':w_count,
                    'a_count':a_count
                }
    return render(request,'hr_allData.html',content)

def hr_password(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'n_count':n_count,
                    'w_count':w_count,
                    'a_count':a_count
                }
    return render(request,'hr_password.html',content)

def hr_passwordupdate(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        if request.POST:
           emp_dash.log_username = request.POST['emp_uname']
           emp_dash.log_password = request.POST['emp_password']
           emp_dash.save()  
           success = True
           success_text = 'User name or password change.'
           content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'success':success,
                'success_text':success_text,
                'n_count':n_count,
                'w_count':w_count,
                'a_count':a_count
            }
        else:
            error=True
            error_text = 'Oops! something went wrong.'
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'error':error,
                'error_text':error_text,
                'n_count':n_count,
                'w_count':w_count,
                'a_count':a_count
            }
        return render(request,'hr_password.html',content)
    else:
            return redirect('/')

def hr_newdata(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash,status='new').order_by('-data_added_date')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'data':data,
                    'n_count':n_count,
                    'w_count':w_count,
                    'a_count':a_count
                }
    return render(request,'hr_newData.html',content)

def hr_waitlist(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').order_by('-data_added_date')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'data':data,
                    'n_count':n_count,
                    'w_count':w_count,
                    'a_count':a_count
                }
    return render(request,'hr_waitinglist.html',content)

def hr_wastedata(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash,status='wastedata').order_by('-data_added_date')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'data':data,
                    'n_count':n_count,
                    'w_count':w_count,
                    'a_count':a_count
                }
    return render(request,'hr_wasteData.html',content)

def add_response(request,pk):
    data= candidateDetails.objects.get(id=pk)
    if request.method == 'POST':
        d_response=request.POST['response']
        d_reason=request.POST['response_reason']
        data.reason=d_reason
        data.response=d_response
        data.status='responded'
        data.save()
        success=True
        success_text = 'Response added successfully.'
        if 'emp_id' in request.session:
            if request.session.has_key('emp_id'):
                emp_id = request.session['emp_id']
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash,status='new')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content={
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'data':data,
            'success_text':success_text,
            'success':success,
            'n_count':n_count,
            'w_count':w_count,
            'a_count':a_count
        }
        return render(request,'hr_newData.html',content)
    return redirect('hr_newdata')

def add_response_from_waitinglist(request,pk):
    data= candidateDetails.objects.get(id=pk)
    if request.method == 'POST':
        d_response=request.POST['response']
        d_reason=request.POST['response_reason']
        data.response=d_response
        data.reason=d_reason
        data.status='responded'
        data.save()
        success=True
        success_text = 'Response added successfully.'
        if 'emp_id' in request.session:
            if request.session.has_key('emp_id'):
                emp_id = request.session['emp_id']
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content={
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'data':data,
            'success_text':success_text,
            'success':success,
            'n_count':n_count,
            'w_count':w_count,
            'a_count':a_count
        }
        return render(request,'hr_waitinglist.html',content)
    return redirect('hr_waitlist')

def add_to_waitingList(request,pk):
    data= candidateDetails.objects.get(id=pk)
    if request.method == 'POST':
        d_reason =request.POST['wait_reason']
        data.reason=d_reason
        data.response='In WaitingList'
        data.status='waitlist'
        data.save()
        waitlist_text='Added to waitlist'
        waitlist=True
        if 'emp_id' in request.session:
            if request.session.has_key('emp_id'):
                emp_id = request.session['emp_id']
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash,status='new')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content={
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'data':data,
            'warning_text':waitlist_text,
            'waitlist':waitlist,
            'n_count':n_count,
            'w_count':w_count,
            'a_count':a_count
        }
        return render(request,'hr_newData.html',content)
    return redirect('hr_newdata')


def add_to_wastedata(request,pk):
    data= candidateDetails.objects.get(id=pk)
    if request.method == 'POST':
        d_reason=request.POST['waste_reason']
        data.reason=d_reason
        data.status='wastedata'
        data.response='It is a wastedata'
        data.save()
        waitlist_text='Added to wastedata'
        error=True
        if 'emp_id' in request.session:
            if request.session.has_key('emp_id'):
                emp_id = request.session['emp_id']
        emp_dash = LogRegister_Details.objects.get(id=emp_id,active_status=1)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash,emp_active_status=1)
        data= candidateDetails.objects.filter(hr_id=emp_dash,status='new')
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        content={
            'emp_dash':emp_dash,
            'dash_details':dash_details,
            'data':data,
            'error_text':waitlist_text,
            'error':error,
            'n_count':n_count,
            'w_count':w_count,
            'a_count':a_count
        }
        return render(request,'hr_newData.html',content)
    return redirect('hr_newdata')


def hr_profileupdate(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
        else:
            return redirect('/')
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        n_count=candidateDetails.objects.filter(hr_id=emp_dash,status='new').count()
        w_count=candidateDetails.objects.filter(hr_id=emp_dash,status='waitlist').count()
        a_count=n_count+w_count
        if request.POST:
            emp_obj = EmployeeRegister_Details.objects.get(id=dash_details.id)
            emp_obj.emp_name = request.POST['empname']
            emp_obj.emp_contact_no = request.POST['contactno']
            emp_obj.emp_email = request.POST['empEmail']
            emp_obj.emp_address1 = request.POST['add1']
            emp_obj.emp_address2 = request.POST['add2']
            emp_obj.emp_address3 = request.POST['add3']
            emp_obj.emp_pin = request.POST['pincode']
            emp_obj.emp_location = request.POST['loc']
            emp_obj.emp_district = request.POST['empdist']
            emp_obj.emp_state = request.POST['empState']
            if request.FILES.get('empProfile'):
                emp_obj.emp_profile = request.FILES.get('empProfile')
            else:
                emp_obj.emp_profile =  emp_obj.emp_profile 
            if request.FILES.get('empResume'):
                emp_obj.emp_file = request.FILES.get('empResume')
            else:
                emp_obj.emp_file =  emp_obj.emp_file 
            emp_obj.save()
            success_text = 'Profile Details Updated.'
            success = True
            dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'success_text':success_text,
                'success':success,
                'n_count':n_count,
                'w_count':w_count,
                'a_count':a_count
            }
        else:
            error_text = 'Profile Details Updated.'
            error = True
            content = {
                'emp_dash':emp_dash,
                'dash_details':dash_details,
                'error_text':error_text,
                'error':error,
                'n_count':n_count,
                'w_count':w_count,
                'a_count':a_count
            }
        return render(request,'hr_profile.html',content)
    else:
            return redirect('/')
    
def hr_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')            