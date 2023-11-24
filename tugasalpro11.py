from flask import Flask, request, jsonify, render_template
import random

app = Flask(__name__, template_folder="template11")

pesan_acak = [
    "Makan patty itu spongebob",
    "Berdansalah, Patrick",
    "Gary, janganlah malas!"
    "Mr. Krabs selalu menjaga uangnya.",
    "Sandy suka olahraga ekstrem.",
    "Plankton sering kali kehilangan rencananya.",
    "Gary suka memenangkan perlombaan siput.",
    "Bikini Bottom penuh petualangan.",
    "Krusty Krab terkenal dengan Krabby Patty-nya.",
    "Squidward bermimpi menjadi seniman terkenal.",
]

def pesan_acak_get(name=None):
    if name:
        return f"{name}, {random.choice(pesan_acak)}"
    else:
        return random.choice(pesan_acak)

@app.route('/puja-kerang-ajaib', methods=['GET'])
def get_random_message_endpoint():
    name = request.args.get('nama')
    message = pesan_acak_get(name)
    return jsonify({'Pesan untukmu': message})

@app.route('/puja-kerang-ajaib/welcome', methods=['POST'])
def welcome_user():
    name = request.form.get('nama')
    if name:
        welcome_message = f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
        return jsonify({'Pesan untukmu': welcome_message})
    else:
        return jsonify({'error': 'Siapa namamu?'}), 400
    
@app.route('/formpost', methods=['GET'])
def formulir_test():
    return render_template('form_post.html')


#if __name__ == '__main__':
    #app.run(debug=True)
