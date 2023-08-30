##  اسامة محمد صالح الهرش

from ast import Attribute


class Experience:
    ## function some the Attributes
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date
   ## This function do view experience
    def display_experience(self):
        print("Company:", self.company)
        print("Job Title:", self.job_title)
        print("Employment Period:", self.start_date, "to", self.end_date)


class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date
       ## This function do view education
    def display_education(self):
        print("Degree:", self.degree)
        print("Institution:", self.institution)
        print("Completion Date:", self.completion_date)


class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage
        ## This function do view skill
    def display_skill(self):
        print("Skill:", self.skill)
        print("Proficiency Level:", self.percentage)


class CV:
    def __init__(self):
        self.experiences = []
        self.education = []
        self.skills = []
        ## This function do added  add_experience
    def add_experience(self):
        company = input("Enter the company name: ")
        job_title = input("Enter the job title: ")
        start_date = input("Enter the start date: ")
        end_date = input("Enter the end date: ")
        
        experience = Experience(company, job_title, start_date, end_date)
        self.experiences.append(experience)
        
        add_more = input("Do you want to add another experience? (yes/no): ")
        if add_more.lower() == "yes":
            self.add_experience()
            ## This function do added  add_education
    def add_education(self):
        degree = input("Enter the degree: ")
        institution = input("Enter the institution: ")
        completion_date = input("Enter the completion date: ")
        
        education = Education(degree, institution, completion_date)
        self.education.append(education)
        
        add_more = input("Do you want to add another education? (yes/no): ")
        if add_more.lower() == "yes":
            self.add_education()
     ## This function do added  add_skill
    def add_skill(self):
        skill = input("Enter the skill: ")
        percentage = input("Enter the proficiency level: ")
        
        skill = Skill(skill, percentage)
        self.skills.append(skill)
        
        add_more = input("Do you want to add another skill? (yes/no): ")
        if add_more.lower() == "yes":
            self.add_skill()
    ## This function do view cv
    def display_cv(self):
        print("--- Curriculum Vitae ---")
        print("Name:", self.name)
        print("\nExperiences:")
        for experience in self.experiences:
            experience.display_experience()
            print()
        
        print("\nEducation:")
        for education in self.education:
            education.display_education()
            print()
        
        print("\nSkills:")
        for skill in self.skills:
            skill.display_skill()
            print()
    ## This function do create  cv
    def create_cv(self):
        self.name = input("Enter your name: ")
        
        add_skills = input("Do you want to add skills? (yes/no): ")
        if add_skills.lower() == "yes":
            self.add_skill()
        
        self.add_education()
        self.add_experience()
        
        self.display_cv()

## call the CV
cv = CV()
cv.create_cv()