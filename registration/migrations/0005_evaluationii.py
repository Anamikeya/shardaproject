# Generated by Django 3.0.8 on 2020-09-14 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_auto_20200914_0705'),
    ]

    operations = [
        migrations.CreateModel(
            name='evaluationII',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_No', models.CharField(max_length=100)),
                ('Guide_Name', models.CharField(max_length=100)),
                ('Project_Title', models.CharField(max_length=100)),
                ('Student_Name', models.CharField(max_length=100)),
                ('System_Id', models.CharField(max_length=100)),
                ('Roll_No', models.CharField(max_length=100)),
                ('Team_size', models.CharField(max_length=100)),
                ('Project_Category', models.CharField(max_length=100)),
                ('Section', models.CharField(max_length=100)),
                ('Project_Passcode', models.CharField(max_length=100)),
                ('Student_Email', models.CharField(max_length=100)),
                ('Phone_Number', models.CharField(max_length=20)),
                ('Project_Form_Number', models.IntegerField()),
                ('Pannel_Number', models.CharField(max_length=100)),
                ('Attendance_In_Eval_2', models.IntegerField()),
                ('Identification_of_problem_Domain', models.CharField(max_length=100)),
                ('Knowledge_Of_Problem_Domain', models.CharField(max_length=100)),
                ('Creativity_And_Originality_In_Problem', models.CharField(max_length=100)),
                ('Knowledge_Purpose_And_Resource', models.CharField(max_length=100)),
                ('Team_Size_As_Project_Size', models.IntegerField()),
                ('Project_Planning_And_Work_Distribution', models.CharField(max_length=100)),
                ('Oral_Communication', models.CharField(max_length=100)),
                ('Quality_Of_Written_Proposal', models.CharField(max_length=100)),
                ('Guide_Marks', models.IntegerField()),
                ('Quality_Of_Project_Title', models.CharField(max_length=100)),
                ('Total', models.IntegerField()),
                ('Remark', models.CharField(max_length=100)),
            ],
        ),
    ]