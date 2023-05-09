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
        <form action="2Display.php"  method="post">
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