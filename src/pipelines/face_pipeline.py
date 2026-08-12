import dlib
import numpy as np
import face_recognition_models
from sklearn.svm import SVC
import streamlit as st
from src.database.db import get_all_students

@st.cache_resource
def load_dlib_models():
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor(
        face_recognition_models.pose_predictor_model_location()
    )
    facerec = dlib.face_recognition_model_v1(
        face_recognition_models.face_recognition_model_location()
    )
    return detector, sp, facerec

def get_face_embeddings(image_np):
    detector, sp, facerec = load_dlib_models()
    faces = detector(image_np, 1)
    encodings = []

    for face in faces:
        shape = sp(image_np, face)
        face_descriptor = facerec.compute_face_descriptor(image_np, shape, 1)  # 128 embedding
        encodings.append(np.array(face_descriptor))
    return encodings

@st.cache_resource
def get_trained_model():
    X = []
    y = []

    try:
        student_db = get_all_students()
    except Exception:
        return None

    if not student_db:
        return None
    
    for student in student_db:
        embedding = student.get('face_embedding')
        if embedding:
            X.append(np.array(embedding))
            y.append(student.get('student_id'))

    if len(X) == 0:
        return None
    
    all_classes = sorted(list(set(y)))
    if len(all_classes) < 2:
        return {'clf': None, 'X': X, 'y': y}

    clf = SVC(kernel='linear', probability=True, class_weight='balanced')
    try:
        clf.fit(X, y)
    except Exception:
        clf = None

    return {'clf': clf, 'X': X, 'y': y}

def train_classifier():
    st.cache_resource.clear()
    model_data = get_trained_model()
    return bool(model_data)

def predict_attendance(class_image_np):
    encodings = get_face_embeddings(class_image_np)
    detected_student = {}

    if not encodings:
        return detected_student, [], 0

    model_data = get_trained_model()
    if not model_data or not model_data.get('X'):
        return detected_student, [], len(encodings)
    
    clf = model_data.get('clf')
    X_train = model_data.get('X')
    y_train = model_data.get('y')

    all_students = sorted(list(set(y_train)))

    for encoding in encodings:
        # Calculate Euclidean distances to all registered student face embeddings
        distances = [np.linalg.norm(x - encoding) for x in X_train]
        if not distances:
            continue
            
        best_idx = int(np.argmin(distances))
        min_dist = float(distances[best_idx])
        
        # Robust dlib threshold (0.68) for matching registered student profiles
        if min_dist <= 0.68:
            predicted_id = int(y_train[best_idx])
            detected_student[predicted_id] = True
        elif clf is not None and len(all_students) >= 2:
            try:
                svm_pred = int(clf.predict([encoding])[0])
                svm_indices = [idx for idx, sid in enumerate(y_train) if sid == svm_pred]
                if svm_indices:
                    svm_dist = min(np.linalg.norm(X_train[idx] - encoding) for idx in svm_indices)
                    if svm_dist <= 0.68:
                        detected_student[svm_pred] = True
            except Exception:
                pass

    return detected_student, all_students, len(encodings)
