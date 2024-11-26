import streamlit as st

# Set the title of the app
st.title("Student Biography: [Hazel D. simorlan]")

# Add an image (you can replace the URL with your own image)
st.image("https://via.placeholder.com/150", caption="Student Profile", width=150)

# Section: Introduction
st.header("Hello! I'm [Hazel D. Simorlan] 👋")
st.write("""
Welcome to my biography page! I am a student at [surigao city state university], and I am passionate about [BSCpE].
I love learning and am always eager to explore new challenges and opportunities in the field of [Computer engineering].
""")

# Section: Education
st.header("Education 🎓")
st.write("""
- **Current Program**: [programming] (e.g., Bachelor of Science in Computer engineering)
- **University**: [surigao city state university]
- **Year of Study**: [2024 2025, e.g., ,collage]
- **Expected Graduation**: [2027 2028]
""")

# Section: Interests
st.header("My Interests 💡")
st.header("I am passionate about several topics and activities 💡")
st.write("""
I have a variety of interests that I actively pursue. These include:
""")
# List of passions
st.write("""
- **Web Development**: I love building interactive and dynamic websites using technologies like JavaScript, React, and Node.js.
- **Machine Learning**: I am passionate about teaching machines to learn from data and apply algorithms to make predictions and solve problems.
- **Photography**: Capturing moments through photography is one of my hobbies. I enjoy both landscape and portrait photography.
- **Traveling**: Exploring new cultures and traveling around the world is something that inspires me and helps me broaden my horizons.
- **Music**: I play the guitar and enjoy composing music in my spare time.
""")

# Section: Skills
st.header("Skills 🛠️")
st.write("""
I have developed a range of technical and soft skills, including:
- **Programming Languages**: Python, JavaScript, C++, Java
- **Tools & Technologies**: SQL, Flask, TensorFlow, Git, Docker
- **Soft Skills**: Problem-solving, Team Collaboration, Communication, Leadership
""")

# Section: Projects
st.header("My Projects 🔧")
st.write("""
"Here are a few projects I've worked on during my studies"
- **[Project 1]**: [Brief Description of the Project]. Technologies used: [e.g., Python, Flask, PostgreSQL].
- **[Project 2]**: [Brief Description of the Project]. Technologies used: [e.g., JavaScript, Node.js, MongoDB].
- **[Project 3]**: [Brief Description of the Project]. Technologies used: [e.g., TensorFlow, Keras, Python].
""")

# Section: Goals
st.header("My Goals ")
st.write("""
- **Short-Term Goal**: [Your short-term goal, e.g., "Complete my current semester with a high GPA."]
- **Long-Term Goal**: [Your long-term career goal, e.g., "Become a software engineer and work on AI-driven applications."]
""")

# Section: Contact Information
st.header("Contact Me 📧")
st.write("""
Feel free to reach out to me:
- **Email**: [hazeldeguiasimorlan@gmail.com]
- **LinkedIn**: [LinkedIn Profile URL]
- **GitHub**: [GitHub Profile URL]
""")

# Add some interactivity (optional)
st.sidebar.header("Personal Details")
st.sidebar.write("""
- **Date of Birth**: September 11, 2006
- **Hobbies**: Reading, Coding, Exploring on Social Media
""")

