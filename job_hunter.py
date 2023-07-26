import openai 
from dataclasses import dataclass , field 
import typing as T

@dataclass 
class Section:
    pass 

@dataclass
class SkillCategory:
    name_category : str 
    examples : T.List[str] = field(default_factory=lambda : [])

    def add_examples(self) -> None:
        choice = input('Example of skill: ')

        while choice.lower() != 'no':
            self.examples.append(choice)
            choice = input('Example of skill: (type no to stop) ')

    def __repr__(self) -> str:
        output = '' 
        output += f"{self.name_category}: "
        output += ', '.join(self.examples)
        return output 

@dataclass 
class Skills(Section):
    list_categories : T.List[SkillCategory] = field(default_factory=lambda : [])

    def add_skills(self) -> None:
        choice = input('Name of the skills category: ')

        while choice.lower() != 'no':
            skills = SkillCategory(name_category=choice)
            skills.add_examples()
            self.list_categories.append(skills)
            choice = input('Name of the next skills category: (type no to stop) ')

    def __repr__(self) -> str:
        output = '\t\t\tRELEVANT SKILLS\n'
        for skill in self.list_categories:
            output += skill.__repr__()
            output += '\n'
        output += '\n'
        return output

@dataclass 
class School:
    name : str # name of school author went to 
    month : str # month the author graduated 
    year : int # year the author graduated 
    degree : str # BA/BS/MS/MA/PhD?
    major : str # name of the degree 

    def __repr__(self) -> str:
        return f"{self.degree} in {self.major}, {self.name}\t\t{self.month} {self.year}"

@dataclass
class Education(Section):
    list_schools : T.List[School] = field(default_factory=lambda : [])

    def add_schools(self) -> None:
        choice = input('Would you like to add one more university\'s name? Enter the name to start with: ')

        while choice.lower() != 'no':
            month = input('Month of graduation: ')
            year = int(input('Year of graduation: '))
            degree = input('Type of degree: ')
            major = input('Name of the major: ')

            school = School(name=choice, month=month, year=year, degree=degree, major=major)
            self.list_schools.append(school)

            choice = input('Would you like to add one more university\'s name? (type no to stop) ')
    
    def __repr__(self) -> str:
        output = '\t\t\tEDUCATION\n' 
        for school in self.list_schools:
            output += school.__repr__()
            output += '\n'
        return output 

@dataclass 
class Company:
    company_name : str # name of company author worked at 
    role : str 
    location : str 
    start_date : str 
    end_date : str
    outcomes : T.List[str] = field(default_factory=lambda : []) # list of bullet points done at work 

    def add_outcomes(self) -> None:
        choice = input('Would you like to add an accomplishment? ')

        while choice.lower() != 'no':
            self.outcomes.append(choice)
            choice = input('Would you like to add an accomplishment? (type no to end) ')
    
    def __repr__(self) -> str:
        output = '' 
        output += f"{self.role}, {self.location}\t\t\t{self.start_date}-{self.end_date}\n" 
        output += f"{self.company_name}\n"
        for outcome in self.outcomes:
            output += f"- {outcome}\n"
        return output 

@dataclass 
class ProfessionalExperiences(Section):
    list_positions : T.List[Company] = field(default_factory=lambda : [])

    def add_works(self) -> None:
        choice = input('Would you like to add a company/line of work? ')

        while choice.lower() != 'no':
            role = input('Title of the role: ')
            location = input('Location of the company: ')
            start_date = input('Start date of the work (like "Jun 2022")')
            end_date = input('End date of the work (leave blank if current role)')

            work = Company(company_name=choice, role=role, location=location, start_date=start_date, end_date=end_date)
            work.add_outcomes()
            self.list_positions.append(work)

            choice = input('Would you like to add one more company/line of work? ')
    
    def __repr__(self) -> str:
        output = '\t\t\tPROFESSIONAL EXPERIENCE\n' 
        for pos in self.list_positions:
            output += pos.__repr__()
            output += '\n'
        return output 

