from django.shortcuts import render,redirect
from django.contrib import messages
from .models import regitration,evaluationI,evaluationII

# Create your views here.
def front(request):
    return render(request,"front.html")

def registerss(request):
    
    if request.method == "POST":
        datass = evaluationII()

        datass.S_No = request.POST.get('S_No')
        datass.Guide_Name = request.POST.get('Guide_Name')
        datass.Project_Title = request.POST.get('Project_Title')
        datass.Student_Name = request.POST.get('Full_Name')
        datass.System_Id = request.POST.get('System_Id')
        datass.Roll_No = request.POST.get('Roll_No')
        datass.Team_size = request.POST.get('Team_Size')
        datass.Project_Category = request.POST.get('Project_Category')
        datass.Section = request.POST.get('Section')
        datass.Project_Passcode = request.POST.get('Project_Passcode')
        datass.Student_Email = request.POST.get('Email')
        datass.Phone_Number = request.POST.get('Phone_Number')
        datass.Project_Form_Number = request.POST.get('Project_Form_Number')
        datass.Pannel_Number = request.POST.get('Pannel_Number')
        datass.Attendance_In_Eval_2 = request.POST.get('Attendance_In_Eval_2')
        datass.Identification_of_problem_Domain = request.POST.get('Identification_Of_Problem_Domain')
        datass.Knowledge_Of_Problem_Domain = request.POST.get('Knowledge_Of_Problem_Domain')
        datass.Creativity_And_Originality_In_Problem = request.POST.get('Creativity_And_Originality_In_Problem')
        datass.Knowledge_Purpose_And_Resource = request.POST.get('Knowledge_Purpose_And_Resource')
        datass.Team_Size_As_Project_Size = request.POST.get('Team_Size_As_Project_Size')
        datass.Project_Planning_And_Work_Distribution = request.POST.get('Project_Planning_And_Work_Distribution')
        datass.Oral_Communication = request.POST.get('Oral_Communication')
        datass.Quality_Of_Written_Proposal = request.POST.get('Quality_Of_Written_Proposal')
        datass.Guide_Marks = request.POST.get('Guide_Marks')
        datass.Quality_Of_Project_Title = request.POST.get('Quality_Of_Project_Title')
        datass.Total = request.POST.get('Total')
        datass.Remark= request.POST.get('Remark')
        
        messages.info(request,"Successfully Uploaded")

        datass.save()
        return redirect('registerss')
    else:
        return render(request,'evaluation-II.html')

def registers(request):

    if request.method == "POST":
        datas = evaluationI()

        datas.S_No = request.POST.get('S_No')
        datas.Guide_Name = request.POST.get('Guide_Name')
        datas.Project_Title = request.POST.get('Project_Title')
        datas.Student_Name = request.POST.get('Student_Name')
        datas.System_Id = request.POST.get('System_Id')
        datas.Roll_No = request.POST.get('Roll_No')
        datas.Team_size = request.POST.get('Team_Size')
        datas.Project_Category = request.POST.get('Project_Category')
        datas.Section = request.POST.get('Section')
        datas.Project_Passcode = request.POST.get('Project_Passcode')
        datas.Student_Email = request.POST.get('Email')
        datas.Phone_Number = request.POST.get('Phone_Number')
        datas.Project_Form_Number = request.POST.get('Project_Form_Number')
        datas.Pannel_Number = request.POST.get('Pannel_Number')
        datas.Attendance_In_Eval_1 = request.POST.get('Attendance_In_Eval_1')
        datas.Identification_of_problem_Domain = request.POST.get('Identification_Of_Problem_Domain')
        datas.Knowledge_Of_Problem_Domain = request.POST.get('Knowledge_Of_Problem_Domain')
        datas.Creativity_And_Originality_In_Problem = request.POST.get('Creativity_And_Originality_In_Problem')
        datas.Knowledge_Purpose_And_Resource = request.POST.get('Knowledge_Purpose_And_Resource')
        datas.Team_Size_As_Project_Size = request.POST.get('Team_Size_As_Project_Size')
        datas.Project_Planning_And_Work_Distribution = request.POST.get('Project_Planning_And_Work_Distribution')
        datas.Oral_Communication = request.POST.get('Oral_Communication')
        datas.Quality_Of_Written_Proposal = request.POST.get('Quality_Of_Written_Proposal')
        datas.Guide_Marks = request.POST.get('Guide_Marks')
        datas.Quality_Of_Project_Title = request.POST.get('Quality_Of_Project_Title')
        datas.Total = request.POST.get('Total')
        datas.Remark= request.POST.get('Remark')
        
        messages.info(request,"Successfully Uploaded")

        datas.save()
        return redirect('registers')
    else:
        return render(request,'evaluation-I.html')

def register(request):
    if request.method == "POST":
        data = regitration()

        data.S_No = request.POST.get('S_No')
        data.Guide_Name = request.POST.get('Guide_Name')
        data.Project_Title = request.POST.get('Project_Title')
        data.Student_Name = request.POST.get('Student_Name')
        data.System_Id = request.POST.get('System_Id')
        data.Roll_No = request.POST.get('Roll_No')
        data.Team_size = request.POST.get('Team_Size')
        data.Project_Category = request.POST.get('Project_Category')
        data.Section = request.POST.get('Section')
        data.Project_Passcode = request.POST.get('Project_Passcode')
        data.Student_Email = request.POST.get('Student_Email')
        data.Phone_Number = request.POST.get('Phone_Number')
        data.Project_Form_Number = request.POST.get('Project_Form_Number')
        data.Pannel_Number = request.POST.get('Pannel_Number')
        data.Attendance_In_Eval_0 = request.POST.get('Attendance_In_Eval_0')
        data.Identification_of_problem_Domain = request.POST.get('Identification_Of_Problem_Domain')
        data.Knowledge_Of_Problem_Domain = request.POST.get('Knowledge_Of_Problem_Domain')
        data.Creativity_And_Originality_In_Problem = request.POST.get('Creativity_And_Originality_In_Problem')
        data.Knowledge_Purpose_And_Resource = request.POST.get('Knowledge_Purpose_And_Resource')
        data.Team_Size_As_Project_Size = request.POST.get('Team_Size_As_Project_Size')
        data.Project_Planning_And_Work_Distribution = request.POST.get('Project_Planning_And_Work_Distribution')
        data.Oral_Communication = request.POST.get('Oral_Communication')
        data.Quality_Of_Written_Proposal = request.POST.get('Quality_Of_Written_Proposal')
        data.Guide_Marks = request.POST.get('Guide_Marks')
        data.Quality_Of_Project_Title = request.POST.get('Quality_Of_Project_Title')
        data.Total = request.POST.get('Total')
        data.Remark= request.POST.get('Remark')
        
        messages.info(request,"Successfully Uploaded")

        data.save()
        return redirect('register')
    else:
        return render(request,'evaluation.html')