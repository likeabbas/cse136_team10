#!/usr/bin/ruby

require 'cgi'
cgi = CGI.new
userName = cgi['username']
userPassword = cgi['userpassword']
magicNumber = cgi['magicnumber']

puts cgi.header("type" => "text/html", "cache_control" => "no-cache, no-store")

for i in 0..5-1
	puts "<h2>Hello with a username of #{userName} with a password of #{userPassword}!</h2>"
end