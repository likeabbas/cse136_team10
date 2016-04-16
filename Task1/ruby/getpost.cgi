#!/usr/bin/ruby

require 'cgi'
# cgi = CGI.new
# userName = cgi['username']
# userPassword = cgi['userpassword']
# magicNumber = cgi['magicnumber']
cgi = CGI.new
cgi.out{
   cgi.html{
      cgi.head{ "\n"+cgi.title{"This Is a Test"} } +
      cgi.body{ "\n"+
         cgi.form{"\n"+
            cgi.hr +
            cgi.h1 { "A Form: " } + "\n"+
            cgi.textarea("get_text") +"\n"+
            cgi.br +
            cgi.submit
         }
      }
   }
}




# puts cgi.header("type" => "text/html", "cache_control" => "no-cache, no-store")

# for i in 0..5-1
# 	puts "<h2>Hello with a username of #{userName} with a password of #{userPassword}!</h2>"
# end
