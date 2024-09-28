from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    personal_info = {
        "name": "Puneet Bajaj",
        "phone": "(408) 326-9383",
        "email": "puneet.bajaj@sjsu.edu",
        "location": "San Jose, CA",
        "linkedin": "https://linkedin.com/in/puneet-bajaj-",
        "github": "https://github.com/pb2323"
    }
    about_me = "A motivated Software Engineer with expertise in developing scalable solutions and optimizing performance across various platforms. Adept at leveraging frameworks like React, Next.js, and Ruby on Rails to deliver high-quality user experiences."
    skills = {
        "languages": ["Ruby", "JavaScript", "C", "C++", "TypeScript", "Java", "Python", "HTML", "CSS", "Bash", "Solidity"],
        "frameworks": ["Ruby on Rails", "React.js", "Next.js", "Node.js", "Express.js", "Redux", "Flask", "Django", "Socket.IO", "Web3.js"],
        "tools": ["Git", "GitHub", "AWS S3", "REST APIs", "GraphQL", "Docker", "Kubernetes", "AWS Lambda", "Elasticsearch"],
        "databases": ["MySQL", "MongoDB", "PostgreSQL", "Redis"],
        "os": ["Linux", "Unix"]
    }
    projects = [
        {
            "name": "Network-In: Social Networking Platform for Freelancers",
            "description": "A platform that enables users to create smart contracts on the Polygon blockchain, ensuring stake-based security. Includes functionalities for sharing, chat, audio, and video calls, with image storage in IPFS.",
            "technologies": ["Next.js", "Node.js", "Express.js", "Solidity", "MongoDB", "Socket.IO", "Web3.js", "IPFS"],
            "github": "https://github.com/pb2323/Social_Media_App",
            "website": "https://network-in-25db1b54cfae.herokuapp.com/"
        }
    ]
    experience = [
        {
            "title": "Software Engineer",
            "company": "BrowserStack",
            "duration": "Jan 2022 – Jul 2024",
            "details": [
                "Researched and developed support for Cucumber, boosting product adoption by 8% YoY.",
                "Engineered a video recording app, improving video log stability from 30% to 99% and reducing S3 costs by 7%.",
                "Integrated Detox testing framework, resolving a deal blocker worth $1.3 million."
            ]
        },
        {
            "title": "Full Stack Developer Intern",
            "company": "SkoolOfCode",
            "duration": "Oct 2021 – Jan 2022",
            "details": [
                "Upgraded Next.js from v7 to v14 with zero downtime, improving Lighthouse score by 25%.",
                "Enhanced SEO, resulting in a 92% YoY increase in website traffic and improved Google ranking."
            ]
        },
        {
            "title": "Frontend Developer Intern",
            "company": "Namasys Analytics",
            "duration": "Jun 2021 – Aug 2021",
            "details": [
                "Developed SACRD, a web application for chartered accountants, streamlining daily workflows."
            ]
        },
        {
            "title": "Frontend Developer Intern",
            "company": "Odiware Technologies",
            "duration": "Nov 2020 – Feb 2021",
            "details": [
                "Created dashboards for quizzes and assignments, increasing test coverage by 30%."
            ]
        }
    ]
    education = [
        {
            "degree": "Master of Science in Computer Software Engineering",
            "institution": "San Jose State University",
            "graduation": "May 2026"
        },
        {
            "degree": "Bachelor of Technology in Computer Engineering",
            "institution": "International Institute of Information Technology, Bhubaneswar, India",
            "graduation": "May 2022",
            "cgpa": "3.78/4.00"
        }
    ]
    volunteer = [
        {
            "role": "SKY Campus Happiness Program",
            "duration": "Aug 2022 – Present",
            "details": "Coordinated mental well-being workshops and organized blood donation camps for students."
        }
    ]
    return render_template('index.html', personal_info=personal_info, about_me=about_me, skills=skills, projects=projects, experience=experience, education=education, volunteer=volunteer)

if __name__ == '__main__':
    app.run(debug=True)