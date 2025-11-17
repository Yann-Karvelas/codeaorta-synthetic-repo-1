# Finding 4: SQL Injection Risk
@app.route('/user/<id>')
def get_user(id):
    query = f"SELECT * FROM users WHERE id = {id}"
    # ... execute query
