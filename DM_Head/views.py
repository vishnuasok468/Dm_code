from django.shortcuts import render,redirect
from Registration_Login.models import *
from .models import *
from django.core import serializers
from django.db.models import Q
from django.utils import timezone
from datetime import date, datetime,timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.models import Count


def head_dashboard(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

           # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employee_count = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id).count()
        work_count = WorkRegister.objects.filter(wcompId=dash_details.emp_comp_id).count()
        client_count = ClientRegister.objects.filter(compId=dash_details.emp_comp_id).count()
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employee_count':employee_count,
                    'work_count':work_count,
                    'client_count':client_count}

        return render(request,'HD_dashboard.html',content)

    else:
            return redirect('/')



# Profile Page -------------------------
def head_profile(request):  
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_profile.html',content)

    else:
            return redirect('/')
    

    
def profile_detailsUpdate(request):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        # Details Save -----------------

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
        
        
             content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'success_text':success_text,
                    'success':success}

        else:
            error_text = 'Profile Details Updated.'
            error = True
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error_text':error_text,
                    'error':error}

        return render(request,'HD_profile.html',content)

    else:
            return redirect('/')
    

# Remove Profile Image ---------------

def profileImage_remove(request):
    emp_id = request.POST.get('emp_id')
    dash_details = EmployeeRegister_Details.objects.get(id=emp_id)
    dash_details.emp_profile = ''
    dash_details.save()
    return JsonResponse({'message': 'Received emp_id: ' + emp_id})
     
# End ------------------------------------------------


# Password Section -----------------------------------

def head_password(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_password.html',content)

    else:
            return redirect('/')


def user_passwordUpdate(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        if request.POST:
           
           emp_dash.log_username = request.POST['emp_uname']
           emp_dash.log_password = request.POST['emp_password']

           emp_dash.save()  
           success = True
           success_text = 'User name or password change.'
        
           content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success':success,
                   'success_text':success_text}
        else:

            error=True
            error_text = 'Oops! something went wrong.'
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'error':error,
                    'error_text':error_text}

        return render(request,'HD_password.html',content)

    else:
            return redirect('/')


# Work section  ----------------------------------

def Head_work_section(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_workSection.html',content)

    else:
            return redirect('/')


def head_createClient(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        

        data_box ={} 
        
        if request.POST:
             
            client_obj = ClientRegister()

            client_obj.compId = dash_details.emp_comp_id
            client_obj.client_name = request.POST['cName']
            client_obj.client_email_primary = request.POST['cEmail_1']
            client_obj.client_email_alter = request.POST['cEmail_2']
            client_obj.client_phone = request.POST['cPhno_1']
            client_obj.client_phone_alter = request.POST['cPhno_2']
            client_obj.client_address1 = request.POST['cAddress1']
            client_obj.client_address2 = request.POST['cAddress2']
            client_obj.client_address3 = request.POST['cAddress3']
            client_obj.client_place = request.POST['cPlace']
            client_obj.client_district = request.POST['cDistrict']
            client_obj.client_state = request.POST['cState']
            client_obj.client_profile = request.FILES.get('cProfile')

            # Bussiness Details ----------------------

            client_obj.client_bussiness_name = request.POST['cBussinessName']
            client_obj.client_bussiness_email_primary = request.POST['cBussinessEmail_1']
            client_obj.client_bussiness_email_alter = request.POST['cBussinessEmail_2']
            client_obj.client_bussiness_phone = request.POST['cBussinessPhno_1']
            client_obj.client_bussiness_phone_alter = request.POST['cBussinessPhno_2']
            client_obj.client_bussiness_website = request.POST['cBussinessUrl']
            client_obj.client_bussiness_address1 = request.POST['cBussinessAddress_1']
            client_obj.client_bussiness_address2 = request.POST['cBussinessAddress_2']
            client_obj.client_bussiness_address3 = request.POST['cBussinessAddress_3']
            client_obj.client_bussiness_place = request.POST['cBussinessLoc']
            client_obj.client_bussiness_district = request.POST['cBussinessDistrict']
            client_obj.client_bussiness_state = request.POST['cBussinessState']
            client_obj.bussiness_logo = request.FILES.get('cBussinessLogo')
            client_obj.client_bussiness_file = request.FILES.get('cBussinessFile')
            client_obj.more_discription = request.POST['moreAbout']
            client_obj.client_status = 1
        
            client_obj.save()

            success = True
            success_text= 'Client creation successful.' 

            clients = ClientRegister.objects.filter(compId=dash_details.emp_comp_id)
            Tasks = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id.id)
                
            data_box = {'success':success,
                        'success_text':success_text,
                        'clients':clients,
                        'client_obj':client_obj,
                        'Tasks':Tasks}

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
            content = {**data_box, **content}

            return render(request,'HD_workCreate.html',content)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}
        
       

        return render(request,'HD_createClient.html',content)

    else:
            return redirect('/')



def head_createWork(request): 

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        clients = ClientRegister.objects.filter(compId=dash_details.emp_comp_id)
        Tasks = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id.id)
        

        if request.POST:
             
            work_obj = WorkRegister()
            work_obj.clientId = ClientRegister.objects.get(id=int(request.POST['client_data']))
            work_obj.work_create_date = request.POST['start_date']
            work_obj.work_end_date = request.POST['end_date']
            work_obj.work_discription = request.POST['work_discription']
            work_obj.work_file = request.FILES.get('work_file')
            work_obj.wcompId = dash_details.emp_comp_id
            work_obj.save()

            tasks_list = request.POST.getlist('task_name')

            print(tasks_list)

            for task in tasks_list:
                task_obj = ClientTask_Register()
                task_obj.cTcompId = dash_details.emp_comp_id
                task_obj.work_Id = work_obj
                task_obj.client_Id = ClientRegister.objects.get(id=int(request.POST['client_data']))
                task_obj.task_name = task
                task_obj.task_create_date = date.today()
                task_obj.save()

            success = True
            success_text= 'Work and Tasks creation successful.' 

            works = WorkRegister.objects.filter(wcompId=dash_details.emp_comp_id)
                
        
            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success':success,
                    'success_text':success_text,
                    'works':works}
        

            return render(request,'HD_Viem_Edit.html',content)
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'clients':clients,
                   'Tasks':Tasks}

        return render(request,'HD_workCreate.html',content)

    else:
            return redirect('/')


