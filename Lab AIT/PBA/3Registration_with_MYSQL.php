<?php

$servername = "localhost";
$username = "root";
$pwd = "";
$dbname = "student";


//  Database connection
$conn = mysqli_connect($servername, $username, $pwd, $dbname);
//  die if connection was not successful
if(!$conn){
    die("Sorry connection failed: ".mysqli_connect_error());
}


if($_SERVER['REQUEST_METHOD'] == 'POST'){
    $name = $_POST['name'];
    $email= $_POST['email'];
    $number = $_POST['number'];
    $address = $_POST['address'];
    $password = $_POST['password']; 

    echo '<script language="javascript">';
    echo 'alert("Registration successful")';
    echo '</script>';




$sqlcommand = "INSERT INTO `registration` (`Name`, `Email`, `Mobile`, `Address`, `Password`) VALUES ('$name', '$email', '$number', '$address', '$password')";

$result = mysqli_query($conn, $sqlcommand);

}

?>

<!DOCTYPE html>
<html>
    <head>
        <title>Student Registration</title>
        <style>
            form{
                border: 2px solid red;
                width: 300px;   height: 410px;
                background-color: lightblue;
            }
            .submit{                
                font-weight: bold;
            }
            input{
                height: 25px;   width: 60%;
            }
        </style>
        <script>

        </script>
    </head>
    <body><center>
        <form action="3Registration_with_MYSQL.php"  method="post">
            <h2>Student Registration</h2>
            <input type="text" name="name" placeholder="Your Name" required><br><br>
            <input type="email" name="email" placeholder="Email Address" required><br><br>
            <input type="number" name="number" placeholder="Whatsapp number" required><br><br>
            <textarea name="address" cols="22" rows="5" placeholder="Present Address" required></textarea><br><br>
            <input type="password" name="password" placeholder="8 Characters Password" required><br><br>
            <input class="submit" type="submit" name="SubmitClicked"><br>
        </form>
    </body>
</html>