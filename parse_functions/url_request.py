import requests
from data.database import session
from data.database import Employee, Faculty
class html_worker:
    def __init__(self, method, info):
        self.method = method
        self.info = info

    def get_html(self):
        if self.method == 'get_article':
            name = '%' + self.info[0] + '%'
            id = '%' + self.info[1] + '%'
            task_url = "/wp-json/wp/v2/posts"
            url = ''
            try:
                url = session.query(Faculty).filter(Faculty.faculty_name.ilike(name))
            except:
                print('WRONG!!!')
            r = requests.get('https://{}.lnu.edu.ua{}/{}'.format(url, task_url, id))
            return 1
        if self.method == 'get_employee':
            name = '%' + self.info[1] + '%'
            fac = '%' +self.info[0] + '%'
            url = ''
            try:
                url = session.query(Employee).filter(Employee.faculty_id == Faculty.faculty_id).filter(
                    Faculty.faculty_name.ilike(fac)).filter(Employee.name.ilike(name)).all()[0].employee_url
            except:
                print('Wrong request')

            task_url = "/employee"
            r = requests.get('https://{}.lnu.edu.ua{}/{}'.format(fac, task_url, url))
            return r