def head_getClient_data(request):
    client_id = request.GET.get('client_id')

    client = ClientRegister.objects.get(id=client_id)

    response_data = {
        'client_email': client.client_email_primary,
        'client_phone': client.client_phone,
        'client_bussinessName': client.client_bussiness_name,
        'client_bussinessEmail': client.client_bussiness_email_primary,
        'client_website': client.client_bussiness_website,
        
    }

    return JsonResponse(response_data)


def head_WorkviewEdit(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        works = WorkRegister.objects.filter(wcompId=dash_details.emp_comp_id)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'works':works}

        return render(request,'HD_Viem_Edit.html',content)

    else:
            return redirect('/')
    

def head_workEdit(request,pk):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        works = WorkRegister.objects.get(id=pk)
        Company_taskList = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id)
        ClientTask_list = ClientTask_Register.objects.filter(work_Id=works)


        data_box ={} 
        
        if request.POST:
             
            client_obj = ClientRegister.objects.get(id=int(request.POST['client_ID']))

            workID = int( request.POST['work_ID'])

            client_obj.compId = dash_details.emp_comp_id
            client_obj.client_name = request.POST['cName']
            client_obj.client_email_primary = request.POST['cEmail_1']
            client_obj.client_email_alter = request.POST['cEmail_2']
            client_obj.client_phone = request.POST['cPhno_1']
            client_obj.client_phone_alter = request.POST['cPhno_2']
            client_obj.client_address1 = request.POST['cAddress1']
            client_obj.client_address2 = request.POST['cAddress2']
            client_obj.client_address3 = request.POST['cAddress3']
            client_obj.client_place = request.POST['cPlace']
            client_obj.client_district = request.POST['cDistrict']
            client_obj.client_state = request.POST['cState']

            if request.FILES.get('cProfile'):

                client_obj.client_profile = request.FILES.get('cProfile')
            else:
                client_obj.client_profile = client_obj.client_profile

            # Bussiness Details ----------------------

            client_obj.client_bussiness_name = request.POST['cBussinessName']
            client_obj.client_bussiness_email_primary = request.POST['cBussinessEmail_1']
            client_obj.client_bussiness_email_alter = request.POST['cBussinessEmail_2']
            client_obj.client_bussiness_phone = request.POST['cBussinessPhno_1']
            client_obj.client_bussiness_phone_alter = request.POST['cBussinessPhno_2']
            client_obj.client_bussiness_website = request.POST['cBussinessUrl']
            client_obj.client_bussiness_address1 = request.POST['cBussinessAddress_1']
            client_obj.client_bussiness_address2 = request.POST['cBussinessAddress_2']
            client_obj.client_bussiness_address3 = request.POST['cBussinessAddress_3']
            client_obj.client_bussiness_place = request.POST['cBussinessLoc']
            client_obj.client_bussiness_district = request.POST['cBussinessDistrict']
            client_obj.client_bussiness_state = request.POST['cBussinessState']

            if request.FILES.get('cBussinessLogo'):

                client_obj.bussiness_logo = request.FILES.get('cBussinessLogo')

            else:
                client_obj.bussiness_logo =  client_obj.bussiness_logo

            if request.FILES.get('cBussinessFile'):
                
                client_obj.client_bussiness_file = request.FILES.get('cBussinessFile')
            else:
                client_obj.client_bussiness_file = client_obj.client_bussiness_file 

            client_obj.more_discription = request.POST['moreAbout']
            client_obj.client_status = 1
        
            client_obj.save()

            works = WorkRegister.objects.get(id=workID)

            success = True
            success_text= 'Client details edit successful.' 

            data_box = {'success':success,
                        'success_text':success_text}
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'works':works,'Task_list':ClientTask_list,
                   'Company_taskList':Company_taskList}
        
        content = {**data_box, **content}

        return render(request,'HD_workEdit.html',content)

    else:
            return redirect('/')


def head_workTaskEdit(request,pk):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        task_edit_obj = ClientTask_Register.objects.get(id=pk)
        works = WorkRegister.objects.get(id=task_edit_obj.work_Id.id)

        Company_taskList = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id)
        ClientTask_list = ClientTask_Register.objects.filter(work_Id=works)
        

           
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'works':works,'Task_list':ClientTask_list,
                    'task_edit_obj':task_edit_obj,
                    'Company_taskList':Company_taskList}
            
           

        return render(request,'HD_workEdit.html',content)

    else:
            return redirect('/')


def head_work_taskadd(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

       
        data_box ={} 
        
        if request.POST:
             
            if request.POST['task_ID']:
           
                clientTask_obj = ClientTask_Register.objects.get(id=int(request.POST['task_ID']))
                clientTask_obj.task_name = request.POST['task_name']
                clientTask_obj.task_discription = request.POST['task_discription']

                if request.FILES.get('task_file'):

                    clientTask_obj.task_file = request.FILES.get('task_file')

                else:
                    clientTask_obj.task_file = clientTask_obj.task_file 
                
                clientTask_obj.save()

                success = True
                success_text= 'Task edit successful.' 
            
            else:

                works_obj = WorkRegister.objects.get(id=int(request.POST['Worktask_ID']))
                
                clientTask_obj = ClientTask_Register()
                 
                clientTask_obj.task_name = request.POST['task_name']
                clientTask_obj.task_discription = request.POST['task_discription']
                clientTask_obj.task_file = request.FILES.get('task_file') 
                clientTask_obj.task_status = 1
                clientTask_obj.cTcompId = dash_details.emp_comp_id
                clientTask_obj.client_Id = works_obj.clientId
                clientTask_obj.work_Id = works_obj
                clientTask_obj.task_create_date = date.today()
                clientTask_obj.save()

                success = True
                success_text= 'Task add successful.' 

            works = WorkRegister.objects.get(id=int(request.POST['Worktask_ID']))
            Company_taskList = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id)
            ClientTask_list = ClientTask_Register.objects.filter(work_Id=works)

            data_box = {'success':success,
                        'success_text':success_text}
        
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'works':works,'Task_list':ClientTask_list,
                    'Company_taskList':Company_taskList}
            
            content = {**data_box, **content}

            return render(request,'HD_workEdit.html',content)

        else:
            return redirect('head_WorkviewEdit')

    else:
            return redirect('/')


