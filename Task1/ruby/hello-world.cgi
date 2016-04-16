#!/usr/bin/env ruby

colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
puts Time.now.strftime('%Y%m%d%H%M%S%L')
print "Content-Type: text/html \n\n" 
print '<html><head>'
print "<meta charset='UTF-8'>"
print '<title>Hello World Ruby</title></head>'
print "<body style='background-color:#{colors.sample}'>"
print "<h2>Hello World from Ruby @ #{Time.new.inspect}</h2>"
print '</body>'
print '</html>'
