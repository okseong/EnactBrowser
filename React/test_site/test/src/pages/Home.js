import './Home.css'
import React, { Component, useState, useEffect, Fragment } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import IframeComm from 'react-iframe-comm'
import Webcam from "react-webcam";

 
const WebcamComponent = () => <Webcam />;
 

  
function Home() {
  const [id, setId] = useState("");
  const [pw, setPw] = useState("");
  const [text, setText] = useState("dd");
  const [domResult, setDomResult] = useState('');
  const [domResult2, setDomResult2] = useState('');
  const [cookieResult, setCookieResult] = useState('');
  const [cookieResult2, setCookieResult2] = useState('');
  const [xmlResult, setXmlResult] = useState('');
  const [xssResult, setXssResult] = useState('');
  const [xmlResult2, setXmlResult2] = useState('');


  const reloadIframe = () =>{
    document.getElementById('frame').src = document.getElementById('frame').src
  }

  const sendmessage=()=>{
    try{
    var frameWindow = document.getElementById('frame').contentWindow;
    frameWindow.postMessage("parent에서 보냄", '*');
    var childDocument = frameWindow.document
    console.log(childDocument.cookie)
    // var childDocument = window.child.document
    childDocument.createElement("div")
    var newDiv = childDocument.createElement("button"); 
    newDiv.textContent="parent에서 만든 버튼"
    newDiv.id="fromparent"
    childDocument.body.appendChild(newDiv); 
  }catch(e){
      console.error(e)
      document.getElementById('frame').src = document.getElementById('frame').src
    }
    
  }


  const submit=()=>{
    var frameWindow = document.getElementById('frame').contentWindow;
    frameWindow.postMessage("아이디:"+id+" 비밀번호:"+pw, '*');
  }


  useEffect(() => {
    try{
    window.addEventListener('message', function (evt) { 
      if (evt.origin.indexOf('https://enactchild.web.app') == 0) {
        setDomResult2(true)
        console.log(evt.data);
      }else{
        console.log('aa')
        setDomResult2(false)
      }
    });
  }catch(e){
    console.log(e)
    setDomResult2(false)
  }
    console.log(xmlResult)
    return () => {
        console.log('컴포넌트가 화면에서 사라짐');
    };
}, []);


const dom_parent_to_child =() =>{
  try{
    var frameWindow = document.getElementById('frame').contentWindow;
    var childDocument = frameWindow.document
    setDomResult(true)
  }
  catch(e){
    console.log(e)
    setDomResult(false)
  }
}

const cookie_parent_to_child =() =>{
  try{
    var frameWindow = document.getElementById('frame').contentWindow;
    var childDocument = frameWindow.document
    var childCookie = childDocument.cookie
    setCookieResult(true)
  }
  catch(e){
    console.log(e)
    // document.getElementById('frame').src = document.getElementById('frame').src
    setCookieResult(false)
  }
}

const xss_parent_to_child =() =>{
  try{
    var frameWindow = document.getElementById('frame').contentWindow;
    var childDocument = frameWindow.document
    childDocument.createElement("div")
    var newDiv = childDocument.createElement("button"); 
    newDiv.textContent="parent에서 만든 버튼"
    newDiv.id="fromparent"
    childDocument.body.appendChild(newDiv); 
    // var frameWindow = document.getElementById('frame').contentWindow;
    // var childDocument = frameWindow.document
    // childDocument.body.innerHTML=`<img src="empty.gif" onerror="alert('test');this.parentNode.removeChild(this);"/>`
    setXssResult(true)
    // document.getElementById('frame').src = document.getElementById('frame').src
  }
  catch{
    // document.getElementById('frame').src = document.getElementById('frame').src
    setXssResult(false)
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
      //  document.getElementById('frame').src = document.getElementById('frame').src
     }
  };
  request.open('GET', 'https://enactchild.web.app/', true);
  request.send();
  console.log(request.responseText);
}


  return (
    <Fragment>
      <div style={{margin:'0 auto', textAlign:'center'}}>
      <p className="title">브라우저 보안 취약점 진단 사이트</p>
      <hr/>
      <div>
      부모에서 자식으로의 접근
      <p className="category">DOM 관련</p>
      <button className="homebutton" id="parent_dom" onClick={()=>dom_parent_to_child()}>부모에서 자식 DOM 접근</button> {domResult === false && <p className="result">통과</p>}{domResult && <p className="result2">실패</p>}{domResult==='' && <p className="result"></p>}<br/>
      {/* <button className="homebutton">자식에서 부모 DOM 접근</button>{domResult2 && <p className="result">통과</p>}{domResult2===false && <p className="result2">실패</p>}{domResult2==='' && <p className="result"></p>}<br/> */}
      <p className="category">XMLHttpRequest 관련</p>
  <button className="homebutton" id="parent_xml" onClick={()=>getData()}  > 부모에서 자식으로 XMLHttpRequest 요청</button>{xmlResult === false && <p className="result">통과</p>}{xmlResult && <p className="result2">실패</p>}{xmlResult==='' && <p className="result"></p>}<br/>
      {/* <button className="homebutton">자식에서 부모에게 XMLHttpRequest 요청</button><p className="result">통과</p><br/> */}
      <p className="category">쿠키 관련</p>
  <button className="homebutton" id="parent_cookie" onClick={()=>cookie_parent_to_child()}>부모에서 자식 쿠키 접근</button>{cookieResult === false && <p className="result">통과</p>}{cookieResult && <p className="result2">실패</p>}{cookieResult==='' && <p className="result"></p>}<br/>
      {/* <button className="homebutton">부모에서 자식의 쿠키 접근</button><p className="result">통과</p><br/> */}
      <p className="category">XSS 공격</p>
      <button className="homebutton" id="parent_xss" onClick={()=>xss_parent_to_child()}>부모에서 자식으로 XSS 공격</button>{xssResult === false && <p className="result">통과</p>}{xssResult && <p className="result2">실패</p>}{xssResult==='' && <p className="result"></p>}<br/>
      {/* <button className="homebutton">부모에서 자식으로 XSS 공격</button><p className="result">통과</p><br/> */}
      </div>
      <hr style={{size:"5px"}}/><br/>
    </div>
    <div style={{margin:'0 auto', textAlign:'center'}}>
      자식에서 부모로의 접근<br/><br/><br/>
      <iframe id="frame" style={{ border:'10px #222222 solid',width: '500px', height: '500px' }} src="https://enactchild.web.app/">
      </iframe><br/>
    </div>
    </Fragment>
  );
}

export default Home;
