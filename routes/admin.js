const express = require('express');
const path = require('path');
const router = express.Router();
const isAdmin = require('../middleware/isAdmin');
const Appointment = require('../models/Appointment');
const sendEmail = require('../utils/mailer');
const User = require('../models/user');

router.get('/dashboard', isAdmin, (req, res) => {
  console.log('Admin dashboard accessed by:', req.session.user);
  res.sendFile(path.join(__dirname, '../views/adminDashboard.html'));
});

router.get('/api/appointments', async (req, res) => {
  try {
    const { status, department } = req.query;
    const query = {};

    if (status) query.status = status;
    if (department) query.department = department;

    console.log('Incoming query:', req.query);
    console.log('MongoDB query:', query);

    const appointments = await Appointment.find(query);
    res.json(appointments);
  } catch (err) {
    console.error('Error fetching appointments:', err);
    res.status(500).json({ error: 'Server error' });
  }
});

router.post('/cancel/:id', async (req, res) => {
  const io = req.app.get('io');

  try {
    const appointment = await Appointment.findByIdAndUpdate(
      req.params.id,
      { status: 'cancelled' },
      { new: true }
    );

    const user = await User.findById(appointment.userId);

    await sendEmail(
      user.email,
      "Appointment Cancelled by Hospital – Victoria Multi Speciality Hospital",
      `
        <p>Dear ${user.name || appointment.name},</p>
        <p>We would like to inform you that your appointment has been <strong>cancelled by our hospital team</strong>.</p>
        <ul>
          <li><strong>Date:</strong> ${new Date(appointment.date).toDateString()}</li>
          <li><strong>Time:</strong> ${appointment.time}</li>
          <li><strong>Department:</strong> ${appointment.department}</li>
          <li><strong>Service:</strong> ${appointment.service}</li>
        </ul>
        <p>If you need to rebook, please call us at +61 1800 000 911 or reply to this email.</p>
        <p>Thank you,<br/>Victoria Multi Speciality Hospital – Admin Team</p>
      `,
      "admin@victoriahospital.com"
    );

    io.emit('appointment:cancelled', appointment);
    res.send('Appointment cancelled and user notified via email.');
  } catch {
    res.status(500).send('Error cancelling appointment');
  }
});

router.post('/reschedule/:id', async (req, res) => {
  const io = req.app.get('io');
  const { newDate, newTime } = req.body;

  try {
    const appointment = await Appointment.findByIdAndUpdate(req.params.id, {
      date: newDate,
      time: newTime,
      status: 'rescheduled'
    }, { new: true });

    const user = await User.findById(appointment.userId);

    await sendEmail(
      user.email,
      "Appointment Rescheduled by Hospital – Victoria Multi Speciality Hospital",
      `
        <p>Dear ${user.name || appointment.name},</p>
        <p>This is to inform you that your appointment has been <strong>rescheduled by our hospital administration team</strong>.</p>
        <ul>
          <li><strong>New Date:</strong> ${new Date(newDate).toDateString()}</li>
          <li><strong>New Time:</strong> ${newTime}</li>
          <li><strong>Department:</strong> ${appointment.department}</li>
          <li><strong>Service:</strong> ${appointment.service}</li>
        </ul>
        <p>If you need to change this, please contact us at +61 1800 000 911 or support@victoriahospital.com.</p>
        <p>Best regards,<br/>Victoria Multi Speciality Hospital – Admin Team</p>
      `,
      "admin@victoriahospital.com" 
    );

    io.emit('appointment:rescheduled', appointment);
    res.send('Appointment rescheduled and user notified via email.');
  } catch {
    res.status(500).send('Error rescheduling appointment');
  }
});


router.get('/appointments/booked-times', async (req, res) => {
  const { date } = req.query;
  const appointments = await Appointment.find({ date });
  const bookedTimes = appointments.map(a => a.time);
  res.json(bookedTimes);
});


module.exports = router;
