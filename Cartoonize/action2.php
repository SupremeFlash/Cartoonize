<?php
require_once 'webcamClass.php';
$webcamClass=new webcamClass();

$imagefile=$webcamClass->showImage();

$output = shell_exec("python cartoonizeoffline.py $imagefile 2>&1");

/*$forecho=array($imagefile=>$output);*/
error_log($output,0);

echo $imagefile;