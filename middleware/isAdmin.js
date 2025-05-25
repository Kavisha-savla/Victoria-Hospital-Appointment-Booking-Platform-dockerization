function isAdmin(req, res, next) {
  console.log('Checking session:', req.session.user);
  if (req.session?.user?.role === 'admin') {
    return next();
  } else {
    return res.redirect('/admin/login');
  }
}
module.exports = isAdmin;
