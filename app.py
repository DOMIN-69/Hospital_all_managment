from flask import Flask, render_template, request, redirect, url_for, session, flash
from config import get_db_connection

app = Flask(__name__)
app.secret_key = 'super_secret_admin_key_change_this'

# ==========================================
# GLOBALLY HOSPITAL NAME FETCH KARNE KE LIYE
# ==========================================
@app.context_processor
def inject_hospital_name():
    hospital_name = "Hospital Management System"
    try:
        db = get_db_connection()
        if db:
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT hospital_name FROM settings WHERE id = 1")
            res = cursor.fetchone()
            if res:
                hospital_name = res['hospital_name']
            cursor.close()
            db.close()
    except:
        pass
    return dict(hospital_name=hospital_name)


# ==========================================
# 1. ADMIN LOGIN ROUTE
# ==========================================
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))

    if request.method == 'POST':
        try:
            username = request.form['username'].strip()
            password = request.form['password'].strip()

            db = get_db_connection()
            if db:
                cursor = db.cursor(dictionary=True)
                query = "SELECT * FROM users WHERE username = %s AND password = %s"
                cursor.execute(query, (username, password))
                user = cursor.fetchone()
                cursor.close()
                db.close()

                if user:
                    session['logged_in'] = True
                    session['username'] = user['username']
                    flash('Welcome back, Admin!', 'success')
                    return redirect(url_for('dashboard'))
                else:
                    flash('Invalid Username or Password', 'danger')
            else:
                flash('Database connection failed!', 'danger')
        except Exception as e:
            flash(f'Login Error: {str(e)}', 'danger')

    return render_template('login.html')


# ==========================================
# 2. DASHBOARD ROUTE
# ==========================================
@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    counts = {'patients': 0, 'doctors': 0, 'appointments': 0}
    try:
        db = get_db_connection()
        if db:
            cursor = db.cursor()
            cursor.execute("SELECT COUNT(*) FROM patients")
            counts['patients'] = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM doctors")
            counts['doctors'] = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM appointments")
            counts['appointments'] = cursor.fetchone()[0]
            cursor.close()
            db.close()
    except Exception as e:
        print(f"Dashboard count error: {e}")

    return render_template('dashboard.html', counts=counts)


# ==========================================
# 3. PATIENTS ROUTE (CRUD - Full)
# ==========================================
@app.route('/patients', methods=['GET', 'POST'])
def patients():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    db = get_db_connection()
    if not db:
        flash('Database connection failed!', 'danger')
        return render_template('patients.html', patients=[])

    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        try:
            name = request.form['name'].strip()
            age = request.form['age'].strip()
            gender = request.form['gender']
            phone = request.form['phone'].strip()
            emergency_contact = request.form['emergency_contact'].strip()
            disease = request.form['disease'].strip()

            # Mandatory fields server-side validation
            if not phone or not emergency_contact or not name:
                flash('Name, Contact Info, and Emergency Contact are strictly mandatory!', 'danger')
                return redirect(url_for('patients'))

            query = "INSERT INTO patients (name, age, gender, phone, emergency_contact, disease) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (name, age, gender, phone, emergency_contact, disease))
            db.commit()
            flash('Patient added successfully with contact verifications!', 'success')
        except Exception as e:
            db.rollback()
            flash(f'Error adding patient: ({str(e)})', 'danger')
        finally:
            return redirect(url_for('patients'))

    search_query = request.args.get('search', '')
    try:
        if search_query:
            query = "SELECT * FROM patients WHERE name LIKE %s OR disease LIKE %s"
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%"))
        else:
            cursor.execute("SELECT * FROM patients")
        patients_list = cursor.fetchall()
    except Exception as e:
        patients_list = []
        flash(f'Failed to fetch patients list: {str(e)}', 'danger')
    finally:
        cursor.close()
        db.close()
    
    return render_template('patients.html', patients=patients_list, search_query=search_query)