def head_workTaskDelete(request,pk):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        task_obj = ClientTask_Register.objects.get(id=pk)

        task_delete_obj = ClientTask_Register.objects.get(id=pk)
        task_delete_obj.delete()

        error = True
        error_text= 'Task delete successful.' 

        works = WorkRegister.objects.get(id=task_obj.work_Id.id)

        Company_taskList = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id)
        ClientTask_list = ClientTask_Register.objects.filter(work_Id=works)
        
        content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'works':works,'Task_list':ClientTask_list,
                    'Company_taskList':Company_taskList,
                    'error':error,'error_text':error_text}
            
           

        return render(request,'HD_workEdit.html',content)

    else:
            return redirect('/')


def head_workDetailsEdit(request,pk):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        if request.POST:
            
            works = WorkRegister.objects.get(id=pk)
            works.work_discription =  request.POST['wDiscription']
            works.work_create_date = request.POST['wSdate']
            works.work_end_date = request.POST['wEdate']
            works.work_progress = request.POST['wProgress']
            works.save()  

            
            success = True
            success_text= 'Work details edit successful.' 

            works = WorkRegister.objects.get(id=pk)
            Company_taskList = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id)
            ClientTask_list = ClientTask_Register.objects.filter(work_Id=works)
            
            content = {'emp_dash':emp_dash,
                        'dash_details':dash_details,
                        'notifications':notifications,
                        'works':works,'Task_list':ClientTask_list,
                        'Company_taskList':Company_taskList,
                        'success':success,'success_text':success_text}   

            return render(request,'HD_workEdit.html',content)
        
        else:
             
            return redirect('head_WorkviewEdit')
        
    else:
        return redirect('/')
    
  
# Work Allocate section----------------
def head_allocateWorkView(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        works = WorkRegister.objects.filter(wcompId=dash_details.emp_comp_id).order_by('-id')
        tl_list = EmployeeRegister_Details.objects.filter(emp_department_id=dash_details.emp_department_id,
                                                          emp_designation_id__dashboard_id=2)
        
        client_task = ClientTask_Register.objects.all()
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'works':works,'tl_list':tl_list,
                   'client_task':client_task}

        return render(request,'HD_workAllocate.html',content)

    else:
            return redirect('/')
    

def head_workAllocate(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')


        if request.POST:
             
            workId = WorkRegister.objects.get(id=int(request.POST['Work_id']))
            seletedTl = EmployeeRegister_Details.objects.get(id=int(request.POST['selected_tl']))
            selected_list = request.POST.getlist('clientTask')

            client_task = ClientTask_Register.objects.filter(id__in=selected_list)

            sdate = request.POST['fDate']
            duedate = request.POST['dueDate']
            discription = request.POST['discription_data']
            any_file = request.FILES.get('wFile')

            workId.allocated_emp.add(seletedTl)
            workId.work_allocate_status = 1
            workId.save()

            work_assign_obj = WorkAssign()

            work_assign_obj.wa_compId = workId.wcompId
            work_assign_obj.wa_clientId = workId.clientId
            work_assign_obj.wa_work_regId = workId
            work_assign_obj.wa_work_allocate = seletedTl
            work_assign_obj.wa_from_date = sdate
            work_assign_obj.wa_due_date = duedate
            work_assign_obj.wa_discription = discription
            work_assign_obj.wa_file = any_file
            work_assign_obj.wa_status = 1
            work_assign_obj.save()

            work_assign_obj.wa_tasksId.add(*client_task)
            work_assign_obj.save()

            success = True
            success_text= 'Work and Task add successful.' 

            works = WorkRegister.objects.filter(wcompId=dash_details.emp_comp_id).order_by('-id')
            tl_list = EmployeeRegister_Details.objects.filter(emp_department_id=dash_details.emp_department_id,
                                                            emp_designation_id__dashboard_id=2)
            
            client_task = ClientTask_Register.objects.all()
            
            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'works':works,'tl_list':tl_list,
                    'client_task':client_task,'success':success,
                    'success_text':success_text}

            return render(request,'HD_workAllocate.html',content)

    else:
            return redirect('/')
    

def get_client_tasks(request):
    client_id = request.GET.get('client_id')
    
    # Fetch data from the ClientTaskRegister model based on the selected client_id
    client_tasks = ClientTask_Register.objects.filter(client_Id=client_id).values('id', 'task_name')
    
    return JsonResponse(list(client_tasks), safe=False)

def head_pendingworkView(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        assigned_works = WorkAssign.objects.filter(wa_compId=dash_details.emp_comp_id,wa_status=1).order_by('-id')

        tl_list = EmployeeRegister_Details.objects.filter(emp_department_id=dash_details.emp_department_id,
                                                          emp_designation_id__dashboard_id=2)
        
        client_task = ClientTask_Register.objects.all()
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'assigned_works':assigned_works,'tl_list':tl_list,
                   'client_task':client_task}

        return render(request,'HD_workpending.html',content)

    else:
            return redirect('/')
    
     
    
def head_WorkProgress(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        works = WorkRegister.objects.filter(wcompId=dash_details.emp_comp_id).order_by('-id')
       
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'works':works}


        return render(request,'HD_workProgress.html',content)

    else:
            return redirect('/')    

def head_clientWorkDetails(request,pk):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        client = ClientRegister.objects.get(id=pk)

        works = WorkRegister.objects.filter(clientId=client)

        tasks = ClientTask_Register.objects.filter(client_Id=client)
       
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'client':client,'works':works,'tasks':tasks}


        return render(request,'HD_client_WorkMonitor.html',content)

    else:
            return redirect('/')    

     

def head_tasksForWork(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        try:
            task_add_obj = Work_Task.objects.get(task_name='Lead Collection')
            pass

        except Work_Task.DoesNotExist:
            task_obj = Work_Task()
            task_obj.task_name = 'Lead Collection'
            task_obj.task_discription = 'Efficient lead collection is the cornerstone of successful business growth.'
            task_obj.comp_taskid = dash_details.emp_comp_id
            task_obj.save()
             

        data_box = {}
        if request.POST:
             
            taskName = request.POST['task_name']
            taskDiscription = request.POST['task_discription']

            task_obj = Work_Task()
            task_obj.task_name = taskName
            task_obj.task_discription = taskDiscription
            task_obj.comp_taskid = dash_details.emp_comp_id
            task_obj.save()
            success = True
            success_text= 'Task add successful.' 
                
            data_box = {'success':success,'success_text':success_text}
            
            
        Tasks = Work_Task.objects.filter(comp_taskid=dash_details.emp_comp_id.id)

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'Tasks':Tasks}
        
        content = {**data_box, **content}

        return render(request,'HD_workTasks.html',content)

    else:
            return redirect('/')
     


