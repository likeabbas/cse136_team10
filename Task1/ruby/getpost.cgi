
#!/usr/bin/ruby
print "Content-Type: text/html charset=UTF8 \n\n"
puts "<!DOCTYPE html>"
print "<html><head>"
print "<meta charset=\"UTF-8\">"
puts '<title></title></head>'
puts "<body>"
puts "<h1>Get Form:</h1>"
puts "<form action ="processdata.cgi" method = "get">"
puts "<input type="text" name="username" placeholder="Username">"
puts "<input type ="password" name= "userpassword" placeholder="Password">"
puts "<input type="number" name="magicnumber" placeholder="Magic Number">"
puts "<input type="submit" value="Submit">"
puts "</form>"
puts "<h2>Get Form:</h2>"
puts "<form action ="processdata.cgi" method = "post">"
puts "<input type="text" name="username" placeholder="Username">"
puts "<input type= "password" name="userpassword" placeholder="Password" >"
puts "<input type="number" name="magicnumber" placeholder="Magic Number">"
puts " <input type="submit" value="Submit"> "
puts "</form>"
print"</body>\n</html>"

