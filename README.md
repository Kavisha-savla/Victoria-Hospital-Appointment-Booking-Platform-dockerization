# Victoria Multi Speciality Hospital Appointment Booking System

![Product Name Screen Shot](./public/images/hospital-logo.jpg)

> A real-time, full-stack web application for booking, managing, and canceling appointments at a multi-specialty hospital.

---

## 📋 Table of Contents

- [About The Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

---

## 📌 About The Project

The Victoria Multi Speciality Hospital Appointment Booking System is designed to streamline how patients schedule, cancel, and reschedule appointments. Featuring secure authentication, real-time updates, time-slot blocking, email notifications, and a chatbot assistant, the system enables seamless, contactless hospital appointment handling.

Here's why we built this:

- To reduce human error and workload in appointment management.
- To enable patients to handle appointments across multiple devices.
- To demonstrate full-stack development with real-time and cloud integrations.

---

## ⚒️ Built With

- Node.js & Express.js
- HTML, CSS, JavaScript
- MongoDB Atlas (cloud database)
- Socket.IO (real-time updates)
- Nodemailer (email notifications)
- Botpress (chatbot assistant)
- Selenium WebDriver (testing)

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- npm

```sh
npm install npm@latest -g
```

### Installation

1. Clone the repo

```sh
git clone https://github.com/your_username/victoria-hospital-booking.git
```

2. Install NPM packages

```sh
npm install
```

3. Create a `.env` file in the root and add:

```env
MONGO_URI=your_mongodb_atlas_connection_string
JWT_SECRET=your_jwt_secret
EMAIL_USER=your_email
EMAIL_PASS=your_email_password_or_app_key
```

4. Run server

```sh
node server.js
```

---

##  Usage

###  For Users:
- Register or log in to your account
- Book an appointment by selecting date, time, department, and description
- Cancel or reschedule appointments via the user dashboard
- Receive confirmation, cancellation, and reschedule emails instantly
- Chatbot assistant available to guide users through the process

###  For Admins:
- Log in to the Admin Panel via the `/admin/dashboard` route
- View all appointments with filters (status: booked, cancelled, rescheduled | department-wise)
- Inline reschedule and cancel functionality built directly into appointment cards
- Real-time updates across all dashboards using **Socket.IO**
- Email notifications with **BCC support** to track appointment changes
- View **daily and weekly statistics** via integrated **Chart.js analytics**
- Export appointment data as **PDF** or **CSV** with one click
- Chatbot assistant for basic inquiries and automation support
- **Booked slots are disabled** to prevent double booking
- Fully supported **Docker deployment** for easy containerized hosting

Visit: `http://localhost:9000`

---

##  Admin Features

-  **Admin Dashboard** – Access, filter, and manage all appointments in one place.
-  **Search & Filter** – By status (booked, cancelled, rescheduled) and department.
-  **Disable Already-Booked Slots** – Prevents multiple users from booking the same time.
-  **Nodemailer Email Integration** – Email alerts to users and BCC to admin for all actions.
-  **Inline Reschedule & Cancel** – Adjust date/time or cancel without leaving the dashboard.
-  **Real-Time Updates** – Uses Socket.IO to reflect all changes live on both dashboards.
-  **Analytics with Chart.js** – Graphs for daily and weekly appointment trends.
-  **Export Appointments** – One-click export as PDF or CSV for reporting needs.
-  **Chatbot Assistant** – AI chatbot built with Botpress for admin and user support.
-  **Docker Deployment** – Seamlessly deployable with Docker for scalable environments.

---

##  Roadmap

| Feature                             | Status         | Sprint     |
|-------------------------------------|----------------|------------|
| User Registration & Login           | ✅ Completed    | Sprint 1   |
| Appointment Booking System          | ✅ Completed    | Sprint 1   |
| Admin Dashboard with Filtering      | ✅ Completed    | Sprint 2   |
| Real-time Updates (Socket.IO)       | ✅ Completed    | Sprint 2   |
| Email Notifications (Nodemailer)    | ✅ Improved     | Sprint 2   |
| Disable Booked Slots                | ✅ Implemented  | Sprint 2   |
| Visual Analytics (Chart.js)         | ✅ Completed    | Sprint 2   |
| Export as PDF/CSV                   | ✅ Completed    | Sprint 2   |
| Chatbot Assistant (Botpress)        | ✅ Integrated   | Sprint 2   |
| Docker Deployment                   | ✅ Configured   | Sprint 2   |
| Inline Reschedule/Cancel UI         | ✅ Completed    | Sprint 2   |

---

##  Contributing

Contributions make the open source community great!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🧾 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📫 Contact

Victoria Team - mailappointmentbooking@gmail.com

Project Link: [GitHub](https://github.com/AishuN1107/Victoria-Hospital-Appointment-Booking-Platform)

---

## 🙏 Acknowledgments

- [MongoDB Atlas](https://www.mongodb.com/atlas)
- [Socket.IO](https://socket.io)
- [Nodemailer](https://nodemailer.com/about/)
- [Botpress](https://botpress.com)
- [Selenium](https://www.selenium.dev)
- [Font Awesome](https://fontawesome.com)

---