# Employee Section ---------------------------------


def Head_employees_section(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications}

        return render(request,'HD_employeeSection.html',content)

    else:
            return redirect('/')    


def head_viewEmployees(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'employees':employees}

        return render(request,'HD_employeeView.html',content)

    else:
            return redirect('/')    


def head_employeeAllocate(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

          # Team Leads featch----
        Team_leads_desig_obj = DesignationRegister_details.objects.get(dashboard_id=2) 
        Team_leads = EmployeeRegister_Details.objects.filter(emp_designation_id=Team_leads_desig_obj,logreg_id__active_status=1)
        TeamLead_emp_ids = [leads.id for leads in Team_leads]

        data_box ={}

        if request.POST:
            allocateTo =  request.POST['alocated_to']
            employee_list = request.POST.getlist('selected_emp')
            dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

            count_allocate = 0

            for emp_id in employee_list:
                allocate_obj = Allocation_Details()
                allocate_obj.allocatEmp_id = EmployeeRegister_Details.objects.get(id=int(emp_id))
                allocate_obj.allocat_to = EmployeeRegister_Details.objects.get(id=int(allocateTo))
                allocate_obj.allocate_status = 1
                allocate_obj.alloaction_date = date.today()
                allocate_obj.save()
                count_allocate =count_allocate +  1
                success = True
                success_text= str(count_allocate) + " " +'Allocation successful.' 
                
                data_box = {'success':success,'success_text':success_text}


             
        # Allocated Employees -------------------
        allocated_emp = Allocation_Details.objects.filter(allocate_status=1)
        allocated_emp_ids = [allocation.allocatEmp_id.id for allocation in allocated_emp]

        # Pending to allocate ------------
        allocate_employees = EmployeeRegister_Details.objects.filter(
            emp_comp_id=dash_details.emp_comp_id,logreg_id__active_status=1).exclude(
            id__in=allocated_emp_ids).exclude(
            id=dash_details.id).exclude(
            id__in=TeamLead_emp_ids)
        
        allocation_counts = Allocation_Details.objects.values('allocat_to__id', 'allocat_to__emp_name').annotate(count=Count('allocatEmp_id'))
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'Team_leads':Team_leads,
                   'employees':allocate_employees,
                   'allocation_counts':allocation_counts}
        
        content = {**data_box, **content}

        return render(request,'HD_employeeAllocate.html',content)

    else:
            return redirect('/')    


def head_employeeAllocated_list(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id,logreg_id__active_status=1)

        Team_leads_desig_obj = DesignationRegister_details.objects.get(dashboard_id=2) 
        Team_leads = EmployeeRegister_Details.objects.filter(emp_designation_id=Team_leads_desig_obj)
        TeamLead_emp_ids = [leads.id for leads in Team_leads]
        
        allocated_employees = Allocation_Details.objects.filter(allocat_to__in=TeamLead_emp_ids).order_by('allocat_to')

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'allocated_employees':allocated_employees,
                   'Team_leads':Team_leads,
                   'employees':employees}

        return render(request,'HD_employeeAllocatedList.html',content)

    else:
            return redirect('/')    

#Leave View-------
def head_employee_leaves(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        today = date.today()

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id,logreg_id__active_status=1)
        employee_ids = employees.values_list('id', flat=True)

        employees_leaves = EmployeeLeave.objects.filter(start_date__lte=today,end_date__gte=today,emp_id__in=employee_ids)

        if request.POST:
             
            if request.POST['emp_name'] == '0' and request.POST['fDate'] and request.POST['toDate'] :

                employees_leaves = EmployeeLeave.objects.filter(start_date__gte=request.POST['fDate'],end_date__lte=request.POST['toDate'],emp_id__in=employee_ids)
            
            elif request.POST['emp_name'] and request.POST['fDate'] and request.POST['toDate'] :

                emp_obj = EmployeeRegister_Details.objects.get(id=int(request.POST['emp_name']))
                employees_leaves = EmployeeLeave.objects.filter(start_date__gte=request.POST['fDate'],end_date__lte=request.POST['toDate'],emp_id=emp_obj)
                 
            
            elif request.POST['emp_name'] != '0' :
                emp_id = int(request.POST['emp_name'])
                emp_obj = EmployeeRegister_Details.objects.get(id=emp_id)
                employees_leaves = EmployeeLeave.objects.filter(emp_id=emp_obj)

            else:

                employees_leaves = EmployeeLeave.objects.filter(start_date__lte=today,end_date__gte=today,emp_id__in=employee_ids)
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'employees_leaves':employees_leaves}

        return render(request,'HD_employeeLeave.html',content)

    else:
            return redirect('/')     


# Schedules View -------------

def head_employee_schedules(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        today = date.today()

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id,logreg_id__active_status=1)
        employee_ids = employees.values_list('id', flat=True)

        schedules = EmployeeSchedule.objects.filter(emp_id__in=employee_ids,schedule_date=today)

        if request.POST:
             
            if request.POST['emp_name'] == '0' and request.POST['fDate'] and request.POST['toDate']:
                 
                schedules = EmployeeSchedule.objects.filter(schedule_date__gte=request.POST['fDate'],schedule_date__lte=request.POST['toDate'],emp_id__in=employee_ids)
                 
            elif request.POST['emp_name'] and request.POST['fDate'] and request.POST['toDate'] :

                emp_obj = EmployeeRegister_Details.objects.get(id=int(request.POST['emp_name']))
                schedules = EmployeeSchedule.objects.filter(schedule_date__gte=request.POST['fDate'],schedule_date__lte=request.POST['toDate'],emp_id=emp_obj)

            elif request.POST['emp_name'] != '0' :
                emp_id = int(request.POST['emp_name'])
                emp_obj = EmployeeRegister_Details.objects.get(id=emp_id)
                schedules = EmployeeSchedule.objects.filter(emp_id=emp_obj)

            else:
                schedules = EmployeeSchedule.objects.filter(emp_id__in=employee_ids,schedule_date=today)
        
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'schedules':schedules}

        return render(request,'HD_employeeSchedules.html',content)

    else:
            return redirect('/')     
     
