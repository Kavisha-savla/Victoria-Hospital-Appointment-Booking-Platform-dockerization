function isAdmin(req, res, next) {
  if (req.session?.user?.role === 'admin') {
    return next(); // Allow access
  } else {
    return res.redirect('/admin/login'); // Block access
  }
}
module.exports = isAdmin;
