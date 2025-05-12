# HW3 CMPE131

I was having issues with connecting the wrong github account to my gradescope and cannot change it. This is my HW3 for Natalie Tran 017266093, CMPE131.
---

## Setup Instructions

### 1. Clone this Repository
```bash
git clone git@github.com:tedwu1/Recipe-Maker-Web-App.git
cd <project-directory>
```

### 2. Install the packages, make sure you already have Python 3 installed!

```bash
pip install flask flask_sqlalchemy flask_wtf flask_login
```

### 3. Initialize the Database by using this code in your terminal(assuming bash)
This is to create a sample user that can login and add/view/delete recipes

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> from app.models import User
>>> u = User(username="admin")
>>> u.set_password("password")
>>> db.session.add(u)
>>> db.session.commit()
>>> exit()
```

### 4. Finally, run the Application
```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Then open your browser to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Login Information
The sample login that we initialized in Step 3 is this: 
- **Username:** `admin`
- **Password:** `password`