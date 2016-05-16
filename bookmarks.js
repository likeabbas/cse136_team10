/**
 * Created by abbas on 5/15/16.
 */
var db = require('./db');
var regex = require("regex");

var list = module.exports.list = function(req, res) {
  console.log(req.session.user);
  if (!req.session) res.redirect('/error');
  //if (!req.session.user )
  // add regex to check if user is of type name@email.com
  var user = req.session.user;
  db.query('SELECT * from bookmark where username = ' + db.escape(user), function (err, bookmarks) {
    if (err) throw err;
    // console.log(bookmarks);
    res.render('bookmarks/list.ejs', {bookmarks: bookmarks});
  });
};

module.exports.add = function(req, res) {
  res.render('bookmarks/add.ejs');
};

module.exports.insert = function(req, res){
  if (!req.session) res.redirect('/error');
  var user = req.session.user;

  var title = db.escape(req.body.title);
  var url = db.escape(req.body.url);
  var keywords = db.escape(req.body.keywords);
  var description = db.escape(req.body.description);
  var star = 0;

  var date = new Date();
  date =  date = date.getUTCFullYear() + '-' +
    ('00' + (date.getUTCMonth() + 1)).slice(-2) + '-' +
    ('00' + date.getUTCDate()).slice(-2) + ' ' +
    ('00' + date.getUTCHours()).slice(-2) + ':' +
    ('00' + date.getUTCMinutes()).slice(-2) + ':' +
    ('00' + date.getUTCSeconds()).slice(-2);
  if (req.body.star) star = "on";


  var urlExpression = /[-a-zA-Z0-9@:%_\+.~#?&//=]{2,256}\.[a-z]{2,4}\b(\/[-a-zA-Z0-9@:%_\+.~#?&//=]*)?/gi;
  var urlRegex = new RegExp(urlExpression);
  if (!url.match(urlRegex)) {
    // change all errors to specific ones
    console.log("urlreg");
    res.redirect('/error');
  }
  var keywordExp = /,\s?/;
  // var keywordRegex = new RegExp(keywordExp);
  // if (!keywords.match(keywordRegex)) {
  //   console.log("keywordreg");
  //   res.redirect('/error');
  // }

  var queryString = 'INSERT INTO bookmark (username, title, url, description, star, tag1, tag2, tag3, tag4, creationDate, lastVisit, counter, folder) VALUES (' + db.escape(user) + ', ' + title  + ', '  + url + ', ' + description + ', ' + db.escape(star) + ', ' + 'NULL, ' + 'NULL, ' + 'NULL, ' + 'NULL, ' +  db.escape(date) + ', ' + db.escape(date) + ', ' + db.escape(0) + ', ' + 'NULL' + ')';

  db.query(queryString, function(err){
    if (err) throw err;
    res.redirect('/bookmarks');
  });
};