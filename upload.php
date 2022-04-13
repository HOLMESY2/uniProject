<?php
    $currentDirectory = getcwd();
    $uploadDirectory = "/uploads/";

    $errors = []; // Store errors here

    $fileExtensionsAllowed = ['json']; // These will be the only file extensions allowed 

    $fileName = $_FILES['the_file']['name'];
    $fileSize = $_FILES['the_file']['size'];
    $fileTmpName  = $_FILES['the_file']['tmp_name'];
    $fileType = $_FILES['the_file']['type'];
    $fileExtension = (end(explode('.',$fileName)));
    $file_name = 'newUpload'; // New unique file name
    move_uploaded_file($_FILES["the_file"]["tmp_name"], "uploads/{$file_name}.json");
    $uploadPath = $currentDirectory . $uploadDirectory . basename($fileName); 

    
    if (isset($_POST['submit'])) {

      if (! in_array($fileExtension,$fileExtensionsAllowed)) {
        $errors[] = "This file extension is not allowed. Please upload a JPEG or PNG file";
      }

      if ($fileSize > 4000000) {
        $errors[] = "File exceeds maximum size (4MB)";
      }
     

      if (empty($errors)) {
        $didUpload = move_uploaded_file($fileTmpName, $uploadPath);
       
      

        if ($didUpload) {
          echo "The file " . basename($fileName) . " has been uploaded";
        } 
        }
      } else {
        foreach ($errors as $error) {
          echo $error . "These are the errors" . "\n";
        }
      }

    
    echo "</br>";
    echo "<a href=fileToUpload.php>back to upload</a>"
?>