# Actin Taken ----------------

def head_employee_actionTaken(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        today = date.today()

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id,logreg_id__active_status=1)
        employee_ids = employees.values_list('id', flat=True)

        actions_taken = ActionTaken.objects.filter(act_emp_id__in=employee_ids)

        if request.POST:
             
            if request.POST['emp_name'] == '0' and request.POST['fDate'] and request.POST['toDate']:
                 
                actions_taken = ActionTaken.objects.filter(action_date__gte=request.POST['fDate'],action_date__lte=request.POST['toDate'],act_emp_id__in=employee_ids)
                 
            elif request.POST['emp_name'] and request.POST['fDate'] and request.POST['toDate'] :

                emp_obj = EmployeeRegister_Details.objects.get(id=int(request.POST['emp_name']))
                actions_taken = ActionTaken.objects.filter(action_date__gte=request.POST['fDate'],action_date__lte=request.POST['toDate'],act_emp_id=emp_obj)

            elif request.POST['emp_name'] != '0' :
                emp_id = int(request.POST['emp_name'])
                emp_obj = EmployeeRegister_Details.objects.get(id=emp_id)
                actions_taken = ActionTaken.objects.filter(act_emp_id=emp_obj)

            else:
                actions_taken = ActionTaken.objects.filter(act_emp_id__in=employee_ids)
             

        
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'actions_taken':actions_taken}

        return render(request,'HD_employeeActionTaken.html',content)

    else:
            return redirect('/')     
     

# Feedback -------------------

def head_employee_feedback(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        today = date.today()

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=dash_details.emp_comp_id,logreg_id__active_status=1)
        employee_ids = employees.values_list('id', flat=True)

        schedules = EmployeeSchedule.objects.filter(emp_id__in=employee_ids,schedule_date=today)

        
        
        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'schedules':schedules}

        return render(request,'HD_employeeFeedback.html',content)

    else:
            return redirect('/')     
     

     
# =================================End Employeee Section ===============================

#Schedule -------------------------------------------

def head_schedule(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
         # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
          
        today = date.today()
        schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date=today)
        schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'schedules':schedules,
                   'schedule_days':schedule_days}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')
    
    
def head_scheduleRemove(request,pk):
     
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
         # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        schedule_remove = EmployeeSchedule.objects.get(id=pk)
        schedule_remove.delete()  

        error = True
        error_text = 'Schedule task removed'
        
        today = date.today()
        schedules = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today)
        schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'schedules':schedules,
                   'schedule_days':schedule_days,'error':error,'error_text':error_text}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')
    

def head_schedule_save(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        schedules = None
        schedule_days = None

        if request.POST:

            if request.POST['scheduleId']:

                schedule_obj = EmployeeSchedule.objects.get(id=int(request.POST['scheduleId']))

                schedule_obj.emp_id=dash_details
                schedule_obj.start_time=request.POST['stime']
                schedule_obj.end_time=request.POST['etime']
                schedule_obj.schedule_head=request.POST['task_head']
                schedule_obj.todo_content=request.POST['task_content']
                schedule_obj.log_time = timezone.now()
                schedule_obj.schedule_date = date.today()
                schedule_obj.save()

                today = date.today()
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date=today)
                schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()
                success_text = 'Schedule edit successful.'
                success = True

            else:

    
                schedule_obj = EmployeeSchedule()

                schedule_obj.emp_id=dash_details
                schedule_obj.start_time=request.POST['stime']
                schedule_obj.end_time=request.POST['etime']
                schedule_obj.schedule_head=request.POST['task_head']
                schedule_obj.todo_content=request.POST['task_content']
                schedule_obj.log_time = timezone.now()
                schedule_obj.schedule_date = request.POST['schedule_date']

                schedule_obj.save()

                today = date.today()
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date=today)
                schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

                success_text = 'Schedule save successful.'
                success = True

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'success_text':success_text,
                   'success':success,
                   'schedules':schedules,
                   'schedule_days':schedule_days}

        return render(request,'HD_dayTaskschedule.html',content)

    else:
            return redirect('/')


def ScheduleEdit(request):

    schedule_id = request.GET.get('scheduleid')
    try:
            schedule = EmployeeSchedule.objects.get(id=schedule_id)
           
            data = {
                'scheduleid':schedule.id,
                'start_time': schedule.start_time,
                'end_time': schedule.end_time,
                'task_head': schedule.schedule_head,
                'task_content': schedule.todo_content,
            }
            return JsonResponse(data)
    except EmployeeSchedule.DoesNotExist:
            return JsonResponse({'error': 'Schedule not found'}, status=404)  


def update_schedule_status(request):
        schedule_id = request.POST.get('schedule_id')
        checked = request.POST.get('checked')

        # Retrieve the schedule by ID
        schedule = EmployeeSchedule.objects.get(id=schedule_id)
        if schedule.schedule_status == 0:
            schedule.schedule_status =  1
        else: 
            schedule.schedule_status =  0
        schedule.save()
        return JsonResponse({'success': True})


def head_schedulesearchBy_date(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
         # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        today = date.today()

        if request.POST:
            
            if request.POST['f_date'] and request.POST['t_date']:

                fdate = request.POST['f_date']
                tdate = request.POST['t_date']
            
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date__gte=fdate,schedule_date__lte=tdate)
            
            else:
                schedules = EmployeeSchedule.objects.filter(emp_id=dash_details,schedule_date=today)

            schedule_days = EmployeeSchedule.objects.filter(emp_id=dash_details, schedule_date=today).values('schedule_date').distinct()

            content = {'emp_dash':emp_dash,
                    'dash_details':dash_details,
                    'notifications':notifications,
                    'schedules':schedules,
                    'schedule_days':schedule_days}

            return render(request,'HD_dayTaskschedule.html',content)
        else:
             
             return redirect('head_schedule')

    else:
            return redirect('/')
     


