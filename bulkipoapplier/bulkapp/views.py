from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
import json
from django.contrib import messages
from .forms import DmatsForm,ApplyShareForm
from django.contrib.auth.decorators import login_required
from .models import DmatsAccount, Share
from .scraping import *

from django.core.cache import cache

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
  
    if request.method == 'POST':
        aform = ApplyShareForm(request.POST)
        
        if aform.is_valid():
            aform.save()
            sleep(2)
            ids = aform['username'].value()
            qty=aform['qty'].value()
            
            request.session['ids'] = ids
            request.session['qty'] = qty
            # Fetch DmatsAccount data outside the loop
            dmat = DmatsAccount.objects.select_related('user').get(id=ids, user=request.user)
            
            capital=dmat.capital
            username = dmat.username
            password = dmat.password
    
            try:
                count = 0
                web_driver.open_browser()
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
                    response = redirect('/applyshareid/')
                    return response
                else:
                    messages.error(request,'Could Not Login ! Check your credentials')
                    return redirect('/applyipo/')
            except:
                messages.error(request,'Timeout Error ! Try again later')
                web_driver.close_browser()
                return redirect('/applyipo/')
        else:
            messages.error(request,aform.errors)
            return redirect('/applyipo/')
    else:
        aform = ApplyShareForm()
        aform.fields['username'].queryset = DmatsAccount.objects.filter(user=request.user).select_related('user')
        context = {
            'aform':aform
        }
        
    return render(request,'applyipo.html',context)
    

@login_required(login_url='/login/')
def applyshareid(request):
    if request.method == 'POST':
        ids = request.session.get('ids')
        qty = request.session.get('qty')
        dmat = DmatsAccount.objects.filter(user=request.user, id=ids).first()
        crn = dmat.crn
        pin = dmat.pin
        shareId = request.POST.get('shareId')
        
        if web_driver.driver.current_url == 'https://meroshare.cdsc.com.np/#/asba':
            try:
                ipo_selector(shareId)
            except:
                messages.error(request,'Looks like you have already applied for this IPO \n Or No IPOS Avalable')
                
                return redirect('/applyipo/')
            try:
                apply_success(qty, crn, pin)
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
        ids = request.session.get('ids')
        ipos = cache.get('ipos')  # Check cache for ipos
        if not ipos:
            ipos = open_ipo_lister()
            cache.set('ipos', ipos, timeout=3600)  # Cache ipos for 1 hour
        
        messages.success(request,'Select the IPO you want to apply for')
        context = {
            'ipos':ipos,  
        }
        return render(request,'applyshareid.html',context)
    
@login_required(login_url='/login/')
def about(request):
    return render(request,'about.html')
