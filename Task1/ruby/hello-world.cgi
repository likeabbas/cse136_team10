#!/usr/bin/env ruby

colors = ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "purple", "red", "silver", "teal", "white", "yellow"]
col = {colors.sample}
print col
#print '<br/>'
#if(col=='black' || col=='navy' || col=='purple' || col=='red')
#   print "<style>body{background-color: #{colors.sample} ; color:white;}</style>"
#else
#  print "<style>body{background-color: #{colors.sample};}</style>"
#end
print "Content-Type: text/html \n\n" 
print '<html><head>'
print "<meta charset='UTF-8'>"
print '<title>Hello World Ruby</title></head>'
print "<body style='background-color:#{colors.sample}'>"
print "<h2>Hello World from Ruby @ #{Time.new.inspect}</h2>"
print '</body>'
print '</html>'
