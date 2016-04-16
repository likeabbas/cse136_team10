#!/usr/bin/ruby

print "Content-Type: text/html\n\n"
print "<html><head>"
print "<title>Get vs Post Ruby</title></head>"
print "<bordy>"
print "<form action ='processdata.cgi' method = 'get'>"
print "<h1>Get Form:</h1>">
print "<br/>"
print "<input type='text' name='username' placeholder='Username' required='true'>"
print "<input type ='password' name= 'userpassword' placeholder='Password' required='true'>"
print "<input type='number' name='magicnumber' placeholder='Magic Number' required='true'>"
print "<input type='submit' value='Submit'>"
print "</form>"

print "<form action ='processdata.cgi' method = 'post'>"
print "<h1>Post Form:</h1>"
print "<br/>"
print "<input type='text' name='username' placeholder='Username' required='true'>"
print "<input type ='password' name= 'userpassword' placeholder='Password' required='true'>"
print "<input type='number' name='magicnumber' placeholder='Magic Number' required='true'>"
print "<input type='submit' value='Submit'>"
print "</form>"
print "</body>"
print "</html>"

