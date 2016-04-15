#!/usr/bin/env ruby
colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]

print "Content-Type: text/html charset=UTF8 \n\n" 
puts "<!DOCTYPE html>"

print "<html><head>"
print "<meta charset=\"UTF-8\">"

print '<title>Hello World Ruby</title></head>'
puts "<body style = 'background-color: #{colors.sample}'>"

puts "Hello World from Ruby @ #{Time.new.inspect}"

print '</html>'
