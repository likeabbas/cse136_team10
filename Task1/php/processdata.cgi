#!/usr/bin/env php
<?php
echo("Content-Type: text/html\n\n");
echo('<html><head>
	<title>Process Data in PHP</title>
</head>
<body>');
echo "test<br/>";
echo $_ENV['REQUEST_METHOD'];
echo "<br/>";
echo htmlspecialchars($_GET['username']);
echo $_GET['password'];
echo $_GET['magicnumber'];
echo $_POST['username'];
echo $_POST['password'];
echo $_POST['magicnumber'];
	if (isset($_GET['username']) && isset($_GET['password']) && isset($_GET['magicnumber'])){
		echo "test get";
		$num = $_GET['magicnumber'];
		$name = $_GET['username'];
		$pw = $_GET['password'];
		$res = "Hello ".$name." with a password of ".$pw."!";
			for($k = 1; $k<=$num ; $k++){
				echo "test for get";
			echo $res;
			echo "<br/>";
			}
	}
	else{
		if (isset($_POST['username']) && isset($_POST['password']) && isset($_POST['magicnumber'])){
		echo "test post";
		$num = $_POST['magicnumber'];
		$name = $_POST['username'];
		$pw = $_POST['password'];
		$res = "Hello ".$name." with a password of ".$pw."!";
			for($k = 1; $k<=$num ; $k++){
			echo "test for post";
			echo $res;
			echo "<br/>";
			}
		}
		else{
			echo "The form has not been filled up properly.";
		}
	}
echo("</body></html>");
?>
