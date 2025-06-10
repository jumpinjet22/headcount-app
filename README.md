# 🧠 CSRNet Headcount Web App

This is a Dockerized web application that counts the number of people in uploaded images using the CSRNet deep learning model. It stores the results in a database and allows exporting to a preformatted Excel template.

---

## 📦 Features

* Upload images to detect and count people using CSRNet (PyTorch)
* Store results (image name, timestamp, count) in a database
* Export headcounts into a custom Excel sheet
* Fully Dockerized with FastAPI backend

---

## 🛠️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://your-repo-url.git
cd headcount-app
```

### 2. Download Pretrained CSRNet Weights

Download weights trained on [ShanghaiTech Part A](https://github.com/leeyeehoo/CSRNet-pytorch):

```bash
mkdir -p app/model/weights
wget -O app/model/weights/csrnet.pth.tar https://github.com/leeyeehoo/CSRNet-pytorch/releases/download/v1.0/partAmodel_best.pth.tar
```

> You can also manually download and place the file in `app/model/weights`.

---

## 🚀 Running the App

### With Docker:

```bash
docker build -t headcount-app .
docker run -p 8000:8000 -v %cd%:/app headcount-app
```

> On Linux/macOS use `$(pwd)` instead of `%cd%`.

The app will be available at:
`http://localhost:8000/docs` ← Swagger UI for testing

---

## 📄 Uploading Images

Send a `POST` request to `/upload` with an image file.
Returns JSON with the estimated count.

Example using `curl`:

```bash
curl -F "file=@people.jpg" http://localhost:8000/upload
```

---

## 📊 Export to Excel

Send a `GET` request to `/export_excel` to download an `.xlsx` file populated with headcount data based on your template in `template/Template.xlsx`.

---

## 📂 Folder Structure

```
headcount-app/
├── app/
│   ├── main.py
│   ├── model/
│   ├── routes/
│   ├── db/
│   └── export/
├── template/
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

## 📋 License

This project uses the CSRNet architecture for academic and non-commercial use. Original model: [CSRNet](https://github.com/leeyeehoo/CSRNet-pytorch)
