<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Variables in PHP</title>
</head>
<body>
	<h2>Environment variables reached out using PHP</h2>
	<br/>
		<h3>Browser and Server variables</h3>
			<?php
			sort($_SERVER);
			$res = '<table border=1>';
			foreach ($_SERVER as $var){
		    //commandes
				if ($var!=""){
				$res.='<tr><td>'.$var.'</td></tr>';	
				$res.='<tr><td>'.$var[0].'</td></tr>';	
				}
			//echo $_SERVER['name']." : ".$var.'<br/>';//['DOCUMENT_ROOT'];
			}
			$res.='</table>';
			echo $res;
			?>
		
	</div>

</body>
</html>