def head_employees_schedule(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1).exclude(Q(id=dash_details.id))

        success_text, schedules, employee_name = None, None, None
        success = False

        today = date.today()

        if request.POST: 

            if request.POST['employeeId']!=0:  

                employee_id= int(request.POST['employeeId'])

                try:
                    schedules = EmployeeSchedule.objects.filter(emp_id__id=employee_id,schedule_date__gte=today,
                    schedule_date__lte=today).order_by('start_time')
                except EmployeeSchedule.DoesNotExist:
                    schedules = None

                try:
                    employee_name = EmployeeRegister_Details.objects.get(id=employee_id)
                except EmployeeRegister_Details.DoesNotExist:
                    employee_name = None
            
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'success':success,
                   'today':today,'success_text':success_text,
                   'employees':employees,'schedules':schedules,'employee_name':employee_name}

        return render(request,'HD_employees_dayTaskschedule.html',content)

    else:
            return redirect('/')
    
     
def head_employee_scheduleAdd(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1).exclude(Q(id=dash_details.id))


        today = date.today()

        if request.POST:   

            employee_id= int(request.POST['add_employeeId'])
                 
            schedule_obj = EmployeeSchedule()

            schedule_obj.emp_id=EmployeeRegister_Details.objects.get(id=employee_id)
            schedule_obj.start_time=request.POST['stime']
            schedule_obj.end_time=request.POST['etime']
            schedule_obj.schedule_head=request.POST['task_head']
            schedule_obj.todo_content=request.POST['task_content']
            schedule_obj.log_time = timezone.now()
            schedule_obj.schedule_date = request.POST['schedule_date']

            schedule_obj.save()

            emp_obj=EmployeeRegister_Details.objects.get(id=int(request.POST['add_employeeId']))

            schedules = EmployeeSchedule.objects.filter(emp_id__id=int(request.POST['add_employeeId']),schedule_date__gte=today,
            schedule_date__lte=today).order_by('start_time')
            
            success_text = 'Schedule saved for ' + emp_obj.emp_name + ' successfully.'
            success = True 

            # Notification add 

            Notification_obj = Notification()
            Notification_obj.emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['add_employeeId']))
            Notification_obj.notific_head = 'Schedule Update'
            Notification_obj.notific_content = 'There is change in your schedule , Please check the schedule section '
            Notification_obj.save()

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'success':success,
                   'today':today,'success_text':success_text,
                   'employees':employees,'schedules':schedules,
                   'employee_name':emp_obj}

            return render(request,'HD_employees_dayTaskschedule.html',content)
      
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'employees':employees}

        return render(request,'HD_employees_dayTaskscheduleAdd.html',content)

    else:
            return redirect('/')

    
def head_employeeScheduleEdit(request,pk):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1).exclude(Q(id=dash_details.id))

        schedules = EmployeeSchedule.objects.get(id=pk)

        today = date.today()

        if request.POST:   

            employee_id= int(request.POST['add_employeeId'])
                 
            schedule_obj = EmployeeSchedule()

            schedule_obj.emp_id=EmployeeRegister_Details.objects.get(id=employee_id)
            schedule_obj.start_time=request.POST['stime']
            schedule_obj.end_time=request.POST['etime']
            schedule_obj.schedule_head=request.POST['task_head']
            schedule_obj.todo_content=request.POST['task_content']
            schedule_obj.log_time = timezone.now()
            schedule_obj.schedule_date = request.POST['schedule_date']

            schedule_obj.save()

            emp_obj=EmployeeRegister_Details.objects.get(id=int(request.POST['add_employeeId']))

            schedules = EmployeeSchedule.objects.filter(emp_id__id=int(request.POST['add_employeeId']),schedule_date__gte=today,
            schedule_date__lte=today).order_by('start_time')
            
            success_text = 'Schedule saved for ' + emp_obj.emp_name + ' successfully.'
            success = True      

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'success':success,
                   'today':today,'success_text':success_text,
                   'employees':employees,'schedules':schedules,
                   'employee_name':emp_obj}

            return render(request,'HD_employees_dayTaskschedule.html',content)
      
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,'schedules':schedules,
                   'employees':employees}

        return render(request,'HD_employees_dayTaskscheduleAdd.html',content)

    else:
            return redirect('/')


def head_scheduleFilter(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

          # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')
        
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1).exclude(Q(id=dash_details.id))
      

        schedules = None 
        emp_obj=None
        today = date.today()

        if request.POST:
             
            empId = request.POST['emp_name']
            from_date = request.POST['fDate']
            to_date = request.POST['toDate']
       

            if empId != '0' and from_date and to_date :

                emp_obj = EmployeeRegister_Details.objects.get(id=empId)
                schedules = EmployeeSchedule.objects.filter(emp_id=emp_obj,schedule_date__gte=from_date,
                schedule_date__lte=to_date).order_by('emp_id')
            
            elif empId == '0' and from_date and to_date :

                schedules = EmployeeSchedule.objects.filter(emp_id__in=employees,schedule_date__gte=from_date,
                schedule_date__lte=to_date).order_by('emp_id')

            elif empId != '0' :

                emp_obj = EmployeeRegister_Details.objects.get(id=empId)
                schedules = EmployeeSchedule.objects.filter(emp_id=emp_obj,schedule_date__gte=today,
                schedule_date__lte=today).order_by('emp_id')

            else:
                schedules = EmployeeSchedule.objects.filter(emp_id__in=employees,schedule_date__gte=today,
                schedule_date__lte=today).order_by('emp_id')
        
        else:
            
            schedules = EmployeeSchedule.objects.filter(emp_id__in=employees,schedule_date__gte=today,
            schedule_date__lte=today).order_by('emp_id')
                 

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'schedules':schedules,'emp_obj':emp_obj}

        return render(request,'HD_scheduleFilter.html',content)

    else:
            return redirect('/')
     

# Feedback -------------------------

def head_feedback(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

          # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)

        feedback_data = Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')


        # Saveing Feedback 
        if request.POST:

            feedback_obj = Feedback()
            feedback_obj.feedback_emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['to_id']))
            feedback_obj.from_id = dash_details.id
            feedback_obj.from_name = dash_details.emp_name
            feedback_obj.feedback_content = request.POST['feedback_content']
            feedback_obj.feedback_date = date.today()
            feedback_obj.save()

            success=True
            success_text = 'Feedback add successfully.'

            feedback_data =Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,

                   'employees':employees,
                   'feedback_data':feedback_data,
                   'success':success,
                   'success_text':success_text}
        
        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,

                   'employees':employees,
                   'feedback_data':feedback_data}

        return render(request,'HD_feedback.html',content)

    else:
            return redirect('/')


