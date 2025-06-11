# 🚨 Help Wanted: CSRNet Headcount Web App (Uber Alpha 🚧)

Hey folks!

I work at a church, and for some reason, my pastors want to use machine vision to count the number of service attendees. So, I’m currently working on a Dockerized headcount web app powered by CSRNet (the crowd-counting deep learning model). The idea is to upload an image, run it through CSRNet, store the results in a DB, and then export everything into a preformatted Excel template.

The project is currently in **Uber Alpha** — meaning it’s about 80% vibe-coded and 20% duct tape. 😅 I’m actively cleaning up bugs, tightening up the logic, and improving structure.

* * *

### 🔍 What I’m Looking For

- **Feedback** on architecture (FastAPI + Docker + PyTorch)
- **Help debugging** any known issues or inefficiencies
- **Suggestions** for cleaning up the flow or improving the UI/API
- **Ideas** for features you'd like to see added
- **Any contributions** at all, honestly. PRs, issues, vibes... it's all welcome

* * *

### 💡 Quick Overview

- Upload an image → CSRNet estimates headcount
- Store results (filename, timestamp, people count)
- Export all that into a preformatted Excel `.xlsx` file
- Access everything through Swagger UI (`/docs`)
- Fully Dockerized

* * *

### 🧪 Try It Out

Clone the repo, download the pretrained weights from the [CSRNet repo](https://github.com/leeyeehoo/CSRNet-pytorch), and run:

    docker build -t headcount-app .docker run -p 8000:8000 -v %cd%:/app headcount-app # Use $(pwd) on Mac/Linux

Then go to:  
[**http://localhost:8000/docs**](http://localhost:8000/docs)

* * *

### 🧠 Tech Stack

- **FastAPI** backend
- **CSRNet** model (PyTorch)
- **SQLite** for now (pluggable DB later?)
- **openpyxl** for Excel export

* * *

### 🗂 Folder Layout

    headcount-app/├── app/│ ├── main.py│ ├── model/│ ├── routes/│ ├── db/│ └── export/├── template/├── Dockerfile├── requirements.txt├── .env└── README.md

* * *

### 🙏 Final Word

If you’re into computer vision, web dev, or just like the idea of having machines count heads so you don’t have to — I’d *love* your feedback or help.

**Thanks in advance for your time and any help you can offer.**  
**–  jumpinjet22**
