const express = require('express');
const mongoose = require('mongoose');
const dotenv = require('dotenv');
const path = require('path');
const http = require('http');
const socketIo = require('socket.io');
const session = require('express-session');

const authRoutes = require('./routes/auth');
const appointmentRoutes = require('./routes/appointments');
const adminAuthRoutes = require('./routes/adminAuth');
const adminRoutes = require('./routes/admin');

dotenv.config();
const app = express();
const server = http.createServer(app);
const io = socketIo(server, { cors: { origin: "*" } }); 
app.set('io', io);

app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(session({
  secret: 'admin-secret',
  resave: false,
  saveUninitialized: true
}));

mongoose.connect(process.env.MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log("MongoDB Connected"))
  .catch((err) => console.error("MongoDB Error:", err));

app.use('/auth', authRoutes);
app.use('/appointments', appointmentRoutes);
app.use('/admin', adminAuthRoutes);
app.use('/admin', adminRoutes);

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'index.html'));
});
app.get('/login.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'login.html'));
});
app.get('/register.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'register.html'));
});
app.get('/dashboard.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'dashboard.html'));
});
app.get('/book.html', (req, res) => {
  res.sendFile(path.join(__dirname, 'views', 'book.html'));
});

const PORT = process.env.PORT || 9000;
server.listen(PORT, () => console.log(`Server running on port ${PORT}`));
