from flask import Flask, render_template, request, jsonify
import os
import shutil
import openpyxl
from datetime import datetime
from mail import send_email_to_hr
from inquirymail import send_contact_inquiry
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
EXCEL_FILE = "careers.xlsx"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

if not os.path.exists(EXCEL_FILE):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["Name", "Email", "Phone", "Position", "Resume", "Date"])
    wb.save(EXCEL_FILE)

# Home route
@app.route('/')
def home():
    # Dynamic data for the ticker
    stats = {
        "crude": "-1.2$",
        "nat_gas": "+1.5%",
    }
    return render_template('home.html', active='home', stats=stats)

# About Us route
@app.route('/about')
def about():
    return render_template('about.html', active='about')

# Products route
@app.route('/product')
def product():
    return render_template('products.html', active='product')

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html', active='contact')
    
    try:
        # Get data from the form
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        # Trigger the email (to HR, Owner, BCC, and Auto-reply to user)
        status_msg = send_contact_inquiry(name, email, subject, message)
        
        # We pass the status back to the template to show the success message
        return render_template('contact.html', active='contact', status=status_msg)

    except Exception as e:
        print("CONTACT ERROR:", e)
        return render_template('contact.html', active='contact', status="Error: Could not send message.")

# Solvent route
@app.route('/products/solvents')
def solvent_list():
    return render_template('products/solvents/solvent.html', active='product')

@app.route('/products/solvents/newmax_a')
def newmax_a():
    return render_template('products/solvents/newmax_a.html',  active='product') 

@app.route('/products/solvents/newmax_b')
def newmax_b():
    return render_template('products/solvents/newmax_b.html',  active='product')

@app.route('/products/solvents/niomax')
def niomax():
    return render_template('products/solvents/niomax.html',  active='product')

@app.route('/products/solvents/niomax90')
def niomax90():
    return render_template('products/solvents/niomax90.html',  active='product')

@app.route('/products/solvents/niomol')
def niomol():
    return render_template('products/solvents/niomol.html',  active='product')

@app.route('/products/solvents/niosol100')
def niosol100():
    return render_template('products/solvents/niosol100.html',  active='product')

@app.route('/products/solvents/niosol150')
def niosol150():
    return render_template('products/solvents/niosol150.html',  active='product')

@app.route('/products/solvents/niosol200')
def niosol200():
    return render_template('products/solvents/niosol200.html',  active='product')

@app.route('/products/solvents/niosol250')
def niosol250():
    return render_template('products/solvents/niosol250.html',  active='product')

@app.route('/products/solvents/niosol150plus')
def niosol150plus():
    return render_template('products/solvents/niosol_150_Plus.html',  active='product')

# Oil route
@app.route('/products/oils')
def oil_list():
    return render_template('products/oils/oil.html', active='product')

@app.route('/products/oils/atf')
def atf():
    return render_template('products/oils/atf.html', active='product')

@app.route('/products/oils/ago')
def ago():
    return render_template('products/oils/ago.html', active='product')

@app.route('/products/oils/base')
def base():
    return render_template('products/oils/base.html', active='product')

@app.route('/products/oils/brake')
def brake():
    return render_template('products/oils/brake.html', active='product')

@app.route('/products/oils/compressor')
def compressor():
    return render_template('products/oils/compressor.html', active='product')

@app.route('/products/oils/cutting')
def cutting():
    return render_template('products/oils/cutting.html', active='product')

@app.route('/products/oils/bike')
def bike():
    return render_template('products/oils/bike.html', active='product')

@app.route('/products/oils/thermic')
def thermic():
    return render_template('products/oils/thermic.html', active='product')

@app.route('/products/oils/hydraulic')
def hydraulic():
    return render_template('products/oils/hydraulic.html', active='product')

@app.route('/products/oils/igo')
def igo():
    return render_template('products/oils/igo.html', active='product')

@app.route('/products/oils/machine')
def machine():
    return render_template('products/oils/machine.html', active='product')

@app.route('/products/oils/quenching')
def quenching():
    return render_template('products/oils/quenching.html', active='product')

