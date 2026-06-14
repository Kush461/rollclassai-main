import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
import numpy as np
from src.database.db import get_all_students, create_student
from PIL import Image
import time
from src.components.dialog_enroll import enroll_dialog
from src.database.db import get_student_attendance,get_student_subjects,enroll_student_to_subject,unenroll_student_from_subject
from src.components.subject_card import subject_card

def student_dashboard():
    student_data = st.session_state.student_data 
    student_id = student_data["student_id"]
    c1, c2 = st.columns([3, 1], vertical_alignment="center")
    with c1: 
        header_dashboard() 
    with c2: 
        st.write(f"""Welcome {student_data["name"]}""")
        if st.button("← Logout", type="secondary", key="backtohome", shortcut="control+backspace"): 
            st.session_state["is_logged_in"] = False
            del st.session_state.student_data
            st.rerun()

    st.space() 

    c1,c2 = st.columns(2)
    with c1: 
        st.header("Your Enrolled Subjects")

    with c2: 
        if st.button("Enroll in Subject",type="primary",width="stretch"): 
            enroll_dialog()

    st.divider()

    with st.spinner("Loading your subjects..."):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    stats_map = {}

    for log in logs:
        subject_id = log["subject_id"]
        if subject_id not in stats_map: 
            stats_map[subject_id] = {"total":0,"present":0}

        stats_map[subject_id]["total"] += 1

        if log.get("is_present"):
            stats_map[subject_id]["present"] += 1

    cols = st.columns(2)
    for i,sub_node in enumerate(subjects):
        sub = sub_node["subjects"]
        sub_id = sub["subject_id"]

        stats = stats_map.get(sub_id,{"total":0,"present":0})
        def unroll_button(): 
            if st.button("Unenroll from this course",type="tertiary",width="stretch",icon=":material/delete_forever:"): 
                unenroll_student_from_subject(student_id,subject_id=sub_id)
                st.toast(f"unenrolled from {sub["name"]} course successfully")
                st.rerun()
        with cols[i%2]:
            subject_card(
                name = sub["name"], 
                code = sub["subject_code"], 
                section = sub["section"],
                stats = [
                    ("📋","Total",stats["total"]), 
                    ("✅","Present",stats["present"])
                ],
                footer_callback=unroll_button
            )

    footer_dashboard()

def stud_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    if "show_registration" not in st.session_state:
        st.session_state.show_registration = False

    c1, c2 = st.columns([3, 1], vertical_alignment="center")
    with c1:
        header_dashboard()
    with c2:
        if st.button("← Home", type="secondary", key="backtohome", shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.session_state.show_registration = False
            st.rerun()

    st.header("Login using FaceID", divider=False, text_alignment="center")
    st.space()

    photo_source = st.camera_input("Position your face in the center")
    if photo_source:
        img = np.array(Image.open(photo_source))
        with st.spinner("Scanning..."):
            detected, all_ids, num_faces = predict_attendance(img)
            if num_faces == 0:
                st.warning("Face not found")
                st.session_state.show_registration = False
            elif num_faces > 1:
                st.warning("Multiple faces found")
                st.session_state.show_registration = False
            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next((s for s in all_students if s["student_id"] == student_id), None)
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = "student"
                        st.session_state.student_data = student
                        st.session_state.show_registration = False
                        st.toast(f"Welcome back! {student['name']}")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.info("Face not recognised. You might be a new student")
                        st.session_state.show_registration = True
                else:
                    st.info("Face not recognised. You might be a new student")
                    st.session_state.show_registration = True

    if st.session_state.show_registration:
        with st.container(border=True):
            st.header("Register new profile")
            new_name = st.text_input("Enter your name")
            st.subheader("Optional: Voice Enrollment")
            st.info("Enroll for voice only attendance")

            audio_data = None
            try:
                audio_data = st.audio_input("Record a short phrase like I am present. My name is Akash")
            except Exception:
                st.error("Audio input failed")

            if st.button("Create Profile", type="primary"):
                if new_name:
                    with st.spinner("Creating profile..."):
                        img = np.array(Image.open(photo_source))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()
                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())

                            response_data = create_student(new_name, face_emb, voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = "student"
                                st.session_state.student_data = response_data[0]
                                st.session_state.show_registration = False
                                st.toast(f"Profile created! {new_name}")
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error("Couldn't capture your face. Please retake the photo.")
                else:
                    st.warning("Please enter your name")

    footer_dashboard()