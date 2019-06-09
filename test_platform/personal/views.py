from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# MTV view
def say_hello(abc):
    input_name = abc.GET.get("name","")
    if input_name == "":
        #r如果name为空
         return HttpResponse("请求输入？name=name")
    return render(abc,"index.html",{"name": input_name})

def index(request):
    """
    登录的首页
    """
    if request.method=="GET":
        return render(request, "index.html", )
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        print(username)
        print(password)
        print(request.method)
        if username == "" or password == "":
            return render(request, "index.html", {
                "error": "用户名或密码为空"})
        if username == "admin" and password == "123":
            return HttpResponse("登录成功")
        else:
            return render(request, "index.html", {
                "error": "用户名或密码错误！"})
