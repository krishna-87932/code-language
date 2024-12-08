from flask import Flask, render_template, request, session
import Secrete_code

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for session to work
obj1 = Secrete_code.Encode()
obj2 = Secrete_code.Decode()
def All_clear():
    obj2.input_string = ""
    obj1.temp_code.clear()
    obj1.temp_text.clear()
    obj2.secondary.clear()
    obj2.result_list.clear()
    obj2.final_list.clear()
    
@app.route('/', methods=['GET', 'POST'])
def index():
    
    output = obj1.main()
    if request.method == 'POST':
        All_clear()
        input_string = request.form.get('String', '')
        input_code = request.form.get('Codes', "")
        obj1.text = input_string
        obj2.input_string = input_code
        user_string = obj1.main()
        user_code = obj2.main()
        output = {
            "string":user_string,
            "codes" : user_code
        }
        
    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
