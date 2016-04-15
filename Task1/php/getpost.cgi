#!/usr/bin/env php
<?php
echo("Content-Type: text/plain\n\n");
echo("<html><head><title>Get vs Post methods in forms PHP</title>
</head><body>");
echo("<h1>GET Form</h1>");
echo("<form action='processdata.cgi' method='get'>
<input type='text' name='username' placeholder='Username'>
<input type='password' name='password' placeholder='Password'>
<input type='number' name='magicnumber' placeholder='Magic Number'>
<input type='submit' value='Submit">
</form>");

echo("<h1>Post Form</h1>");
echo("<form action='processdata.cgi' method='get'>
<input type='text' name='username' placeholder='Username'>
<input type='password' name='password' placeholder='Password'>
<input type='number' name='magicnumber' placeholder='Magic Number'>
<input type='submit' value='Submit">
</form>");
echo("</body></html>");
?>