def feedback_Typechange(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)

        selected_value = request.GET.get('value')
    
        if selected_value == '1':
            feedback_data =Feedback.objects.filter(feedback_emp_id__in=employees).exclude(
            Q(feedback_emp_id=dash_details) | Q(feedback_emp_id=None)).order_by('-id')
        else:
            feedback_data =Feedback.objects.filter(feedback_emp_id=dash_details).order_by('-id')
        
        data_list = []
        for feedback in feedback_data:
            data = {
                'feedback_date': feedback.feedback_date,
               
                'from_name': feedback.from_name,
                
                'to_name': feedback.feedback_emp_id.emp_name,
                'feedback_content': feedback.feedback_content
            }
            data_list.append(data)
        
        return JsonResponse(data_list, safe=False)
     

# Complaints ---------------------

def head_complaints(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)
        complaints_data = Complaints.objects.filter(complaint_emp_id__in=employees).order_by('status')

        # Save action taken to the selected complaint
        if request.POST:
            complaints_obj = Complaints.objects.get(id=int(request.POST['complaintId']))
            complaints_obj.action = request.POST['action_content']
            complaints_obj.action_date = date.today()
            complaints_obj.status = 1
            complaints_obj.save()

            success=True
            success_text = 'Response add successfully.'
            complaints_data = Complaints.objects.filter(complaint_emp_id__in=employees).order_by('status')

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'complaints_data':complaints_data,
                   'success':success,
                   'success_text':success_text}

        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'complaints_data':complaints_data}

        return render(request,'HD_complaints.html',content)

    else:
            return redirect('/')
     

# Action Taken -------------------

def head_actionTaken(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        action_taken_data = ActionTaken.objects.filter(act_emp_id__in=employees,act_from_id=dash_details.id)

        # Save data
        if request.POST:
             
             action_taken_obj = ActionTaken()
             action_taken_obj.act_emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['action_employeeId']))
             action_taken_obj.act_from_id = dash_details.id
             action_taken_obj.act_from_name = dash_details.emp_name
             action_taken_obj.act_head = request.POST['reason_content_head']
             action_taken_obj.act_reason = request.POST['reason_content']
             action_taken_obj.act_content = request.POST['what_action_content']
             action_taken_obj.action_date = request.POST['action_taken_date']
             action_taken_obj.status = 1
             action_taken_obj.save()

             success=True
             success_text = 'Action taken add successfully.'
             
             # Notification Add 
             Notification_obj = Notification()
             Notification_obj.emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['action_employeeId']))
             Notification_obj.notific_head = 'Action Taken'
             Notification_obj.notific_content = 'An action is taken for you , Please check the action taken section '
             Notification_obj.save()

             action_taken_data = ActionTaken.objects.filter(act_emp_id__in=employees)

             content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data,
                   'success':success,
                   'success_text':success_text}

        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data}

        return render(request,'HD_actionTaken.html',content)

    else:
            return redirect('/')


def head_action_takenEdit(request,pk):  
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)
        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company)
        
        # dummy notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)
        
        action_taken_data =  ActionTaken.objects.get(id=pk)

        # Edit and Save data
        if request.POST:
             
             action_taken_obj = ActionTaken.objects.get(id=pk)
             action_taken_obj.act_emp_id = EmployeeRegister_Details.objects.get(id=int(request.POST['action_employeeId']))
             action_taken_obj.act_from_id = dash_details.id
             action_taken_obj.act_from_name = dash_details.emp_name
             action_taken_obj.act_head = request.POST['reason_content_head']
             action_taken_obj.act_reason = request.POST['reason_content']
             action_taken_obj.act_content = request.POST['what_action_content']
             action_taken_obj.action_date = request.POST['action_taken_date']
             action_taken_obj.status = 1
             action_taken_obj.save()

             success=True
             success_text = 'Action taken edit successfully.'
             action_taken_data = ActionTaken.objects.filter(act_emp_id__in=employees)

             content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data,
                   'success':success,
                   'success_text':success_text}
             
             return render(request,'HD_actionTaken.html',content)
        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'action_taken_data':action_taken_data}
             

        return render(request,'HD_actionTakenedit.html',content)

    else:
            return redirect('/')  


# Leave ------------------------------

def count_weekdays(start_date, end_date):
    current_date = start_date
    weekdays_count = 0

    # Iterate through each date within the range
    while current_date <= end_date:
        # Check if the current date is a weekday (Monday to Saturday)
        if current_date.weekday() < 6:
            weekdays_count += 1
        
        # Move to the next day
        current_date += timedelta(days=1)

    return weekdays_count


def head_leave(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1).exclude(
            Q(id=dash_details.id) | Q(id=None)).order_by('-id')
        
        #Employee id list----
        employees_list = EmployeeRegister_Details.objects.filter(emp_comp_id=company).order_by('-id').values_list('id', flat=True)
        
        
        # notification-----------
        notifications = EmployeeRegister_Details.objects.filter(logreg_id=emp_dash)

        #Head Leave --------
        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')

        #employees leave
        empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees_list).exclude(
            Q(emp_id=dash_details) | Q(emp_id=None)).order_by('-id')
        
        
        leave_request = EmployeeLeave.objects.filter(leave_status=0)

        #save date 
        if request.POST:
             leave_obj = EmployeeLeave()
             leave_obj.start_date = request.POST['fromDate']
             leave_obj.end_date = request.POST['toDate']
             leave_obj.leave_type = request.POST['type_select']
             leave_obj.leave_reason = request.POST['reason_content']
             leave_obj.emp_id = dash_details
             leave_obj.leave_apply_date = date.today()

             # day calculation
             
             start_date_str = request.POST['fromDate']
             end_date_str = request.POST['toDate'] 

             # Convert the date strings to datetime objects
             start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
             end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

             # Calculate the difference in days
             weekdays_count = (count_weekdays(start_date, end_date))
             
             leave_obj.no_of_days = weekdays_count
             leave_obj.save()
             
             success=True
             success_text = 'Leave applied successfully, waiting for approvel.'

             leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
        

             content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'employees':employees,
                   'empleave_data':empleave_data,
                   'leave_request':leave_request,
                   'success':success,
                   'success_text':success_text,'leave_data':leave_data}

        else:

            content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'employees':employees,
                   'empleave_data':empleave_data,
                   'leave_request':leave_request,
                   'notifications':notifications,
                   'leave_data':leave_data}

        return render(request,'HD_leave.html',content)

    else:
            return redirect('/')


