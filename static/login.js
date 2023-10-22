let regsiter =document.getElementById('registrationform');
let login =document.getElementById('loginform');
let rbtn =document.getElementById('changebtn1');
let lbtn =document.getElementById('changebtn2');

regsiter.style.display='none';
lbtn.style.display='none';

function registration(){
    regsiter.style.display='block';
    lbtn.style.display='block';
    login.style.display='none';
    rbtn.style.display='none';
    document.getElementById('para').innerHTML='I have already an account';
    document.getElementById('head').innerHTML='Registration';
    
}

function lgfunc(){
    login.style.display='block';
    rbtn.style.display='block';
    regsiter.style.display='none';
    lbtn.style.display='none';
    document.getElementById('para').innerHTML='I dont have an account';
    document.getElementById('head').innerHTML='Login';
}