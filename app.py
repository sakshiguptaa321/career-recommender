# app.py
from flask import Flask, render_template, request
import re

app = Flask(__name__)

career_db = [
    {
        "title": "Frontend Developer",
        "keywords": ["html", "css", "javascript", "react", "ui", "frontend"],
        "salary": "₹6–15 LPA",
        "companies": ["Flipkart", "Zomato", "CRED"],
        "roadmap": "https://roadmap.sh/frontend",
        "course": "https://www.youtube.com/watch?v=3JluqTojuME",
        "tools": ["VS Code", "Chrome DevTools", "Figma"],
        "article": {
            "overview": "Frontend developers bring websites and applications to life. They focus on what users see and interact with — everything from buttons, animations, and layout to accessibility and responsiveness.",
            "advantages": ["High demand across industries", "Creative and visual role", "Many freelancing opportunities"],
            "challenges": ["Requires constant learning (new frameworks)", "Design precision is essential", "Browser compatibility can be tricky"],
            "path": "Frontend Dev → UI Engineer → Lead Frontend → UX Architect"
        }
    },
    {
        "title": "Backend Developer",
        "keywords": ["python", "node", "api", "database", "sql", "flask", "django"],
        "salary": "₹8–18 LPA",
        "companies": ["Amazon", "Paytm", "Freshworks"],
        "roadmap": "https://roadmap.sh/backend",
        "course": "https://www.youtube.com/watch?v=ldYcgPKEZC8",
        "tools": ["Postman", "VS Code", "MongoDB Compass"],
        "article": {
            "overview": "Backend developers work on the server-side logic, databases, and APIs that power web and mobile apps. They make sure data flows securely and efficiently.",
            "advantages": ["Great problem-solving role", "High scalability & cloud integrations", "Strong demand across companies"],
            "challenges": ["Debugging production issues", "Managing databases and deployments", "Need for clean and optimized code"],
            "path": "Backend Dev → Full-Stack Dev → Tech Lead → Architect"
        }
    },
    {
        "title": "Data Scientist",
        "keywords": ["python", "ml", "data", "pandas", "numpy", "ai", "statistics"],
        "salary": "₹10–25 LPA",
        "companies": ["Google", "Swiggy", "TCS"],
        "roadmap": "https://roadmap.sh/data-science",
        "course": "https://www.youtube.com/watch?v=ua-CiDNNj30",
        "tools": ["Jupyter", "Scikit-learn", "TensorFlow"],
        "article": {
            "overview": "Data Scientists analyze vast amounts of data to find trends, build models, and generate insights. They combine programming with math and domain knowledge.",
            "advantages": ["High salaries and demand", "Works across domains", "Great for analytical thinkers"],
            "challenges": ["Data cleaning can take 80% of time", "Requires statistical foundation", "Model interpretability"],
            "path": "Data Analyst → Data Scientist → ML Engineer → AI Architect"
        }
    },
    {
        "title": "UI/UX Designer",
        "keywords": ["figma", "design", "prototype", "wireframe", "ux", "ui"],
        "salary": "₹5–12 LPA",
        "companies": ["Nykaa", "Byjus", "Razorpay"],
        "roadmap": "https://www.behance.net/search/projects?field=131",
        "course": "https://www.youtube.com/watch?v=3Y1dv4JgWKM",
        "tools": ["Figma", "Adobe XD", "Notion"],
        "article": {
            "overview": "UI/UX Designers craft user-friendly interfaces and experiences. They make sure apps look good and feel intuitive, often creating wireframes and testing usability.",
            "advantages": ["Visually creative field", "User-focused design thinking", "Growing demand in startups"],
            "challenges": ["Subjective feedback", "Balancing aesthetics vs functionality", "Requires constant user testing"],
            "path": "UI/UX Intern → Designer → Design Lead → Product Designer"
        }
    },
    {
        "title": "Cloud Engineer",
        "keywords": ["aws", "gcp", "azure", "cloud", "devops", "docker", "kubernetes"],
        "salary": "₹12–22 LPA",
        "companies": ["Microsoft", "Oracle", "Infosys"],
        "roadmap": "https://roadmap.sh/devops",
        "course": "https://www.youtube.com/watch?v=f2r5-b9z6zE",
        "tools": ["AWS CLI", "Terraform", "Docker"],
        "article": {
            "overview": "Cloud Engineers build and manage scalable infrastructure on platforms like AWS and Azure. They automate deployments and ensure app availability.",
            "advantages": ["High demand with cloud adoption", "Works across IT teams", "Well-paid roles"],
            "challenges": ["High responsibility in uptime", "Security and compliance", "Rapidly evolving tools"],
            "path": "Cloud Intern → DevOps Engineer → Cloud Architect"
        }
    },
    {
        "title": "Cybersecurity Analyst",
        "keywords": ["security", "firewall", "network", "malware", "ethical hacking"],
        "salary": "₹8–16 LPA",
        "companies": ["Cisco", "CheckPoint", "TCS"],
        "roadmap": "https://roadmap.sh/cyber-security",
        "course": "https://www.youtube.com/watch?v=inWWhr5tnEA",
        "tools": ["Wireshark", "Kali Linux", "Burp Suite"],
        "article": {
            "overview": "Cybersecurity Analysts defend systems from digital attacks. They monitor networks, analyze threats, and work on securing systems.",
            "advantages": ["Growing concern = high demand", "Impactful & ethical role", "Interesting challenges"],
            "challenges": ["Need for constant vigilance", "24x7 monitoring in some roles", "Requires certifications"],
            "path": "Security Analyst → SOC Engineer → Cybersecurity Manager"
        }
    },
    {
        "title": "Game Developer",
        "keywords": ["unity", "unreal", "c++", "game", "graphics", "3d", "design"],
        "salary": "₹6–12 LPA",
        "companies": ["Ubisoft", "Zynga", "Nazara"],
        "roadmap": "https://www.gamedev.net/resources",
        "course": "https://www.youtube.com/watch?v=gB1F9G0JXOo",
        "tools": ["Unity", "Unreal Engine", "Blender"],
        "article": {
            "overview": "Game Developers create interactive entertainment using engines like Unity or Unreal. They mix logic, creativity, and storytelling.",
            "advantages": ["Fun and innovative field", "Combines tech and creativity", "Growing in mobile & AR/VR"],
            "challenges": ["Highly competitive", "Crunch time in big releases", "Needs graphic performance skills"],
            "path": "Junior Dev → Game Programmer → Game Designer → Technical Director"
        }
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        input_text = request.form.get('skills')
    else:
        input_text = request.args.get('skills')

    if not input_text:
        return render_template("result.html", recommendations=[], input="")

    input_text = input_text.lower()
    input_keywords = [word.strip() for word in re.split(r'[\s,]+', input_text) if word.strip()]

    recommendations = []
    for career in career_db:
        matches = [kw for kw in input_keywords if kw in career["keywords"]]
        score = round((len(matches) / len(career["keywords"])) * 100, 1) if career["keywords"] else 0
        if score > 0:
            recommendations.append({
                **career,
                "score": score
            })

    recommendations.sort(key=lambda x: x["score"], reverse=True)
    return render_template("result.html", recommendations=recommendations, input=input_text)

if __name__ == '__main__':
    app.run(debug=True)



