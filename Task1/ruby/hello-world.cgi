#!/usr/bin/env ruby

colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]

print "Content-Type: text/html \n\n" 
print '<html><head>'
print "<meta charset='UTF-8'>"
print '<title>Hello World Ruby</title></head>'
print "<body style='background-color:#{colors.sample}'>"
print Time.now.strftime('%Y%m%d%H%M%S')
print '<br/>'
hours,minutes,seconds,frac = Date.send(:day_fraction_to_time, stop-start)
print hours
print '<br/>'
print minutes
print '<br/>'
print seconds
print '<br/>'
print "<h2>Hello World from Ruby @ #{Time.new.inspect}</h2>"
print '</body>'
print '</html>'
