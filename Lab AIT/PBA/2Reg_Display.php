<!DOCTYPE html>
<html>
    <head>
        <title>Student Registration</title>
        <style>
            form{
                border: 2px solid red;
                width: 300px;   height: 510px;
                background-color: lightblue;
            }
            .submit{                
                font-weight: bold;
            }
            select, input{
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
            Birthday: <br><input type="date" name="dob" required><br><br>
            Course: <br>
            <select name="course">
                <option>-- Select --</option>
                <option name="course" value="mba">MBA</option>
                <option name="course" value="mca">MCA</option>
            </select><br><br>
            <input type="number" name="number" placeholder="Whatsapp number" required><br><br>
            <textarea name="address" cols="22" rows="4" placeholder="Present Address" required></textarea><br><br>
            <input type="password" name="password" placeholder="Password" required><br><br>
            <input class="submit" type="submit" name="SubmitClicked"><br>
        </form>
    </body>
</html>
