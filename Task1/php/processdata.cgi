#!/usr/bin/env php
<?php
echo("Content-Type: text/html\n\n");
echo('<html><head>
	<title>Process Data in PHP</title>
</head>
<body>');

	if (isset($_GET['username']) && isset($_GET['userpassword']) && isset($_GET['magicnumber'])){
		$num = $_GET['magicnumber'];
		$name = $_GET['username'];
		$pw = $_GET['userpassword'];
		
		for($k = 1; $k<=$num ; $k++){
		$res = "Hello ".$name." with a password of ".$pw ."!";
		echo $res;
		echo "<br/>";
		}
	}
	else{
		if (isset($_POST['username']) && isset($_POST['userpassword']) && isset($_POST['magicnumber'])){
		$num = $_POST['magicnumber'];
		$name = $_POST['username'];
		$pw = $_POST['userpassword'];
		
			for($k = 1; $k<=$num ; $k++){
			$res = "Hello ".$name." with a password of ".$pw ."!";
			echo $res;
			echo "<br/>";
			}
		}
		else{
			echo "The form has not been filled up properly.";
		}
	}
echo('</body>
</html>');
?>
