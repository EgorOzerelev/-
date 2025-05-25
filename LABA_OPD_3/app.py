from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        favorite_color = request.form.get('favorite_color')

        # Запись в файл
        with open('responses.txt', 'a', encoding='utf-8') as f:
            f.write(f'Имя: {name}, Возраст: {age}, Любимый цвет: {favorite_color}\n')

        return redirect('/thank_you')

    return render_template('form.html')

@app.route('/thank_you')
def thank_you():
    return '<h1>Спасибо за заполнение анкеты!</h1>'

if __name__ == '__main__':
    app.run(debug=True)