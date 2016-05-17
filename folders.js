var db = require('./db');

module.exports.add = function(req, res) {
  res.render('folders/addFolder.ejs');
};

module.exports.insert = function(req, res) {
  var user = req.session.user;

  if (req.body.title === "\s") {
    res.render("/error", {errorType: form});
  }

  var query = 'INSERT INTO folder (name, username) VALUES (' + db.escape(req.body.title) + ', ' + db.escape(user) + ')';
  db.query(query, function(err){
    if (err) throw err;
    res.redirect('/bookmarks');
  });
}