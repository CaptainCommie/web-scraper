from bs4 import BeautifulSoup
import requests
import json
#get the raw html file
html_text = requests.get("https://www.theguardian.com/education/ng-interactive/2021/sep/11/the-best-uk-universities-2022-rankings").text

#converts the raw html file using html parser
content = BeautifulSoup(html_text, "html.parser")
#finds the course rows
#course_rows = content.find_all('tr', class_="c-table__row")

#finds the course table
course_table_body = content.find("tbody")

rank_2022_list = course_table_body.find_all("td", class_="c-table__data c-table__data--1 c-table__data--rank2022 u-text-align-right")
#for i in rank_2022_list:

rank_2021_list = course_table_body.find_all("td", class_="c-table__data c-table__data--2 c-table__data--rank2021 u-text-align-right")
#for i in rank_2021_list:

name_list = course_table_body.find_all("td", class_="c-table__data c-table__data--3 c-table__data--name")
#for i in name_list:

guardian_score_list = course_table_body.find_all("td", class_="c-table__data c-table__data--4 c-table__data--guardianScore u-text-align-right u-relative-mobile")
#for i in guardian_score_list:

course_satisfaction_list = course_table_body.find_all("td", class_="c-table__data c-table__data--5 c-table__data--percentSatisfiedOverall u-text-align-right")
#for i in course_satisfaction_list:

#finds the course satisfaction using the course rows
course_satisfaction_list = course_table_body.find_all("td", class_="c-table__data c-table__data--5 c-table__data--percentSatisfiedOverall u-text-align-right")
#for i in course_satisfaction_list:


teaching_satisfaction_list = course_table_body.find_all("td", class_="c-table__data c-table__data--6 c-table__data--percentSatisfiedWithTeaching u-text-align-right")
#for i in teaching_satisfaction_list:

feedback_satisfaction_list = course_table_body.find_all("td", class_="c-table__data c-table__data--7 c-table__data--percentSatisfiedWithAssessment u-text-align-right")
#for i in feedback_satisfaction_list:

student_staff_ratio_list = course_table_body.find_all("td", class_="c-table__data c-table__data--8 c-table__data--studentStaffRatio u-text-align-right")
#for i in student_staff_ratio_list:

spend_per_student_list = course_table_body.find_all("td", class_="c-table__data c-table__data--9 c-table__data--expenditurePerStudent u-text-align-right")
#for i in spend_per_student_list:

average_entry_tariff_list = course_table_body.find_all("td", class_="c-table__data c-table__data--10 c-table__data--averageEntryTariff u-text-align-right")
#for i in average_entry_tariff_list:

#compares degree results with entry requirements to show how effectively they are taught
value_added_score_list = course_table_body.find_all("td", class_="c-table__data c-table__data--11 c-table__data--valueAdded u-text-align-right")
#for i in value_added_score_list:

career_prospects_list = course_table_body.find_all("td", class_="c-table__data c-table__data--12 c-table__data--careerProspects u-text-align-right")
#for i in career_prospects_list:

continuation_list = course_table_body.find_all("td", class_="c-table__data c-table__data--13 c-table__data--continuation u-text-align-right")
#for i in continuation_list:

with open("json.json") as f:
    data = json.load(f)
    universities = data["universities"]
    print(universities[0])

with open("json.json") as f:
    data = json.load(f)
    universities = data["universities"]
    for i in rank_2022_list:
        universities.add()





