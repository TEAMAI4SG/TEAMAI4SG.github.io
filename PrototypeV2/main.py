#PrototypeV2/
#├── pages/
#│   ├── resume_feedback.py
#│   └── job_postings.py
#└── main.py

#import streamlit as st
# from multiapp import MultiApp
# from PrototypeV2.pages.resume_feedback import resume_feedback
# from PrototypeV2.pages.job_postings import job_postings

# # Initialize MultiApp
# app = MultiApp()

# # Add pages
# app.add_app("Resume Feedback Tool", resume_feedback)
# app.add_app("Job Postings", job_postings)

# # Run the app
# app.run()
import streamlit as st

# This is the main page
st.title('CareerCanvas! 🚀')

st.write('Welcome to the home page! Where you can find all the tools you need to succeed in your career. 🌟')
st.write('Use the sidebar to navigate to different sections of the app. 📚')
st.write('You can find tools for resume advice, job postings, and mock interview practice! 📝')
st.write('Feel free to explore the different features of the app. ✨')



# Or images
st.image('CareerCanvas.png')