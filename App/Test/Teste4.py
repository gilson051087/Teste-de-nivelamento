from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("operadoras.csv")


@app.route('/buscar', methods=['GET'])
def buscar():

    query = request.args.get('q')
    
    if query:
        resultado = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)]
        
        return jsonify(resultado.to_dict(orient='records'))
    
    else:
        
        return jsonify({'erro': 'sem consulta'}), 400

if __name__ == '__main__':
    app.run(debug=True)
