#!/usr/bin/env php
<?php
echo('Content-Type: text/plain\n\n');
echo('<html>');
echo('<head>
	<meta charset="utf-8">
    	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Hello World in PHP</title>
	</head>');

$color = array('aqua', 'black', 'blue', 'fuchsia', 'gray', 'green', 'lime', 'maroon', 'navy', 'olive', 'purple', 'red', 'silver', 'teal', 'white',  'yellow');
$rd = floor(rand(0,17));
echo('<style>
	body{background-color:'.$color[$rd].'};
	</style>');
date_default_timezone_set('America/Los_Angeles');
$date = date('m/d/Y h:i:s a', time());
$res = "Hello World from PHP @ ".$date;
echo("<body>");
echo('<h1>'.$res.'</h1>');
echo('</body></html>');
?>
