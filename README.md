# Career Recommender Website

An AI-powered Career Recommender Web App built using Flask, designed to help students and job seekers discover ideal career paths based on their skills, interests, and goals. The platform suggests suitable careers, provides detailed job descriptions, in-demand skills, related opportunities, and helpful visualizations.

## 🚀 Features

- **Career Recommendation** based on user input (skills, interests, or profile)
- **Detailed Job Descriptions** with advantages, disadvantages, and application advice
- **Smart Suggestions:** Autocomplete & sample input for user convenience
- **Visual Insights:** Radar charts, donut charts, and skill match indicators
- **Downloadable Reports:** Get your career suggestions as a professional PDF
- **Shareable Links:** Easily share your personalized career results
- **Responsive UI:** Clean and intuitive design using HTML, CSS, and Bootstrap/Tailwind

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript (Tailwind/Bootstrap optional)
- **Backend:** Python, Flask
- **AI/NLP:** scikit-learn, Pandas, Text preprocessing
- **Visualization:** Chart.js or Plotly
- **Deployment:** Vercel, Render, or Heroku

## 📂 Project Structure

```
career-recommender/
├── static/
│   ├── css/
│   └── js/
├── templates/
│   ├── index.html
│   └── recommend.html
├── app.py
├── requirements.txt
└── README.md
```

## 🧪 How to Run

1. **Clone the repo:**

   ```bash
   git clone https://github.com/sakshiguptaa321/career-recommender.git
   cd career-recommender
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask server:**

   ```bash
   python app.py
   ```

4. **Open your browser and go to:**
   http://127.0.0.1:5000

## 👩‍💻 Future Improvements

- Resume upload & parsing for automated suggestions
- User login system to save recommendations
- Admin panel to manage career data
- Integration with LinkedIn/Indeed APIs for live job feeds

## 🤝 Contributions

Pull requests are welcome! Feel free to suggest features, report bugs, or submit enhancements.
