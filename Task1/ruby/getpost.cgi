#!/usr/bin/ruby

require 'cgi'
# cgi = CGI.new
# userName = cgi['username']
# userPassword = cgi['userpassword']
# magicNumber = cgi['magicnumber']
cgi = CGI.new("html5")
cgi.out{
   cgi.html{
      cgi.head{ "\n"+cgi.title{"This Is a Test"} } +
      cgi.body{ "\n"+
         cgi.form{"\n"+
            cgi.hr +
            cgi.h1 { "Get Form: " } + "\n"+
            cgi.text_field("username") +
            cgi.password_field("userpassword") +"\n"+
            cgi.br +
            cgi.submit
         }
         cgi.form{"\n"+
            cgi.hr +
            cgi.h1 { "Post Form: " } + "\n"+
            cgi.password_field("userpassword") +"\n"+
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
