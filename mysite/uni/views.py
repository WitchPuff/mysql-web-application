from decimal import Decimal
from dis import Instruction
from django.shortcuts import render

# Create your views here.
from .models import Student, Takes, Course, Department, Instructor
from django.db.models import Count


def home(request):
    return render(request, 'uni/home.html')




def StudentQuery(req):
    ret = None
    msg = 0
    if req.method == "POST":
        #获取表单数据,如果获取不到,则为None
        id = req.POST.get("id",None)

        if len(id) == 5 and id.isdecimal():
            #定义字典
            stud = Student.objects.filter(id=id)
            if len(stud) == 0:
                msg = "Student ID Not Exist"
            else:
                stu = stud[0]
                ret = {'id':stu.id, 'name':stu.name, 'dept_name':stu.dept_name}
                crs = []
                for i in Takes.objects.filter(id=id).values('id', 'course', 'sec', 'semester','grade'):
                    crs.append((i['course'],i['grade']))
                cours = []
                if crs:
                    for i,j in crs:
                        c = Course.objects.filter(course_id=i)[0]
                        cour = {'course_id':c.course_id,'credits':c.credits,'grade':j}
                        cours.append(cour)
                ret.update({'courses':cours})
        else:
            msg = "Invalid Input. Check if your student id is a 5-bit number."
    return render(req, 'uni/student.html',{"i": ret,'msg':msg})



def CourseQuery(req):
    msg = 0
    ret = None
    if req.method == "POST":
        word = req.POST.get("word",None)
        if len(word) > 0:
            ret = []
            courses = Course.objects.filter(title__icontains=word)
            if len(courses) == 0:
                msg = "Course Not Exist"
            else:
                for crs in courses:
                    ret.append({'id':crs.course_id, 'title':crs.title, 'dept_name':crs.dept_name,'credits':crs.credits})
    return render(req, 'uni/course.html',{"i": ret,'msg':msg})

def failed(req):
    msg = 0
    ret = []
    id = Takes.objects.filter(grade='F').values("id").annotate(count=Count("id"))
    stu = []
    for i in id:
        if i['count'] > 1:
            stu.append(i['id'])
    for i in stu:
        s = Student.objects.get(id=i)
        ret.append({'id':s.id, 'name':s.name})
    if len(ret) == 0:
        msg ="Students who failed courses more than twice don't exist."
    return render(req, 'uni/who_failed.html',{"i": ret,'msg':msg})

def RegStu(req):
    stu = None
    msg = 0
    deptlist = Department.objects.all()
    if req.method == "POST":
        id = req.POST.get("id",None)
        name = req.POST.get("name",None)
        dept_name = req.POST.get("dept_name",None)
        if len(Student.objects.filter(id=id)) > 0:
            msg = "Student ID Already Exists"
        elif len(id) != 5 and id.isdecimal():
            msg = "Invalid Input. Check if your student id is a 5-bit number."
        elif len(name) > 20:
            msg = "Invalid Input. Check if your length of name is less than 20 bits."
        else:
            stu = {'id':id,'name':name,'dept_name':dept_name,'tot_credit':0}
            Student.objects.create(id=id,name=name,dept_name=Department(dept_name=dept_name),tot_cred=0)
            msg = "New student registered successfully!"
    return render(req, 'uni/reg_stu.html',{"i": stu,'msg':msg,'deptlist':deptlist})

def RegInst(req):
    inst = None
    msg = 0
    deptlist = Department.objects.all()
    if req.method == "POST":
        id = req.POST.get("id",None)
        name = req.POST.get("name",None)
        dept_name = req.POST.get("dept_name",None)
        salary = Decimal(req.POST.get("salary",0))
        if len(Instructor.objects.filter(id=id)) > 0:
            msg = "Instructor ID Already Exists"
        elif len(id) != 5 and id.isdecimal():
            msg = "Invalid Input. Check if your student id is a 5-bit number."
        elif len(name) > 20:
            msg = "Invalid Input. Check if your length of name is less than 20 bits."
        elif salary < 29000:
            msg = "Invalid Input. Check if your salary is more than 29000."
        else:
            inst = {'id':id,'name':name,'dept_name':dept_name,'salary':salary}
            Instructor.objects.create(id=id,name=name,dept_name=Department(dept_name=dept_name),salary=salary)
            msg = "New instructor registered successfully!"
    return render(req, 'uni/reg_inst.html',{"i": inst,'msg':msg,'deptlist':deptlist})