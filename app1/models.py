from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=512)
    logo = models.ImageField(upload_to='app1/static/app1/images/company/', null=False)


class User(models.Model):  # AbstractEmailUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    company = models.ForeignKey(Company)
    picture = models.ImageField(upload_to='app1/static/app1/images/user/', null=False)
    phone = models.CharField(max_length=15)


class Test(models.Model):
    id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company)


class TestSectionDef(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    company = models.ForeignKey(Company)


class Question (models.Model):  # for mcq
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    difficulty_level = models.CharField(max_length=1, default='3')
    company = models.ForeignKey(Company, null=True) 


class TestSectionQuestions(models.Model):  # table where sections and questions get mapped to a test
    id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test)
    section = models.ForeignKey(TestSectionDef)
    duration = models.IntegerField(blank=True, null=True)
    questions = models.ManyToManyField(Question)  # list of questions that in under a section


class QuestionAnswer (models.Model):  # for mcq
    id = models.AutoField(primary_key=True)
    text = models.CharField(max_length=1024)
    question = models.ForeignKey(Question)


class TestCandidateQuestionHistory(models.Model):  # questions answered by the candidate
    question = models.ForeignKey(Question)
    candidate = models.ForeignKey(User)  # AUTH_USER_MODEL)
    test = models.ForeignKey(Test)
    answer = models.ForeignKey(QuestionAnswer, null=True)
    answer_dateTime = models.DateTimeField(null=True)
    section = models.ForeignKey(TestSectionDef)
    duration = models.SmallIntegerField(default=0)
    status = models.SmallIntegerField(default=0)  # 0 = wrong answer, 1 = right answer
    score = models.SmallIntegerField(default=0)   # 0 if wrong answer


class TestChatTranscripts(models.Model):  # transcripts for a particular question
    id = models.AutoField(primary_key=True)
    question = models.TextField()
    transcripts = models.TextField()
    candidate = models.ForeignKey(User ,null=False)


class TestParagraph(models.Model):  # paragraph for a particular section
    id = models.AutoField(primary_key=True)
    paragraph = models.TextField()
    question = models.ForeignKey(Question)
