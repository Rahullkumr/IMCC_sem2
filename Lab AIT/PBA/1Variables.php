<?php
	$str = "Mathematical Calculator";
	$num1 = 83;
	$num2 = 5;

	$sum = $num1 + $num2;
	$diff = $num1 - $num2;
	$pdt = $num1 * $num2;
	$div = $num1 / $num2;

	echo "<h2>".$str."</h2>";
	echo "<h3>num1 = 83 and num2 = 5";
	echo "<br><br>Sum of ". $num1 . " and " . $num2 ." = ".$sum;
	echo "<br />Difference of ". $num1 . " and " . $num2 ." = ".$diff;
	echo "<br />Product of ". $num1 . " and " . $num2 ." = ".$pdt;
	echo "<br />Division of ". $num1 . " and " . $num2 ." = ".$div;
?>