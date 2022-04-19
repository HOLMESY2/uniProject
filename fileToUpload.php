
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>PHP File Upload</title>
    <link rel="stylesheet" href="style.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lato&display=swap" rel="stylesheet">
    <style>
        .container{
    padding: 0;
margin: 0;
list-style: none;
display: flex;
width: 100%;
height: 200%;
float: right;

   }
   .item{
    width: 50%;
    height: 750px;
    margin: 0;  
      margin-top: 0;
      padding-bottom: -15%;
           }
           .bar{
               width: 100%;
               height: 830px;
           }
           form{
               margin-top: 10%;
               text-align: center;
               font-family: "Lato", sans-serif;
               font-size: 1.5em;
           }
           img{
               margin-left: 5%;
           }
           input{
            font-family: "Lato", sans-serif;
               font-size: 1em;
           }
    </style>
</head>
<body>
<div id="mySidenav" class="sidenav">
          <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
          <a href="home.html">Home</a>
          <a href="activity.html">Activity Segment</a>
          <a href="places.html">Places Visited</a>
          <a href="graph_manual.html">User Manual</a>
          <a href="http://localhost:3000/fileToUpload.php">User Upload</a>
        </div>
        
        <div id="main">
          
          <span style="font-size:30px;cursor:pointer" onclick="openNav()">&#9776; </span>
        
          <div>          <img src="images/maps.png" alt="">
</div></div>
        
        <script>
        function openNav() {
          document.getElementById("mySidenav").style.width = "250px";
          document.getElementById("main").style.marginLeft = "250px";
        }
        
        function closeNav() {
          document.getElementById("mySidenav").style.width = "0";
          document.getElementById("main").style.marginLeft= "0";
        }
        </script>
       
      <header><h1>EXTRACTING JSON DATA<br class="SUBHEADING"></h1>
        <h3>USING PYTHON TO EXTRACT THE DATA FROM A GOOGLE TAKEOUT JSON FILE </h3>
           
            </header>
    <form action="upload.php" method="post" enctype="multipart/form-data">
        Upload a File:
        <input type="file" name="the_file" id="fileToUpload">
        <input type="submit" name="submit" value="Start Upload">
    </form>

    <ul class="container">
        <object  class="item"data="activity_index_upload\index1.html" type="text/html"></object>
        <object class="item" data="activity_index_upload\index2.html" type="text/html"></object>
    </ul> <ul class="container">
        <object  class="item"data="activity_index_upload\index3.html" type="text/html"></object>
        <object class="item" data="activity_index_upload\index4.html" type="text/html"></object>
    </ul>
    <ul class="container">
    
        <object class="item" data="activity_index_upload\index5.html" type="text/html"></object>
        <object  class="item"data="activity_index_upload\index6.html" type="text/html"></object>
    </ul>
    <img src="activity_index_upload\index7.png" alt="">
    <img src="activity_index_upload\index8.png" alt="">
    <img src="activity_index_upload\index10.png" alt="">

    

    
</html>


