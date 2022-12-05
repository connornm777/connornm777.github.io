<?php
  $name = $_POST['name'];
  $comment = $_POST['comment'];

  $file = fopen("comments.txt","a");
  fwrite($file,$name . ": " . $comment . "\n");
  fclose($file);
?>

