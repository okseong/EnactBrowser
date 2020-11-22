import logo from './logo.svg';
import './App.css';
import React, { Component, useState, useEffect, Fragment } from 'react';
function App() {
  const [text, setText] = useState("");
  const [idpw, setIdpw] = useState("");

  function testfunction(){
    alert("해킹!");
  }

  const sendparent_newElement =() =>{
    var parentDocument = window.parent.document
    parentDocument.createElement("div")
    var newDiv = parentDocument.createElement("button"); 
    newDiv.textContent="child에서 만든 버튼"
    newDiv.id="fromchild"
    // parentDocument.body.innerHTML="<script>alert('child에서 보낸 알람');</script>"
    console.log(newDiv)
    
    parentDocument.body.appendChild(newDiv); 
  }
  const sendparent_alert =() =>{
    var parentDocument = window.parent.document
    console.log(parentDocument.body.innerHTML=`<img src="empty.gif" onerror="alert('test');this.parentNode.removeChild(this);"/>`)
  }
    useEffect(() => {
  let start = new Date();
    window.addEventListener('message', function(evt) {
      console.log(window.parent.document.location)
      var parentElement = window.parent.document.getElementById('sendbtn')
      if (evt.origin === 'http://localhost:3000') {
        console.log(evt.data); 
        setText(evt.data)
        window.parent.postMessage("응답", '*');
      }
  });    

    return () => {
        console.log('컴포넌트가 화면에서 사라짐');
    };
}, []);
//window.location.reload()
    

// Send a message to the frame's window

  return (
    <div className="childhome">
      child 사이트 (http://localhost:3001)
      <br/>
      {text}
      <br/>
      <button id="child_testbtn1"onClick={sendparent_alert}>부모사이트에 script실행</button>
      <button id="child_testbtn2" onClick={sendparent_newElement}>부모사이트에 새로운 element만들기</button>
    </div>
  );
}

export default App;
