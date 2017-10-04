from django.shortcuts import render
from django.contrib.auth.models import User
from share_house.models import Meeting_info

# Create your views here.
def index_reg(request):
    print("Hello Login")
    if request.method=='POST':
        print("Hello Login2")
        email = request.POST['email']
        try:
            User.objects.get(email=email)
            print("이미 저장된 계정입니다.")
            return render(request, "index.html")
        except User.DoesNotExist:
            user = User.objects.create_user(request.POST['username'],email,request.POST['password'])
            print("생성됨")
            user.first_name=request.POST['phone_num']
            user.last_name = request.POST['major']
            user.save()
            print("저장됨")
            # request.session['username'] = user.username
            return render(request, "index.html",{"login_id":email})
        except User.MultipleObjectsReturned:
            status = "이미 저장된 계정입니다."
            return render(request, "index.html", {'status': status})
        # else:
        #     email=request.POST['login-email']
        #     password=request.POST['login-password']
        #     print(email)
        #     print(password)
        #     try:
        #         user = User.objects.get(email=email)
        #         if user.check_password(password):
        #             request.session['login_id'] = email
        #             return render(request, 'index.html', {"login_id": email})
        #         else:
        #             status = "Password가 틀렸습니다"
        #             return render(request, 'login_form.html', {"status": status})
        #     except User.DoesNotExist:
        #         status = "존재하지 않는 아이디입니다."
        #         return render(request, 'login_form.html', {"status": status})
    return render(request, "index.html")
def index(request):
    if request.method=='POST':
        email = request.POST['login-email']
        password = request.POST['login-password']
        print(email)
        print(password)
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                request.session['username'] = user.username
                return render(request, 'index.html', {"username": user.username})
            else:
                status = "Password가 틀렸습니다"
                return render(request, 'index.html', {"status": status})
        except User.DoesNotExist:
            status = "존재하지 않는 아이디입니다."
            return render(request, 'index.html', {"status": status})
    elif request.method=='GET':
        if request.session['username']!=None:
            return render(request, "index.html", {"username": request.session['username']})
        else:
            return render(request, "index.html")
    else:
        return render(request, "index.html")
def meeting(request):
    try:
        request.session['username']
    except:
        request.session['username']= None
    if request.method=='POST':
        email = request.POST['login-email']
        password = request.POST['login-password']
        print(email)
        print(password)
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                request.session['username'] = user.username
                return render(request, 'page-1.html', {"username": user.username})
            else:
                status = "Password가 틀렸습니다"
                return render(request, 'page-1.html', {"status": status})
        except User.DoesNotExist:
            status = "존재하지 않는 아이디입니다."
            return render(request, 'page-1.html', {"status": status})
    elif request.method=='GET':
        print(request.session['username'])
        if request.session['username']:
            return render(request, "page-1.html", {"username": request.session['username']})
        else:
            return render(request, "page-1.html")
    else:
        return render(request, "page-1.html")
    if request.session['username']!=None:
        print(request.session['username'])
        return render(request, "page-1.html",{"username": request.session['username']})
    return render(request, "page-1.html")
def logout(request):
    request.session['username']=None
    return render(request, "index.html")
def test2(request):
    if request.method=='POST':
        print(request.POST['meet_catagory'])
        print(request.POST['meet_title'])
        print(request.POST['meet_time_start'])
        print(request.POST['meet_time_end'])
        print(request.POST['meet_dur_start'])
        print(request.POST['meet_dur_end'])
        print(request.POST['meet_place'])
        print(request.POST['meet_comment'])
        meet_add = Meeting_info(
            meet_title=request.POST['meet_title'],
            meet_catagory = request.POST['meet_catagory'],
            meet_time_start = request.POST['meet_time_start'],
            meet_time_end = request.POST['meet_time_end'],
            meet_dur_start = request.POST['meet_dur_start'],
            meet_dur_end = request.POST['meet_dur_end'],
            meet_place = request.POST['meet_place'],
            meet_comment = request.POST['meet_comment']
        )
        meet_add.save()
        print("세이브완료")

    return render(request, "meet_form.html")