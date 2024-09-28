import unittest
from app import app

class PortfolioAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Puneet Bajaj', response.data)
        self.assertIn(b'San Jose, CA', response.data)
        self.assertIn(b'puneet.bajaj@sjsu.edu', response.data)
        self.assertIn(b'(408) 326-9383', response.data)
        self.assertIn(b'linkedin.com/in/puneet-bajaj-', response.data)
        self.assertIn(b'github.com/pb2323', response.data)

    def test_about_me_section(self):
        response = self.app.get('/')
        self.assertIn(b'About Me', response.data)
        self.assertIn(b'A motivated Software Engineer with expertise in developing scalable solutions', response.data)

    def test_skills_section(self):
        response = self.app.get('/')
        self.assertIn(b'Skills', response.data)
        self.assertIn(b'Languages', response.data)
        self.assertIn(b'Ruby', response.data)
        self.assertIn(b'JavaScript', response.data)
        self.assertIn(b'Frameworks', response.data)
        self.assertIn(b'React.js', response.data)
        self.assertIn(b'Tools/Paradigms', response.data)
        self.assertIn(b'Docker', response.data)
        self.assertIn(b'Databases/OS', response.data)
        self.assertIn(b'MySQL', response.data)

    def test_projects_section(self):
        response = self.app.get('/')
        self.assertIn(b'Projects', response.data)
        self.assertIn(b'Network-In: Social Networking Platform for Freelancers', response.data)
        self.assertIn(b'A platform that enables users to create smart contracts on the Polygon blockchain', response.data)
        self.assertIn(b'Next.js', response.data)
        self.assertIn(b'Node.js', response.data)

    def test_experience_section(self):
        response = self.app.get('/')
        self.assertIn(b'Experience', response.data)
        self.assertIn(b'Software Engineer | BrowserStack', response.data)
        self.assertIn(b'Full Stack Developer Intern | SkoolOfCode', response.data)
        self.assertIn(b'Frontend Developer Intern | Namasys Analytics', response.data)
        self.assertIn(b'Frontend Developer Intern | Odiware Technologies', response.data)

    def test_education_section(self):
        response = self.app.get('/')
        self.assertIn(b'Education', response.data)
        self.assertIn(b'Master of Science in Computer Software Engineering', response.data)
        self.assertIn(b'San Jose State University', response.data)
        self.assertIn(b'Bachelor of Technology in Computer Engineering', response.data)
        self.assertIn(b'International Institute of Information Technology, Bhubaneswar, India', response.data)

    def test_volunteer_section(self):
        response = self.app.get('/')
        self.assertIn(b'Volunteer Experience', response.data)
        self.assertIn(b'SKY Campus Happiness Program', response.data)
        self.assertIn(b'Coordinated mental well-being workshops and organized blood donation camps for students', response.data)

if __name__ == '__main__':
    unittest.main(verbosity=2)