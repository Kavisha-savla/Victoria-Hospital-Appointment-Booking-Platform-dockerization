const mongoose = require('mongoose');
const express = require('express');
const router = express.Router();
const Appointment = require('../models/Appointment');
const sendEmail = require('../utils/mailer');
const User = require('../models/user');

router.post('/book', async (req, res) => {
  const io = req.app.get('io');
  const {
    userId, name, age, phone, gender, department,
    service, date, time
  } = req.body;

  if (!mongoose.Types.ObjectId.isValid(userId)) {
    return res.status(400).json({ error: 'Invalid user ID format.' });
  }

  try {
    const appointment = await Appointment.create({
      userId: new mongoose.Types.ObjectId(userId),
      name, age, phone, gender, department, service, date, time
    });

    const user = await User.findById(userId);
    await sendEmail(
  user.email,
  "Appointment Confirmation – Victoria Multi Speciality Hospital",
  `
  <p>Dear ${name},</p>
  <p>Your appointment has been successfully booked. Here are the details:</p>
  <ul>
    <li><strong>Date:</strong> ${new Date(date).toDateString()}</li>
    <li><strong>Time:</strong> ${time}</li>
    <li><strong>Department:</strong> ${department}</li>
    <li><strong>Service:</strong> ${service}</li>
  </ul>
  <p>Please arrive 10–15 minutes early for check-in. If needed, contact us at +61 1800 000 911 or support@victoriahospital.com.</p>
  <p>Warm regards,<br/>Victoria Multi Speciality Hospital – Administration Team</p>
  `,
  "admin@victoriahospital.com" 
);
    io.emit('appointment:booked', appointment);
    res.status(201).json({ message: "Appointment booked and email sent." });
  } catch (e) {
    console.error("Booking error:", e);
    res.status(400).json({ error: "Error booking appointment." });
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
  "Appointment Cancelled – Victoria Multi Speciality Hospital",
  `
  <p>Dear ${user.name || appointment.name},</p>
  <p>Your appointment scheduled on <strong>${new Date(appointment.date).toDateString()}</strong> at <strong>${appointment.time}</strong> for <strong>${appointment.service}</strong> in the <strong>${appointment.department}</strong> department has been cancelled.</p>
  <p>If you’d like to reschedule, please reach out at +61 1800 000 911 or support@victoriahospital.com.</p>
  <p>Kind regards,<br/>Victoria Multi Speciality Hospital – Administration Team</p>
  `,
  "admin@victoriahospital.com"
);


    io.emit('appointment:cancelled', appointment);
    res.send('Appointment cancelled and email sent.');
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
  "Appointment Rescheduled – Victoria Multi Speciality Hospital",
  `
  <p>Dear ${user.name || name},</p>
  <p>Your appointment has been successfully rescheduled. Here are the updated details:</p>
  <ul>
    <li><strong>New Date:</strong> ${new Date(newDate).toDateString()}</li>
    <li><strong>New Time:</strong> ${newTime}</li>
    <li><strong>Department:</strong> ${appointment.department}</li>
    <li><strong>Service:</strong> ${appointment.service}</li>
  </ul>
  <p>If you need to change it again, call +61 1800 000 911 or email support@victoriahospital.com.</p>
  <p>Take care,<br/>Victoria Multi Speciality Hospital – Administration Team</p>
  `,
  "admin@victoriahospital.com"
);


    io.emit('appointment:rescheduled', appointment);
    res.send('Appointment rescheduled and email sent.');
  } catch {
    res.status(500).send('Error rescheduling appointment');
  }
});

router.get('/user/:userId', async (req, res) => {
  try {
    const appts = await Appointment.find({ userId: req.params.userId });
    res.json(appts);
  } catch (e) {
    res.status(500).send("Could not fetch appointments");
  }
});

router.get('/booked-times', async (req, res) => {
  const { date } = req.query;
  if (!date) return res.status(400).send("Date required");

  try {
    const startOfDay = new Date(date);
    const endOfDay = new Date(date);
    endOfDay.setHours(23, 59, 59, 999);

    const appointments = await Appointment.find({
      date: { $gte: startOfDay, $lte: endOfDay },
      status: { $ne: 'cancelled' }
    });

    const bookedTimes = appointments.map(app => app.time);
    res.json(bookedTimes);
  } catch (e) {
    console.error("Fetch booked times error:", e);
    res.status(500).send("Could not fetch booked times");
  }
});

module.exports = router;
