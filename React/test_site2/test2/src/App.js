import logo from './logo.svg';
import './App.css';
import React, { Component, useState, useEffect, Fragment } from 'react';
function App() {
  const [text, setText] = useState("");
  const [idpw, setIdpw] = useState("");
  const [domResult, setDomResult] = useState('');
  const [domResult2, setDomResult2] = useState('');
  const [cookieResult, setCookieResult] = useState('');
  const [cookieResult2, setCookieResult2] = useState('');
  const [xmlResult, setXmlResult] = useState('');
  const [xmlResult2, setXmlResult2] = useState('');
  const [xssResult, setXssResult] = useState('');
  function testfunction(){
    alert("해킹!");
  }
  const dom_child_to_parent =() =>{
    try{
      var parentDocument = window.parent.document
      setDomResult(true)
    }
    catch{
      setDomResult(false)
    }
  }
  const getData=()=>{
    var request = new XMLHttpRequest();
    console.log("Inside getData method");
    request.onreadystatechange = function() {
       if (this.readyState == 4 && this.status == 200) {
           setXmlResult(true)
           console.log(this.responseText);
       }else{
         setXmlResult(false)
       }
    };
    request.open('GET', 'https://enactparent.web.app', true);
    request.send();
    console.log(request.responseText);
  }

  const cookie_child_to_parent =() =>{
    try{
      var parentDocument = window.parent.document
      var parnetCookie = parentDocument.cookie
      setCookieResult(true)
    }
    catch{
      setCookieResult(false)
    }
  }
  
  const sendparent_newElement =() =>{
    try{
    var parentDocument = window.parent.document
    parentDocument.createElement("div")
    window.parent.postMessage("ddd","*");
    var newDiv = parentDocument.createElement("button"); 
    newDiv.textContent="child에서 만든 버튼"
    newDiv.id="fromchild"
    // parentDocument.body.innerHTML="<script>alert('child에서 보낸 알람');</script>"
    // console.log(newDiv)
    parentDocument.body.appendChild(newDiv); 
  }catch(e){
    console.log(e)

  }
  }

  const sendparent_alert =() =>{
    var parentDocument = window.parent.document
    console.log(parentDocument.body.innerHTML=`<img src="empty.gif" onerror="alert('test');this.parentNode.removeChild(this);"/>`)
  }


    useEffect(() => {
      try{
  let start = new Date();
    window.addEventListener('message', function(evt) {
      console.log(window.parent.document.location)
      var parentElement = window.parent.document.getElementById('sendbtn')
      if (evt.origin === 'https://enactparent.web.app') {
        console.log(evt.data); 
        setText(evt.data)
        window.parent.postMessage("응답", '*');
      }
    
  });    


    return () => {
        console.log('컴포넌트가 화면에서 사라짐');
    };}catch{}
}, []);
//window.location.reload()
    
const xss_child_to_parent =() =>{
  try{
    var parentDocument = window.parent.document
    parentDocument.createElement("div")
    window.parent.postMessage("ddd","*");
    var newDiv = parentDocument.createElement("button"); 
    newDiv.textContent="child에서 만든 버튼"
    newDiv.id="fromchild"
    // console.log(newDiv)
    parentDocument.body.appendChild(newDiv)
    setXssResult(true)
  }
  catch(e){
    console.log(e)
    setXssResult(false)
  }
}
// Send a message to the frame's window

  return (
    <div className="childhome">
      자식사이트 <br/>
      <br/>
      <button className="homebutton" id="child_dom" onClick={()=>dom_child_to_parent()}>자식에서 부모 DOM 접근</button> {domResult===false && <p className="result">통과</p>}{domResult && <p className="result2">실패</p>}{domResult==='' && <p className="result"></p>}<br/>
      {/* <button className="homebutton">자식에서 부모 DOM 접근</button>{domResult2 && <p className="result">통과</p>}{domResult2===false && <p className="result2">실패</p>}{domResult2==='' && <p className="result"></p>}<br/> */}
      <p className="category">XMLHttpRequest 관련</p>
      <button className="homebutton" id="child_xml" onClick={()=>getData()}  > 자식에서 부모로 XMLHttpRequest 요청</button>{xmlResult ===false && <p className="result">통과</p>}{xmlResult && <p className="result2">실패</p>}{xmlResult==='' && <p className="result"></p>}<br/>
      {/* <button className="homebutton">자식에서 부모에게 XMLHttpRequest 요청</button><p className="result">통과</p><br/> */}
      <p className="category">쿠키 관련</p>
      <button className="homebutton" id="child_cookie" onClick={()=>cookie_child_to_parent()}>자식에서 부모의 쿠키 접근</button>{cookieResult ===false && <p className="result">통과</p>}{cookieResult && <p className="result2">실패</p>}{cookieResult==='' && <p className="result"></p>}<br/>
      {/* <button className="homebutton">자식에서 부모의 쿠키 접근</button><p className="result">통과</p><br/> */}
      <p className="category">XSS 공격</p>
      {/* <button className="homebutton">자식에서 부모로 XSS 공격</button><p className="result">통과</p><br/> */}
      <button className="homebutton" id="child_xss" onClick={()=>xss_child_to_parent()}>자식에서 부모로 XSS 공격</button>{xssResult ===false && <p className="result">통과</p>}{xssResult && <p className="result2">실패</p>}{xssResult==='' && <p className="result"></p>}<br/>
      {text}
      <br/>
    </div>
  );
}

export default App;
