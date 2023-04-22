from flask import Flask, render_template, request, redirect, url_for
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    concert_venues = get_all_concert_venues()
    return render_template('index.html', concert_venues = concert_venues)

#everything with render use concert_templates

@app.route('/edit/<rowid>')
def edit(rowid):
    # concert_venues = get_concert_venues(rowid)
    concert_venues = concert_venues(rowid)
    return render_template('edit.html', concert_venues = concert_venues)
# get_venue - make functio   to delete or updat 

@app.route('/edit-concert_venues/<rowid>', methods=['POST'])
def edit_concert_venues(rowid):
    name = request.form['name']
    age = int(request.form['location']) 
    height = request.form['capacity']
    group = request.form['parking']
    update_venue(name, age, height, group, rowid)

    return redirect(url_for('index'))


@app.route('/', methods=['POST'])
def submit():
    name = request.form['name']
    location = request.form['location']
    capacity = int(request.form['capacity']) 
    parking = int(request.form['parking'])
    
    add_venue(name,location, capacity, parking)
    return redirect(url_for('index'))

@app.route('/delete-concert_venues/<rowid>')
def delete(rowid):
    delete_venue(rowid)
    return redirect(url_for('index'))

#wheres the url




def add_venue(name, location, capacity, parking):
    conn = sqlite3.connect('./static/data/venues.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO concert_venues(name, location, capacity, parking) VALUES (?, ?, ?, ?)", (location, capacity, parking, name))
    conn.commit()
    conn.close()

def update_venue(name, age, height, group, rowid):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("UPDATE engineers SET name = ?, age = ?, height = ?, group_num = ? WHERE rowid = ?", (name, age, height, group, rowid))
    conn.commit()
    conn.close()

def delete_venue(rowid):
    conn = sqlite3.connect('./static/data/team-edge.db')
    curs = conn.cursor()
    curs.execute("INSERT INTO concert_venues(name, location, capacity, parking) VALUES (?, ?, ?, ?)", (location, capacity, parking, name))
    conn.commit()
    conn.close()



def get_concert_venues():
    conn = sqlite3.connect('./static/data/venues.db')
    curs = conn.cursor()
    result = curs.execute("SELECT * FROM concert_venues")
    concert_venues = []

    for row in result: 
        venue = {
            'rowid': row[0],
            'name': row[1],
            'location': row[2],
            'capacity': row[3],
            'parking': row[4]

        }
        concert_venues.append(venue)

    conn.close()
    return concert_venues




def get_all_concert_venues():
    conn = sqlite3.connect('./static/data/venues.db')
    curs = conn.cursor()
    result = curs.execute("SELECT * FROM concert_venues")
    concert_venues = []

    for row in result: 
        venue = {
            'rowid': row[0],
            'name': row[1],
            'location': row[2],
            'capacity': row[3],
            'parking': row[3]

        }
        concert_venues.append(venue)

    conn.close()
    return concert_venues

if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')