# EDIT PATIENT ROUTE
@app.route('/edit_patient/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
        
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        try:
            name = request.form['name'].strip()
            age = request.form['age'].strip()
            gender = request.form['gender']
            phone = request.form['phone'].strip()
            emergency_contact = request.form['emergency_contact'].strip()
            disease = request.form['disease'].strip()

            if not phone or not emergency_contact:
                flash('Contact Info and Emergency Contact cannot be empty!', 'danger')
                return redirect(url_for('edit_patient', id=id))

            query = """UPDATE patients 
                       SET name=%s, age=%s, gender=%s, phone=%s, emergency_contact=%s, disease=%s 
                       WHERE id=%s"""
            cursor.execute(query, (name, age, gender, phone, emergency_contact, disease, id))
            db.commit()
            flash('Patient details updated successfully!', 'success')
            return redirect(url_for('patients'))
        except Exception as e:
            db.rollback()
            flash(f'Update failed: {str(e)}', 'danger')
            return redirect(url_for('patients'))

    cursor.execute("SELECT * FROM patients WHERE id = %s", (id,))
    patient = cursor.fetchone()
    cursor.close()
    db.close()
    return render_template('edit_patient.html', patient=patient)


# ==========================================
# 4. DOCTORS ROUTE
# ==========================================
@app.route('/doctors', methods=['GET', 'POST'])
def doctors():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        try:
            name = request.form['name']
            specialization = request.form['specialization']
            phone = request.form['phone']

            query = "INSERT INTO doctors (name, specialization, phone) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, specialization, phone))
            db.commit()
            flash('Doctor added successfully!', 'success')
        except Exception as e:
            db.rollback()
            flash(f'Error adding doctor: {str(e)}', 'danger')
        finally:
            return redirect(url_for('doctors'))

    cursor.execute("SELECT * FROM doctors")
    doctors_list = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('doctors.html', doctors=doctors_list)


# ==========================================
# 5. APPOINTMENTS ROUTE
# ==========================================
@app.route('/appointments', methods=['GET', 'POST'])
def appointments():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        try:
            patient_name = request.form['patient_name']
            doctor_name = request.form['doctor_name']
            app_date = request.form['app_date']
            status = request.form['status']

            query = "INSERT INTO appointments (patient_name, doctor_name, app_date, status) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (patient_name, doctor_name, app_date, status))
            db.commit()
            flash('Appointment scheduled successfully!', 'success')
        except Exception as e:
            db.rollback()
            flash(f'Error scheduling appointment: {str(e)}', 'danger')
        finally:
            return redirect(url_for('appointments'))

    cursor.execute("SELECT * FROM appointments")
    appointments_list = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template('appointments.html', appointments=appointments_list)


# ==========================================
# 6. MASTER SETTINGS ROUTE (Pure Text Control)
# ==========================================
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        action_type = request.form.get('action_type')
        try:
            if action_type == 'change_hospital':
                new_h_name = request.form['hospital_name']
                cursor.execute("UPDATE settings SET hospital_name = %s WHERE id = 1", (new_h_name,))
                db.commit()
                flash('Hospital Name updated successfully!', 'success')
            
            elif action_type == 'change_username':
                new_username = request.form['new_username'].strip()
                if new_username:
                    cursor.execute("UPDATE users SET username = %s WHERE username = %s", (new_username, session['username']))
                    db.commit()
                    session['username'] = new_username  
                    flash(f'Username changed to: {new_username}', 'success')

            elif action_type == 'change_password':
                current_pwd = request.form['current_password'].strip()
                new_pwd = request.form['new_password'].strip()

                cursor.execute("SELECT * FROM users WHERE username = %s", (session['username'],))
                user = cursor.fetchone()
                
                if user and user['password'] == current_pwd:
                    cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_pwd, session['username']))
                    db.commit()
                    flash('Password updated! Please log in again.', 'success')
                    session.clear()
                    cursor.close()
                    db.close()
                    return redirect(url_for('login'))
                else:
                    flash('Incorrect current password!', 'danger')
        except Exception as e:
            db.rollback()
            flash(f'Settings Error: {str(e)}', 'danger')
        finally:
            return redirect(url_for('settings'))

    cursor.execute("SELECT hospital_name FROM settings WHERE id = 1")
    h_res = cursor.fetchone()
    current_h_name = h_res['hospital_name'] if h_res else "City Hospital"
    cursor.close()
    db.close()
    return render_template('settings.html', current_hospital_name=current_h_name)


# ==========================================
# 7. DELETE ACTIONS
# ==========================================
@app.route('/delete/<string:type>/<int:id>')
def delete_item(type, id):
    if 'logged_in' not in session:
        return redirect(url_for('login'))
        
    db = get_db_connection()
    if db:
        try:
            cursor = db.cursor()
            table_name = 'patients' if type == 'patient' else ('doctors' if type == 'doctor' else 'appointments')
            cursor.execute(f"DELETE FROM {table_name} WHERE id = %s", (id,))
            db.commit()
            flash(f'{type.capitalize()} deleted successfully!', 'warning')
        except Exception as e:
            db.rollback()
            flash(f'Error deleting: {str(e)}', 'danger')
        finally:
            cursor.close()
            db.close()
    return redirect(url_for(type + 's' if type != 'appointment' else 'appointments'))


# ==========================================
# 8. LOGOUT ROUTE
# ==========================================
@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)