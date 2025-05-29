
# Victoria Multi Speciality Hospital Appointment Booking System

![Hospital Logo](./public/images/hospital-logo.jpg)

> A real-time, full-stack web application for booking, managing, and canceling appointments at a multi-specialty hospital.

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Docker Instructions](#docker-instructions)
- [Usage](#usage)
- [Admin Features](#admin-features)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## 📌 About The Project

The Victoria Hospital Appointment Booking System enables secure, real-time management of hospital appointments. It supports patient bookings, admin management, email notifications, statistics via charts, and chatbot assistance.

---

## ⚒️ Built With

- Node.js + Express.js
- HTML, CSS, JavaScript
- MongoDB Atlas
- Socket.IO
- Nodemailer
- Botpress
- Chart.js
- Docker
- Selenium

---

## 🚀 Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/)
- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [Docker](https://www.docker.com/products/docker-desktop)

### Installation (Without Docker)

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/victoria-hospital-booking.git
   cd victoria-hospital-booking
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create a `.env` file:
   ```env
   MONGO_URI=your_mongo_uri
   JWT_SECRET=your_jwt_secret
   EMAIL_USER=your_email
   EMAIL_PASS=your_password
   ```

4. Run the app:
   ```bash
   node server.js
   ```

---

## 🐳 Docker Instructions

### Build Docker Image
```bash
docker build -t victoria-hospital-app .
```

### Run Docker Container
```bash
docker run -p 9000:9000 victoria-hospital-app
```

### Access the App
Visit: `http://localhost:9000`

### Test `/api/student` Route
Visit: `http://localhost:9000/api/student`

Expected output:
```json
{
  "name": "YOUR_NAME",
  "studentId": "YOUR_STUDENT_ID"
}
```

---

## 🧪 Usage

### For Patients
- Register/Login
- Book/reschedule/cancel appointments
- Email confirmations
- Chatbot assistance

### For Admins
- Dashboard with real-time updates
- Inline reschedule/cancel
- Department & status filters
- Appointment stats via charts
- Export data as PDF/CSV
- Docker deployment support

---

## 🛠️ Admin Features

- Inline rescheduling and canceling
- Appointment filtering
- Real-time Socket.IO updates
- Email alerts (Nodemailer with BCC)
- Chart.js analytics
- Chatbot support via Botpress

---

## 🛣 Roadmap

| Feature                        | Status |
|-------------------------------|--------|
| User Auth                     | ✅     |
| Booking System                | ✅     |
| Admin Panel                   | ✅     |
| Real-time Updates             | ✅     |
| Email Notifications           | ✅     |
| Disable Booked Slots          | ✅     |
| Charts and Analytics          | ✅     |
| Export PDF/CSV                | ✅     |
| Docker Deployment             | ✅     |
| /api/student Route            | ✅     |

---

## 🤝 Contributing

1. Fork the project  
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

---

## 🧾 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📫 Contact

Victoria Team – mailappointmentbooking@gmail.com

Project Link: [https://github.com/AishuN1107/Victoria-Hospital-Appointment-Booking-Platform](https://github.com/AishuN1107/Victoria-Hospital-Appointment-Booking-Platform)

---

## 🙏 Acknowledgments

- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [Socket.IO](https://socket.io)
- [Nodemailer](https://nodemailer.com/about/)
- [Botpress](https://botpress.com)
- [Selenium](https://www.selenium.dev)
- [Font Awesome](https://fontawesome.com)