@app.route('/products/oils/spindle')
def spindle():
    return render_template('products/oils/spindle.html', active='product')

# Other Chemical route
@app.route('/products/chemicals')
def chemical_list():
    return render_template('products/chemicals/chemical.html', active='product')

@app.route('/products/chemicals/acetone')
def acetone():
    return render_template('products/chemicals/acetone.html', active='product')

@app.route('/products/chemicals/mix_xylene')
def mix_xylene():
    return render_template('products/chemicals/mix_xylene.html', active='product')

@app.route('/products/chemicals/toluene')
def toluene():
    return render_template('products/chemicals/toluene.html', active='product')

@app.route('/products/chemicals/ipa')
def ipa():
    return render_template('products/chemicals/ipa.html', active='product')

@app.route('/products/chemicals/phenol')
def phenol():
    return render_template('products/chemicals/phenol.html', active='product')

# Other Chemical route
@app.route('/products/otherchemical')
def otherchem_list():
    return render_template('products/otherchemical/fuel.html', active='product')

@app.route('/products/otherchemical/gas')
def gas():
    return render_template('products/otherchemical/oil_gas_drilling.html', active='product')

@app.route('/products/otherchemical/water')
def water():
    return render_template('products/otherchemical/water.html', active='product')

# Sustainbility route
@app.route('/sustainbility')
def sustainbility():
    return render_template('sustainability.html', active='sustainbility')

# Privacy route
@app.route('/privacy')
def privacy():
    return render_template('privacy.html', active='sustainbility')

# Gobal Office route
@app.route('/globaloffice')
def office():
    return render_template('global.html', active='sustainbility')

# Investor route
@app.route('/Investor')
def investor():
    return render_template('investor.html', active='sustainbility')

# Term of Serivce 
@app.route('/Term of Servies')
def term():
    return render_template('term.html', active='home')

# Career route
@app.route('/career', methods=["GET", "POST"])
def career():
    if request.method == "GET":
        return render_template('career.html', active='career')

    try:
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        position = request.form.get("position")
        resume = request.files.get("resume")

        # ✅ Validation
        if not resume or resume.filename == "":
            return jsonify({"status": "error", "message": "No file uploaded"}), 400

        # ✅ Unique filename (important)
        filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{resume.filename}"
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        resume.save(file_path)

        # ✅ Save to Excel
        wb = openpyxl.load_workbook(EXCEL_FILE)
        ws = wb.active
        ws.append([
            name,
            email,
            phone,
            position,
            filename,
            datetime.now().strftime("%Y-%m-%d %H:%M")
        ])
        wb.save(EXCEL_FILE)

        # ✅ Send email
        send_email_to_hr(name, email, phone, position, file_path)

        return jsonify({"status": "success"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"status": "error"}), 500

        # Send email
        send_email_to_hr(name, email, phone, position, file_path)

        return jsonify({"status": "success"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"status": "error"}), 500

last_data = {
    "crude_price": 75,
    "crude_change": 0,
    "gas_price": 2.5,
    "gas_change": 0
}

def get_price(symbol):
    try:
        url = f"https://stooq.com/q/l/?s={symbol}&f=sd2t2ohlcv&h&e=csv"
        res = requests.get(url, timeout=5).text

        lines = res.split("\n")
        if len(lines) < 2:
            return None

        values = lines[1].split(",")

        price = float(values[6])  # Close price
        return price
    except:
        return None


@app.route('/api/market')
def market_data():
    global last_data

    try:
        crude_price = get_price("cl.f")   # crude oil
        gas_price = get_price("ng.f")     # natural gas

        if crude_price:
            last_data["crude_change"] = crude_price - last_data["crude_price"]
            last_data["crude_price"] = crude_price

        if gas_price:
            last_data["gas_change"] = gas_price - last_data["gas_price"]
            last_data["gas_price"] = gas_price

        return jsonify(last_data)

    except Exception as e:
        print("ERROR:", e)
        return jsonify(last_data)

if __name__ == '__main__':
    app.run(debug=True)