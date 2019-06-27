from flask import Flask,request , render_template
from cl import predik
app = Flask(__name__)

@app.route("/")
def home():
        return render_template('index.html')

@app.route("/pred", methods=['POST'])
def prediksi():
    if request.method == 'POST':
        hamil = request.form['hamil']
        gula_darah = request.form['gula_darah']
        tekanan_darah = request.form['tekanan_darah']
        tbl_kulit = request.form['tebal_kulit']
        insulin = request.form['insulin']
        berat = request.form['berat']
        silsilah = request.form['silsilah']
        umur = request.form['umur']
        hasil = predik(hamil,gula_darah,tekanan_darah,tbl_kulit,insulin,berat,silsilah,umur)
        if (hasil== 1):
            output= "anda positif diabetes"
        else :
            output= "anda negatif diabetes"
        return render_template('index.html', hasil=output)

if __name__ == '__main__':
    app.run(debug=True) 