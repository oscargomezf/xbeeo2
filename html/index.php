<?php
	if (isset($_POST['RL1_ON'])) {
		$result=exec("sudo resources/xbeeo2 -o 0 -m 1");
	} else if (isset($_POST['RL1_OFF'])) {
		$result=exec("sudo resources/xbeeo2 -o 0 -m 0");
	} else if (isset($_POST['RL2_ON'])) {
		$result=exec("sudo resources/xbeeo2 -o 1 -m 1");
	} else if (isset($_POST['RL2_OFF'])) {
		$result=exec("sudo resources/xbeeo2 -o 1 -m 0");
	} 
?>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	<title>XBeeO2 v1.0</title>
	<link href="resources/xbeeo2_style.css" rel="stylesheet" type="text/css">
<body>
<div class="main_wrapper">
    <div id="wrapper">
		<section id="content" class="clearfix">
			<article class="widecolumn">
			<form method="post">
				<div class="container" >
			    	<h2>XBeeO2 v1.0</h2>
					<div class="subContainer clearfix">
			        	<ul class="formData suggestion_form" id="Suggestion_form">
			           	<li>
			           		<input name="RL1_ON" type="submit" value="ON" class="button" />
			           	</li>
			            <li>
			            	<input name="RL1_OFF" type="submit" value="OFF" class="button" />
			            </li>
			            </ul>
			        </div>
			        <h2>Relay 1</h2>
			        <div class="subContainer clearfix">
			        	<ul class="formData suggestion_form" id="Suggestion_form">
			           	<li>
			           		<input name="RL2_ON" type="submit" value="ON" class="button" />
			           	</li>
			            <li>
			            	<input name="RL2_OFF" type="submit" value="OFF" class="button" />
			            </li>
			            </ul>
			            </form>
			        </div>
			        <h2>Relay 2</h2>
		    	</div>
			</article>
		</form>
		</section>
		<footer><div class="footer_contianer">© 2014 www.oscargomezf.com </div></footer>
    </div>
</div>
</body>
</html>