def head_leaveApprove_Reject(request):

    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company,logreg_id__active_status=1).exclude(
            Q(id=dash_details.id) | Q(id=None)).order_by('-id')
        
        employees_leave = EmployeeRegister_Details.objects.filter(emp_comp_id=company)
        
        
        if request.method == 'POST':
            leave_id = request.POST.get('leaveId')
            action = request.POST.get('action')

            leave_obj = EmployeeLeave.objects.get(id=int(leave_id)) 

            if action == 'approve':
                leave_obj.leave_status = 1 
                leave_obj.leave_statuChange_date = date.today()
                leave_obj.save()

                # Adding Notification --------

                notification_obj = Notification()

                notification_obj.emp_id = dash_details
                notification_obj.notific_head = 'Leave Approved'
                notification_obj.notific_content = "I'm pleased to inform you that your request for " + str(leave_obj.leave_type) + "leave from " + str(leave_obj.start_date) + " to " + str(leave_obj.end_date) + " has been approved."


                notification_obj.save()
                
            elif action == 'reject':

                leave_obj.leave_status = 2
                leave_obj.leave_statuChange_date = date.today()
                leave_obj.save()

                   # Adding Notification --------

                notification_obj = Notification()

                notification_obj.emp_id = dash_details
                notification_obj.notific_head = 'Leave Rejectd'
                notification_obj.notific_content = "I regret to inform you that your request for " + leave_obj.leave_type + " from " + str(leave_obj.start_date) + " to " + str(leave_obj.end_date) + " has been reviewed and unfortunately, we are unable to approve it at this time."


                notification_obj.save()



            leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
            empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees_leave).order_by('-id')
            leave_request = EmployeeLeave.objects.filter(leave_status=0)
            
            # Serialize the leave_request queryset to JSON
            leave_request_json = serializers.serialize('json', leave_request)
            
            my_leave = render(request, 'HD_leaveAjaxresponse.html', {'leave_data': leave_data,'dash_details':dash_details}).content.decode('utf-8')
            employe_leave = render(request, 'HD_employeeLeave_ajaxresponse.html', {'emp_data': empleave_data,'employees':employees}).content.decode('utf-8')

        # Return the updated HTML content in the AJAX response
            response_data = {'html_content': employe_leave,'my_leave':my_leave,'leave_request':leave_request_json}
            return JsonResponse(response_data)

        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=400)
       

    else:
            return redirect('/')



def head_leaveSearch(request):
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)

        company = BusinessRegister_Details.objects.get(id=dash_details.emp_comp_id.id)

        employees = EmployeeRegister_Details.objects.filter(emp_comp_id=company).exclude(
            Q(id=dash_details.id) | Q(id=None)).order_by('-id')
        

        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
        empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees).order_by('-id')
        leave_request = EmployeeLeave.objects.filter(leave_status=0)
        leave_request_json = serializers.serialize('json', leave_request)
        

        if request.method == 'POST':
            employeeid = request.POST.get('searchValue')
            fdate = request.POST.get('f_Date')
            edate = request.POST.get('e_Date')

            if fdate and edate :

                if  dash_details.id == int(employeeid):
                    try:
                        leave_data = EmployeeLeave.objects.filter(emp_id__id=int(employeeid),start_date__gte=fdate,end_date__lte=edate).order_by('-id')
                    except EmployeeLeave.DoesNotExist:
                        leave_data = EmployeeLeave.objects.filter(emp_id=dash_details).order_by('-id')
                    
                else:
                    try:
                        empleave_data = EmployeeLeave.objects.filter(emp_id__id=int(employeeid),start_date__gte=fdate,end_date__lte=edate).order_by('-id')
                    except EmployeeLeave.DoesNotExist:
                        empleave_data = EmployeeLeave.objects.filter(emp_id__in=employees).order_by('-id')
            else: 
                 
                 return redirect('head_leave')

            my_leave = render(request, 'HD_leaveAjaxresponse.html', {'leave_data': leave_data,'dash_details':dash_details}).content.decode('utf-8')
            employe_leave = render(request, 'HD_employeeLeave_ajaxresponse.html', {'emp_data': empleave_data,'employees':employees}).content.decode('utf-8')

            response_data = {'html_content': employe_leave,'my_leave':my_leave,'leave_request':leave_request_json}
            return JsonResponse(response_data)

        # Return an error response if the request method is not POST
        return JsonResponse({'error': 'Invalid request method'}, status=400)
       

    else:
            return redirect('/')
    

# Notification -----------------------


def head_allnotification(request):
    
    if 'emp_id' in request.session:
        if request.session.has_key('emp_id'):
            emp_id = request.session['emp_id']
           
        else:
            return redirect('/')
        
        emp_dash = LogRegister_Details.objects.get(id=emp_id)
        dash_details = EmployeeRegister_Details.objects.get(logreg_id=emp_dash)
        
        # Notification-----------
        notifications = Notification.objects.filter(emp_id=dash_details,notific_status=0).order_by('-notific_date')

        notifications_data = Notification.objects.filter(Q(notific_status=0) | Q(notific_status=1),emp_id=dash_details,).order_by('-notific_date')
        
        

        content = {'emp_dash':emp_dash,
                   'dash_details':dash_details,
                   'notifications':notifications,
                   'notifications_data':notifications_data}

        return render(request,'HD_allnotification.html',content)

    else:
            return redirect('/')


def head_notificationUpdate(request):
    
    if request.method == 'POST':
        notification_id = request.POST.get('notification_id')
        
        try:
            notification = Notification.objects.get(pk=notification_id)
            notification.notific_status = 1
            notification.save()
            return JsonResponse({'status': 'success', 'message': 'Notification status updated'})
            

        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notification not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


@method_decorator(csrf_exempt, name='dispatch')
def head_delete_notifications(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_ids[]')

        try:
            # Delete notifications with the selected IDs
            Notification.objects.filter(id__in=selected_ids).update(notific_status=2)
            return JsonResponse({'status': 'success', 'message': 'Notifications deleted successfully'})
        except Notification.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Notification not found'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def head_logout(request):
    request.session.pop('emp_id', None)
    return redirect('login_page')
