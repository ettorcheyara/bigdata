import streamlit as st
from pymongo import MongoClient
import pandas as pd
from streamlit_autorefresh import st_autorefresh


client = MongoClient(
    "mongodb://mongo1:27017,mongo2:27017,mongo3:27017/?replicaSet=rs0&readPreference=primary"
)
db = client.learntrack

st.title("Dashboard LearnTrack - Big Data (Live)")


REFRESH_INTERVAL = 5
st_autorefresh(interval=REFRESH_INTERVAL * 1000, key="datarefresh")


st.header(" Étudiants")
students_df = pd.DataFrame(list(db.students.find()))
if not students_df.empty:
    st.dataframe(students_df)
else:
    st.write("Pas d'étudiants pour l'instant")


st.header("Activités (dernières 50)")
activities_df = pd.DataFrame(list(db.activities.find().sort("timestamp", -1).limit(50)))
if not activities_df.empty:
    st.dataframe(activities_df)
else:
    st.write("Pas d'activités pour l'instant")


st.header(" Scores d'engagement")
engagement_df = pd.DataFrame(list(db.engagement_scores.find()))
if not engagement_df.empty:
    st.bar_chart(engagement_df.set_index("student_id")["engagement_score"])
else:
    st.write("Pas de scores pour l'instant")

st.header(" Rapports quotidiens")
reports_df = pd.DataFrame(list(db.daily_reports.find()))
if not reports_df.empty:
    st.bar_chart(reports_df.set_index("course_id")["total_activities"])
else:
    st.write("Pas de rapports pour l'instant")

st.header("Détections Multi-Régions")
suspicious_df = pd.DataFrame(list(db.suspicious_users.find()))
if not suspicious_df.empty:
    st.dataframe(suspicious_df)
else:
    st.write("Aucune détection suspecte pour l'instant")
