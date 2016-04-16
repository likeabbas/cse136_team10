
#!/usr/bin/ruby

print "Content-Type: text/html charset=UTF8 \n\n"
puts "<!DOCTYPE html>"
print "<html><head>"
print "<meta charset=\"UTF-8\">"
print '<title></title></head>'

print "<form action ="processdata.cgi" method = "get">"
print "Get Form:"
print "<br>"
print "<input type="text" name="username" placeholder="Username">"
print "<input type ="password" name= "userpassword" placeholder="Password">"
print "<input type="number" name="magicnumber" placeholder="Magic Number">"
print "<input type="submit" value="Submit">"
print "</form>"

print "<form action ="processdata.cgi" method = "post">"
print "Post Form:"
print "<br>"
print "<input type="text" name="username" placeholder="Username">"
print "<input type= "password" name="userpassword" placeholder="Password" >"
print "<input type="number" name="magicnumber" placeholder="Magic Number">"
print " <input type="submit" value="Submit"> "
print "</form>"

print"</html>"

