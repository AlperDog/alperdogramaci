from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Session kullanabilmek için gerekli

# Highscore'ı saklamak için global değişken
highscore = 0

@app.route('/')
def index():
    return render_template('index.html', highscore=highscore)

@app.route('/quiz')
def quiz():
    questions = [
        {"question": "Python'da Yapay Zeka (AI) geliştirmek kolay öğrenilebilir mi?", "options": ["Evet", "Hayır"], "answer": "Evet"},
        {"question": "Bilgisayar görüşü, bir bilgisayarın görsel bilgileri anlamasını sağlar mı?", "options": ["Evet", "Hayır"], "answer": "Evet"},
        {"question": "NLP (Nöro-dilbilim) metinleri anlamak ve analiz etmek için kullanılan bir teknolojidir, doğru mu?", "options": ["Evet", "Hayır"], "answer": "Evet"},
        {"question": "Python, AI modellerini uygulamak için yaygın olarak kullanılan bir programlama dilidir, doğru mu?", "options": ["Evet", "Hayır"], "answer": "Evet"}
    ]
    return render_template('quiz.html', questions=questions, highscore=highscore)

@app.route('/submit', methods=['POST'])
def submit_quiz():
    global highscore
    questions = [
        {"question": "Python'da Yapay Zeka (AI) geliştirmek kolay öğrenilebilir mi?", "options": ["Evet", "Hayır"], "answer": "Evet"},
        {"question": "Bilgisayar görüşü, bir bilgisayarın görsel bilgileri anlamasını sağlar mı?", "options": ["Evet", "Hayır"], "answer": "Evet"},
        {"question": "NLP (Nöro-dilbilim) metinleri anlamak ve analiz etmek için kullanılan bir teknolojidir, doğru mu?", "options": ["Evet", "Hayır"], "answer": "Evet"},
        {"question": "Python, AI modellerini uygulamak için yaygın olarak kullanılan bir programlama dilidir, doğru mu?", "options": ["Evet", "Hayır"], "answer": "Evet"}
    ]
    correct = 0
    total = len(questions)
    answers = request.form

    for i, question in enumerate(questions):
        if answers.get(f"question-{i}") == question["answer"]:
            correct += 1

    wrong = total - correct
    if correct > highscore:
        highscore = correct

    return render_template('result.html', correct=correct, wrong=wrong, total=total, highscore=highscore)

if __name__ == "__main__":
    app.run(debug=True)
