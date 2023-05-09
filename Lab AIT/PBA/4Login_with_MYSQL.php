<?php
    $servername = "localhost";
    $username = "root";
    $pwd = "";
    $dbname = "student";


    if(isset($_REQUEST["loginPressed"])){

        $email = $_REQUEST['email'];
        $password = $_REQUEST['password'];

        //  Database connection
        $conn = mysqli_connect($servername, $username, $pwd, $dbname);
        //  die if connection was not successful
        if(!$conn){
            die("Sorry connection failed: ".mysqli_connect_error());
        }
 

        $sqlcommand = "select * from registration where email= '$email' AND Password='$password'";


        if($result = mysqli_query($conn, $sqlcommand)){
            $num = mysqli_fetch_array($result);

            if($num){
                echo '<script language="javascript">';
                echo 'alert("Login successful")';
                echo '</script>';
                echo $email;
                exit;
            }
            else{
                echo '<script language="javascript">';
                echo 'alert("Wrong Credentials")';
                echo '</script>';
            }

        }

    }
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Student Login</title>
        <style>
            form{
                border: 2px solid red;
                width: 300px;   height: 230px;
                background-color: lightblue;
            }
            .submit{
                
                font-weight: bold;
            }
            input{
                height: 30px;   width: 60%;
            }
        </style>
    </head>
    <body><center>
        <form action="4Login_with_MYSQL.php"  method="post">
            <h2>Student Login</h2>
            <input type="email" name="email" placeholder="Email Address" required><br><br>
            <input type="password" name="password" placeholder="8 Characters Password" required><br><br>
            <input type="submit" name="loginPressed" value="Login"><br>
        </form>
    </body>
</html>