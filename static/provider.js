var upImage=null;
var grayImage=null;
var rainbowImg=null;
var redImg=null;
var blurImg=null;
var windowImg=null;
var canvas=document.getElementById("can");

function imageIsLoaded(img){
  if (img == null || !img.complete()){
alert("Image Not Ready");
  return false;}
  else{
    return true;
  }
}     

