from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
import json
from django.contrib import messages
from .forms import DmatsForm,ApplyShareForm
from django.contrib.auth.decorators import login_required
from .models import DmatsAccount, Share
from .scraping import *
import threading



#run in background thread 
def run_in_background(func):
    thread = threading.Thread(target=func)
    thread.start()




# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request,'home.html')



@login_required(login_url='/login/')
def dmatsaccount(request):
    if request.method == 'POST':
        dform = DmatsForm(request.POST)
        if dform.is_valid(): 
            instance = dform.save(commit=False)
            instance.user =request.user
            instance.save()
            messages.success(request,'Account Added successfully')
            return redirect('/dmatsaccount/')
        else:
            messages.error(request,dform.errors)
            return redirect('/dmatsaccount/')
    else:
        dform = DmatsForm()
        user = request.user
        dmats = DmatsAccount.objects.filter(user=user)
        context = {
            'dmats':dmats,
            'dform':dform
        }
    return render(request,'dmatsaccount.html',context)

@login_required(login_url='/login/')
def dmatsdelete(request,pk):
    dmat= DmatsAccount.objects.filter(user=request.user).get(id=pk)
    try:
        dmat.delete()
        messages.success(request,'Account deleted successfully')
    except:
        messages.error(request,'Failed to delete')
    return redirect('/dmatsaccount/')

@login_required(login_url='/login/')
def dmatsdeleteall(request):
    dmats = DmatsAccount.objects.filter(user=request.user)
    try:
        dmats.delete()
        messages.success(request,'All Accounts deleted successfully')
    except:
        messages.error(request,'Failed to delete')
    return redirect('/dmatsaccount/')


#globally declared 
@login_required(login_url='/login/')
def applyipo(request):
    #run in background thread
    run_in_background(web_driver.open_browser(web_driver))
    if request.method == 'POST':
        aform = ApplyShareForm(request.POST)
        
        if aform.is_valid():
            aform.save()
            sleep(2)
            ids = aform['username'].value()
            qty=aform['qty'].value()

            dmat = DmatsAccount.objects.filter(user=request.user).get(id=ids)
            capital=dmat.capital
            username = dmat.username
            password = dmat.password
            
            
            try:
                count = 0
                while web_driver.driver.current_url != "https://meroshare.cdsc.com.np/#/dashboard":
                    login(capital,username,password)
                    count+=1
                    sleep(1)
                    if web_driver.driver.current_url == "https://meroshare.cdsc.com.np/#/dashboard":
                        break
                    if count == 5:
                        break
                if web_driver.driver.current_url == "https://meroshare.cdsc.com.np/#/dashboard":
                    goto_asba()
                    sleep(0.2)
                    response = redirect('/applyshareid/')
                    response.set_cookie('ids',ids)
                    response.set_cookie('qty',qty)
                    return response
                else:
                    messages.error(request,'Could Not Login ! Check your credentials')
                    return redirect('/applyipo/')
            except:
                messages.error(request,'Timeout Error ! Try again later')
                close_browser()
                return redirect('/applyipo/')
        else:
            messages.error(request,aform.errors)
            return redirect('/applyipo/')
    else:
        aform = ApplyShareForm()
        aform.fields['username'].queryset = DmatsAccount.objects.filter(user=request.user)
        context = {
            'aform':aform
        }
        
    return render(request,'applyipo.html',context)
    

@login_required(login_url='/login/')
def applyshareid(request):
    if request.method == 'POST':
        ids = request.COOKIES.get('ids')

        dmat = DmatsAccount.objects.filter(user=request.user).get(id=ids)
        crn = dmat.crn
        pin = dmat.pin
        shareId = request.POST.get('shareId')
        qty = request.COOKIES.get('qty')
        if web_driver.driver.current_url == 'https://meroshare.cdsc.com.np/#/asba':
            try:
                ipo_selector(shareId)
            except:
                messages.error(request,'Looks like you have already applied for this IPO Or No Ipos Listed')
                
                return redirect('/applyipo/')
            try:
                applySuccess(qty, crn, pin)
                msg = web_driver.driver.find_element(By.CLASS_NAME,"toast-message").text
                if "success" in msg:
                    messages.success(request,msg)
                    
                    return redirect('/applyipo/')
                else:
                    messages.error(request, msg)
                   
                    return redirect('/applyipo/') 
            except:
                messages.error(request,'Could not apply for this IPO')
                  
        return redirect('/applyipo/')
    else:
        ids = request.COOKIES.get('ids')
        ipos = open_ipo_lister()
        messages.success(request,'Select the IPO you want to apply for')
        context = {
            'ipos':ipos,  
        }
        return render(request,'applyshareid.html',context)
    
@login_required(login_url='/login/')
def about(request):
    return render(request,'about.html')
