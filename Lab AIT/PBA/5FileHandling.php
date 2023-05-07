<?php
    // Read data from file1.txt 
    $file = fopen("file1.txt", "r");
    $file1_content = fread($file, filesize("file1.txt"));
    fclose($file);



    // Write file1 content to file2.txt
    $file = fopen("file2.txt", "w");
    fwrite($file, $file1_content);
    fclose($file);
?>