#!/usr/bin/env php
<?php
echo("Content-Type: text/html\n\n");
echo('<html><head>
	<title>Process Data in PHP</title>
</head>
<body>');

function convertFromQS($queryString){


}
$method = $_SERVER['REQUEST_METHOD'];

if ($method=="GET"){
	$qr = $_SERVER['QUERY_STRING'];
	$qrexplode = explode("&", $qr);
	$coupleUser = $qrexplode[0];
	$name = explode("=",$coupleUser)[1];
	$couplePassword = $qrexplode[1];
	$pw = explode("=", $couplePassword)[1];
	$coupleNumber = $qrexplode[2];
	$num = explode("=",$coupleNumber)[1];
	if ($name!="" && $num!="" && $pw!=""){
	//	echo "test get";
	//	$num = $_GET['magicnumber'];
	//	$name = $_GET['username'];
	//	$pw = $_GET['password'];
		$res = "Hello ".$name." with a password of ".$pw."!";
			for($k = 1; $k<=$num ; $k++){
			echo "<h2>".$res."</h2>";
			echo "<br/>";
			}
	}
	else{
		echo "The form GET has not been filled up properly.";
	}
}
else{
	if($method=="POST"){
		$entityBody = stream_get_contents(STDIN);
		echo $entityBody;
		$array = explode($entityBody, "&");
		$formUser = $array[0];
		$formPw = $array[1];
		$formNum = $array[2];

		$name = explode("=",$formUser)[1];
		$pw = explode("=", $formPw)[1];
		$num = explode("=",$formNum)[1];
		echo $name;
		echo $pw;
		echo $num;
		if ($name != "" && $num != "" && $pw!= ""){
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
			echo "The form POST has not been filled up properly.";
		}
	}
}
echo("</body></html>");
?>
