<?php
    $name = $_POST['name'];
    $email= $_POST['email'];
    $number = $_POST['number'];
    $address = $_POST['address'];
    $password = $_POST['password']; 
    $dob = $_POST['dob']; 
    $course = $_POST['course']; 

    echo "<h3> Entered Name: </h3>".$name;
    echo "<h3>Birthday: </h3>".$dob;
    echo "<h3>Entered Email: </h3>".$email;
    echo "<h3>Whatsapp Number: </h3>".$number;
    echo "<h3>Address: </h3>".$address;
    echo "<h3>Course: </h3>".$course;


?>
