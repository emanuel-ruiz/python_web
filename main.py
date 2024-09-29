import streamlit as st
st.set_page_config(layout='wide')

col1, col2  = st.columns(2) # returns to instances of columns

with col1:
    st.image("images/Photo.jpg", width=300)

with col2:
    st.title("Emanuel Ruiz")
    content = """
        🚀 𝗔𝘀𝗽𝗶𝗿𝗶𝗻𝗴 𝗘𝗻𝘁𝗿𝘆 𝗟𝗲𝘃𝗲𝗹 𝗦𝗼𝗳𝘁𝘄𝗮𝗿𝗲 𝗘𝗻𝗴𝗶𝗻𝗲𝗲𝗿 with a solid foundation in software development and a proven track record of delivering intuitive, high-performance applications. Armed with a 𝗕.𝗦. 𝗶𝗻 𝗖𝗼𝗺𝗽𝘂𝘁𝗲𝗿 𝗦𝗰𝗶𝗲𝗻𝗰𝗲, 𝗠𝗶𝗹𝗶𝘁𝗮𝗿𝘆 𝗘𝘅𝗽𝗲𝗿𝗶𝗲𝗻𝗰𝗲, and hands-on experience in both frontend and backend development, I specialize in 𝗣𝘆𝘁𝗵𝗼𝗻, 𝗖++, 𝗝𝗮𝘃𝗮, 𝗮𝗻𝗱 𝗞𝗼𝘁𝗹𝗶𝗻—designing scalable solutions that are secure, efficient, and user-friendly.
SKILLS 
     •	𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗶𝗻𝗴 𝗟𝗮𝗻𝗴𝘂𝗮𝗴𝗲𝘀, 𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸𝘀, 𝗧𝗼𝗼𝗹𝘀: Python, C++, Kotlin, Java, HTML, CSS, JavaScript, Numpy, Pyplot, Keras, Object-Oriented Programming (OOP) 
     •	𝗘𝗻𝘃𝗶𝗿𝗼𝗻𝗺𝗲𝗻𝘁𝘀 𝗮𝗻𝗱 𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸𝘀: Qt 6 Creator, Visual Studio Code, Android Studio, Unreal Engine 4, Test Cases
     •	𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 𝗠𝗮𝗻𝗮𝗴𝗲𝗺𝗲𝗻𝘁 & 𝗖𝗹𝗼𝘂𝗱 𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺𝘀: NoSQL, SQL, Firebase Firestore
     •	𝗗𝗲𝘃𝗢𝗽𝘀, 𝗔𝘂𝘁𝗼𝗺𝗮𝘁𝗶𝗼𝗻 & 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 𝗖𝗼𝗻𝘁𝗿𝗼𝗹: CI/CD Pipelines, Git, GitHub 
     •	𝗢𝗽𝗲𝗿𝗮𝘁𝗶𝗻𝗴 𝗦𝘆𝘀𝘁𝗲𝗺𝘀: Windows, Linux

🔍 𝗠𝘆 𝗘𝘅𝗽𝗲𝗿𝗶𝗲𝗻𝗰𝗲 includes leading the development of a desktop calculator widget using the Qt Creator Framework, which reduced user error correction time by 25%, and optimizing an Android application’s backend, decreasing data fetch times by 50%. I thrive in 𝗔𝗴𝗶𝗹𝗲 𝗲𝗻𝘃𝗶𝗿𝗼𝗻𝗺𝗲𝗻𝘁𝘀 and have implemented CI/CD pipelines to accelerate feature deployment while maintaining code quality. My Army background has ingrained a strong work ethic, adaptability, and a focus on security—skills I now apply to software engineering challenges.
🔧 𝗖𝗼𝗿𝗲 𝗖𝗼𝗺𝗽𝗲𝘁𝗲𝗻𝗰𝗶𝗲𝘀: Object-Oriented Programming (OOP), UI/UX Design, Full-Stack Development, Database Management (SQL, NoSQL, Firebase), Agile Methodologies, CI/CD Pipelines, DevOps, Cloud Solutions, Secure Communication.
💼 𝗣𝗿𝗼𝗷𝗲𝗰𝘁𝘀: From developing an Android app that connects users based on shared interests to engineering a Convolutional Neural Network with 82% accuracy, I bring a diverse portfolio that showcases my ability to deliver impactful solutions.
It would be great to connect! I also enjoy growing my network - so please feel free to reach out anytime
    """
    st.info(content)