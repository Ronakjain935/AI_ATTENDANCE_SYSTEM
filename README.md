<div align="center">
  <img src="https://i.ibb.co/YTYGn5qV/logo.png" alt="SnapClass Logo" width="120" />
  <h1>SnapClass - AI-Powered Attendance System</h1>
  <p><strong>Making classroom attendance 10x faster and automated using Facial & Voice Recognition AI</strong></p>

  [![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
  [![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
  [![dlib](https://img.shields.io/badge/dlib-Face_Recognition-blue?style=for-the-badge)](http://dlib.net/)
</div>

---

## 📌 About The Project

**SnapClass** is a modern, full-stack AI attendance platform designed to streamline classroom management for educational institutions. Instead of spending 10-15 minutes calling out roll numbers manually, teachers can take attendance in seconds by uploading a single classroom photo or recording classroom audio. 

SnapClass utilizes deep facial feature extraction via **dlib 128-dimensional embeddings**, vector similarity matching, voice speaker embedding comparison (**Resemblyzer**), and real-time database management using **Supabase**.

---

## 🌟 Key Features

### 📸 1. AI Facial Recognition Attendance
* Upload single or multiple classroom snapshots.
* AI scans and identifies all student faces simultaneously.
* Automatic classification matching registered student face profiles.
* Review & confirm scan results before logging to the database.

### 🎙️ 2. AI Voice Attendance
* Record classroom audio of students speaking (e.g. *"I am present"*).
* Speaker recognition powered by Resemblyzer voice embeddings to automatically identify students.

### 📲 3. QR Code & Instant Link Sharing
* Auto-generated high-resolution QR codes encoded with secure `https://` auto-enrollment links.
* **1-Click WhatsApp Sharing**: Send direct pre-formatted join links directly to class groups.
* **1-Click Email Sharing**: Send invitation emails to students.
* **Downloadable QR Code PNG**: Download and project or print QR codes for classroom displays.

### 👥 4. Student Portal & Permanent Profile Saving
* **Camera FaceID Login**: Log in by positioning your face in front of the camera.
* **Photo File Upload Login**: Log in by uploading a saved profile picture.
* **Profile Selection**: Quick login mode by selecting your registered name.
* **Permanent Profile Storage**: Student facial feature vectors & profile info are saved permanently in Supabase database.

### 📊 5. Teacher Dashboard & Attendance Records Management
* Create and manage subjects and sections.
* View total students enrolled and total classes conducted per subject.
* View attendance history breakdown grouped by timestamp and course.
* **🗑️ Delete Specific Session**: Delete individual attendance logs with instant confirmation.
* **🗑️ Clear All History**: Option to wipe out past log history safely.

---

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/), Custom CSS (Google Fonts *Outfit* & *Inter*)
* **Facial Recognition**: `dlib`, `face_recognition_models`, `scikit-learn` (SVM Classifier)
* **Voice Recognition**: `Resemblyzer`, `librosa`
* **Data & Media Handling**: `NumPy`, `Pandas`, `Pillow`
* **Database**: [Supabase](https://supabase.com/) (PostgreSQL backend)
* **QR Code & Security**: `segno`, `bcrypt`

---

## 📂 Project Structure

```text
snapclass/
├── .streamlit/
│   ├── config.toml           # Streamlit UI theme settings
│   └── secrets.toml          # Supabase credentials (git-ignored)
├── src/
│   ├── components/
│   │   ├── dialog_add_photo.py          # Modal for capturing/uploading photos
│   │   ├── dialog_attendance_results.py # Modal for verifying AI scan results
│   │   ├── dialog_auto_enroll.py        # Modal for quick QR link enrollment
│   │   ├── dialog_create_subject.py     # Modal for creating new subjects
│   │   ├── dialog_enroll.py             # Modal for manual subject code entry
│   │   ├── dialog_share_subject.py      # QR code & WhatsApp/Email share modal
│   │   ├── dialog_voice_attendance.py   # Voice attendance recording modal
│   │   ├── footer.py                    # App footer component
│   │   ├── header.py                    # App header component
│   │   └── subject_card.py              # Subject card widget
│   ├── database/
│   │   ├── config.py                    # Supabase client setup
│   │   └── db.py                        # CRUD database operations & query handlers
│   ├── pipelines/
│   │   ├── face_pipeline.py             # dlib & SVM facial recognition pipeline
│   │   └── voice_pipeline.py            # Resemblyzer voice embedding pipeline
│   ├── screens/
│   │   ├── home_screen.py               # Landing page (Student/Teacher portal selector)
│   │   ├── student_screen.py            # Student dashboard, FaceID login & registration
│   │   └── teacher_screen.py            # Teacher dashboard, attendance scanning & records
│   └── ui/
│       └── base_layout.py               # Master high-contrast CSS design system
├── app.py                           # Main application entrypoint
├── requirements.txt                 # Python dependencies
├── schema.sql                       # Database SQL table setup script
└── README.md                        # Documentation
```

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10 or higher
* Git

### 1. Clone the Repository
```bash
git clone https://github.com/Ronakjain935/AI_ATTENDANCE_SYSTEM.git
cd AI_ATTENDANCE_SYSTEM
```

### 2. Create & Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Supabase Database Setup
1. Create a free account at [Supabase](https://supabase.com/).
2. Create a new project and navigate to **SQL Editor**.
3. Copy the contents of [`schema.sql`](schema.sql) into the SQL Editor and click **Run**.
4. Retrieve your `SUPABASE_URL` and `SUPABASE_KEY` from **Project Settings -> API**.
5. Create `.streamlit/secrets.toml` in your project root:
   ```toml
   SUPABASE_URL = "https://your-supabase-url.supabase.co"
   SUPABASE_KEY = "your-supabase-anon-key"
   ```

### 5. Run the Application
```bash
streamlit run app.py
```
Open `http://localhost:8501` in your browser!

---

## 📄 Database Schema Overview

SnapClass uses 5 core relational tables in Supabase:
* `teachers`: Credentials & profile data.
* `students`: Registered names, 128-d face embedding vectors, and voice profiles.
* `subjects`: Subject codes, names, sections, and teacher links.
* `subject_students`: Student course enrollments.
* `attendance_logs`: Recorded attendance timestamps, subject IDs, and presence statuses.

---

## 👤 Author & Acknowledgments

Created with ⚡ by **Ronak Jain**  
GitHub: [@Ronakjain935](https://github.com/Ronakjain935)
