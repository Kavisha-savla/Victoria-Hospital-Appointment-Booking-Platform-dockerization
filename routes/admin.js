const express = require('express');
const path = require('path');
const router = express.Router();
const isAdmin = require('../middleware/isAdmin');
const Appointment = require('../models/Appointment');
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

    io.emit('appointment:cancelled', appointment);

    res.send('Cancelled');
  } catch {
    res.status(500).send('Error cancelling appointment');
  }
});


router.post('/reschedule/:id', async (req, res) => {
  const io = req.app.get('io');
  const { newDate, newTime } = req.body;

  try {
    const appointment = await Appointment.findByIdAndUpdate(
      req.params.id,
      {
        date: newDate,
        time: newTime,
        status: 'rescheduled'
      },
      { new: true }
    );

    io.emit('appointment:rescheduled', appointment);

    res.send('Rescheduled');
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
