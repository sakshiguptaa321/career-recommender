import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

# Sample extended data
data = pd.DataFrame({
    'career': [
        'Data Scientist',
        'Web Developer',
        'AI Researcher',
        'UI/UX Designer',
        'Cybersecurity Analyst'
    ],
    'skills': [
        'python statistics machine learning',
        'html css javascript react',
        'deep learning nlp reinforcement learning',
        'design thinking figma adobe xd',
        'network security encryption linux'
    ],
    'description': [
        'Analyze data to build predictive models and drive business decisions.',
        'Build and maintain websites and web applications using front-end and back-end tools.',
        'Conduct research and build new models in artificial intelligence and machine learning.',
        'Design user interfaces and experiences for digital products, ensuring usability and appeal.',
        'Protect systems from cyber threats through monitoring, detection, and response.'
    ],
    'opportunities': [
        'Companies: Google, Amazon, Swiggy, MuSigma | Roles: ML Engineer, Data Analyst',
        'Companies: TCS, Infosys, Freelancing | Roles: Frontend Developer, Full Stack Dev',
        'Companies: DeepMind, OpenAI, Microsoft Research | Roles: AI Scientist, NLP Engineer',
        'Companies: Adobe, Zoho, UIPath | Roles: UX Designer, Product Designer',
        'Companies: Palo Alto, Cisco, DRDO | Roles: Security Analyst, SOC Engineer'
    ]
})

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['skills'])
model = NearestNeighbors(n_neighbors=1, metric='cosine')
model.fit(X)

def recommend_career(interests, skill_level):
    input_text = interests + ' ' + skill_level
    input_vec = vectorizer.transform([input_text])
    dist, index = model.kneighbors(input_vec)
    match = data.iloc[index[0][0]]
    return {
        'career': match['career'],
        'description': match['description'],
        'skills': match['skills'],
        'opportunities': match['opportunities']
    }