@dataclass 
class Project:
    title : str 
    outcomes : T.List[str] = field(default_factory=lambda : [])

    def add_outcomes(self) -> None:
        choice = input('Would you like to add more accomplishments? ')

        while choice.lower() != 'no':
            self.outcomes.append(choice)
            choice = input('Would you like to add more accomplishments? (type no to quit) ')
    
    def __repr__(self) -> str:
        output = f'{self.title}\n' 
        for outcome in self.outcomes:
            output += f"- {outcome}\n"
        return output

@dataclass 
class Projects(Section):
    list_projects : T.List[Project] = field(default_factory=lambda : [])

    def add_projects(self) -> None:
        choice = input('Would you like to add a project? Add it\'s title: ')

        while choice != 'no':
            proj = Project(title=choice)
            proj.add_outcomes()
            self.list_projects.append(proj)

            choice = input('Would you like to add one more project? Add it\'s title or say no to quit: ')
    
    def __repr__(self) -> str:
        output = '\t\t\tRELEVANT PROJECTS\n' 
        for project in self.list_projects:
            output += project.__repr__()
            output += '\n'
        return output 
        

@dataclass
class Resume:
    name : str = field(default_factory=lambda : '') # author name 
    phone_number : str = field(default_factory=lambda : '') # author telephone number 
    email : str = field(default_factory=lambda : '') # author's email address 
    github_profile : str = field(default_factory=lambda : '') # link to the github profile
    linkedin_profile : str = field(default_factory=lambda : '') # link to linkedin profile 
    location : str = field(default_factory=lambda : '') # location of the author  
    sections : T.List[Section] = field(default_factory=lambda : []) # list of the different sections 

    def __repr__(self) -> str:
        output = ''
        output += f"\t\t\t{self.name}\n"
        output += f"{self.email} | {self.phone_number} | {self.linkedin_profile} | {self.github_profile} | {self.location}"
        output += '\n\n'

        for section in self.sections:
            output += section.__repr__()
        
        return output 
    
    def get_personal_info(self) -> None:
        self.name = input('What is your name? ')
        self.phone_number = input('What is your phone number? ')
        self.email = input('What is your email? ')
        self.github_profile = input('What is your GitHub username? ')
        self.linkedin_profile = input('What is the link to your LinkedIn profile? ')
        self.location = input('Where are you located? ')

    def add_section(self) -> None:
        msg = f"""Type of sections available:
1. Education
2. Professional experiences
3. Relevant Skills
4. Relevant Projects
(use any other number to quit)
Enter the number that works best for you:\n"""
        choice = int(input(msg))
        section = None 

        while 0 < choice < 5:
            if choice == 1:
                section = Education()
                section.add_schools()
            elif choice == 2:
                section = ProfessionalExperiences()
                section.add_works()
            elif choice == 3:
                section = Skills()
                section.add_skills()
            else:
                section = Projects()
                section.add_projects()
            
            if section is None:
                raise Exception('Something weird is happening...')
            self.sections.append(section)
            choice = int(input(msg))



if __name__ == '__main__':
    # skill = SkillCategory(name_category='Programming')
    # skill.add_examples()
    # print()
    # print()
    # print(skill)

    # skills_section = Skills()
    # skills_section.add_skills()
    # print()
    # print()
    # print(skills_section)


    # school = School(name='stanford', month='june', year=2022, degree='MS', major='Computational and Mathematical Engineering')
    # print(school)

    # education = Education()
    # education.add_schools()
    # print(education)



    # company = Company(company_name='ezoic', role='data scientist', location='san diego, ca', start_date='Sept 2022', end_date='July 2023')
    # company.add_outcomes()
    # print(company)
    
    # work_xp = ProfessionalExperiences()
    # work_xp.add_works()
    # print(work_xp)


    # project = Project(title='COVID-19 analysis')
    # project.add_outcomes()
    # print(project)

    # projects = Projects()
    # projects.add_projects()
    # print(projects)

    resume = Resume()
    resume.get_personal_info()
    resume.add_section()
    print(resume)


    pass 