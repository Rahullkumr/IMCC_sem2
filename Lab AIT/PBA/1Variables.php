<!DOCTYPE html>
<html>
  <head>
    <title>Calculator</title>
  </head>
  <body><center>
    <h1>Basic Calculator</h1>
    <form method="post" action="Calculator.php">
      <input type="number" name="num1" placeholder="Enter Number 1"><br><br>
      <input type="number" name="num2" placeholder="Enter Number 2"><br><br>
      <select name="operator">
        <option>-- Select Operation --</option>
        <option value="+">+</option>
        <option value="-">-</option>
        <option value="*">*</option>
        <option value="/">/</option>
      </select><br><br>
      <button type="submit" name="submit">Calculate</button>
    </form>

    <?php
      if(isset($_POST['submit'])) {
        $num1 = $_POST['num1'];
        $num2 = $_POST['num2'];
        $operator = $_POST['operator'];
        $result = '';

        switch($operator) {
          case '+':
            $result = $num1 + $num2;
            break;
          case '-':
            $result = $num1 - $num2;
            break;
          case '*':
            $result = $num1 * $num2;
            break;
          case '/':
            if ($num2 == 0)
              $result = 'cant divide by 0';
            else
              $result = $num1 / $num2;              
            break;
          default:
            $result = 'Invalid operator';
        }

        echo '<h2>Result: ' . $result . '</h2>';
      }
    ?>

  </body>
</html>
