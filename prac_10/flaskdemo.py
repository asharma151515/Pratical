from flask import Flask, render_template, request, redirect, url_for, session
import wikipedia

app = Flask(__name__)
app.secret_key = 'YOUR_SECRET_KEY'  # Replace with a strong, randomly generated key

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search_term = request.form['search']
        session['search_term'] = search_term #Sanitize input here if needed
        return redirect(url_for('results', search_term=search_term))
    return render_template("search.html")

@app.route('/results/<search_term>')
def results(search_term):
    page = get_page(search_term)
    if page:
      return render_template("results.html", page=page)
    else:
      return render_template("results.html", error="Page not found.")

def get_page(search_term):
    try:
        page = wikipedia.page(search_term)
        return page
    except wikipedia.exceptions.PageError:
        return None
    except wikipedia.exceptions.DisambiguationError as e:
        return {'error': 'Disambiguation', 'options': e.options}
    except Exception as e:
        return {'error': f'An unexpected error occurred: {e}'}

if __name__ == '__main__':
    app.run(debug=True) #debug=True only for development