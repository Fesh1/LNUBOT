import requests
from bs4 import BeautifulSoup
import bs4
from data.database import Employee, Faculty, session
from datetime import datetime
import pytz

Lviv_timezone = pytz.timezone('Europe/Minsk')
class LNU_parser:
    def __init__(self, info: list, method: str):
        self.info = info
        self.method = method
        self.html_file = html_worker(self.method, self.info).get_html()
        if self.html_file != b'<h1>Empty</h1>':
            self.html_file = BeautifulSoup(self.html_file, "html.parser")
            self.html_file = self.html_file.main


    def clean(self):
        if self.html_file != b'<h1>Empty</h1>':
            self.html_file.h1.name = 'b'
            title = self.html_file.b
            text = str(title) + '\n'
        else:
            print('clean started okay')
            text = 'Empty'
        if self.method == 'get_employee':
            for i in self.html_file.div('span'):

                for j in i.contents:
                    if isinstance(j, bs4.element.NavigableString):
                        text = text + str(j) + ' '

                    if j.name == "span":
                        text = text + str(j.contents[0]) + ' '

                    if j.name == "a":
                        text = text + str(j) + ' '

                if (i.name == "span") and i.attrs and (i.attrs['class'] == ['value']):
                    text = text + '\n '
            text = text.replace(': :', ':').replace('завідувач кафедри', 'завідувач')

        if self.method == 'get_article_by_id' or self.method == 'newsletter' and self.html_file != b'<h1>Empty</h1>':
            for i in self.html_file.p.contents:

                if i.name == "span":
                    text = text + str(i.contents[0]) + ' '

                if i.name == "a":
                    text = text + str(i) + ' '

        return text

    def img_extractor(self):

        imgs_url = []
        if self.method == 'get_article' or self.method == 'newsletter' and self.html_file != b'<h1>Empty</h1>':
            for i in self.html_file.find_all(lambda tag: tag.name == 'img'):
                imgs_url.append(i.attrs['src'])

        if self.method == 'get_employee':
            for i in self.html_file.find_all(lambda tag: tag.name == 'span' and (tag.get('class') == ['photo'])):
                url = i.attrs['style'].replace('background-image: url(', '')
                url = url.replace(');', '')
                imgs_url.append(url)
                del url
        return imgs_url


class html_worker:
    def __init__(self, method, info):
        self.method = method
        self.info = info

    def get_html(self):
        if self.method == 'get_article_by_id':

            id = int(float(self.info[1]))
            task_url = "/?p="
            fac = ''

            fac = faculty_getter(self.info[0])

            if fac == 'mmf':
                r = requests.get('http://new.{}.lnu.edu.ua{}{}'.format(fac, task_url, id))
            else:
                r = requests.get('https://{}.lnu.edu.ua{}{}'.format(fac, task_url, id))
            return r.content
        if self.method == 'newsletter':
            print('work', "html_get")
            faculty = self.info
            print('faculty in: ', faculty)
            if faculty == 'mmf':
                r2 = requests.get('http://new.{}.lnu.edu.ua/news'.format(faculty))
                print(r2)
            else:
                r2 = requests.get("https://{}.lnu.edu.ua/news".format(faculty))
                print('not mmf', r2)
            html2 = BeautifulSoup(r2.content, "html.parser")
            html2 = html2.main
            time_of_last_publication = html2.div.div.contents[0].replace('| ', '')
            time_of_last_publication = time_of_last_publication[0:10]
            print("time_of_last_publication", time_of_last_publication)
            datetime_Lviv = datetime.now(Lviv_timezone)
            print(datetime_Lviv.strftime("%d.%m.%Y"))
            if time_of_last_publication == datetime_Lviv.strftime("%d.%m.%Y"):
                news = html2.a.attrs['href']
                r = requests.get(news)
                return r.content
            else:
                return b'<h1>Empty</h1>'


        if self.method == 'get_employee':

            fac = faculty_getter(self.info[0])
            url = employee_getter(self.info[1], fac)

            task_url = "/employee"

            if fac == 'mmf':
                r = requests.get('http://new.{}.lnu.edu.ua{}/{}'.format(fac, task_url, url))
            else:
                r = requests.get('https://{}.lnu.edu.ua{}/{}'.format(fac, task_url, url))
            return r.content


def faculty_getter(info):
    return session.query(Faculty). \
        filter(Faculty.faculty_name.ilike('%' + info + '%')).first().faculty_url


def employee_getter(info, fac):
    return session.query(Employee). \
        filter(Employee.faculty_id == Faculty.faculty_id). \
        filter(Faculty.faculty_url == fac). \
        filter(Employee.name.ilike('%' + info + '%')).first().employee_url

