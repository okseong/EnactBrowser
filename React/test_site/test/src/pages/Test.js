import React, { Component, useState, useEffect, Fragment } from 'react';
import { BrowserRouter as Router, Route, Link, Switch } from 'react-router-dom';
import IframeComm from 'react-iframe-comm'
import Webcam from "react-webcam";

 
const WebcamComponent = () => <Webcam />;
 

  
function Test() {
  const [id, setId] = useState("");
  const [pw, setPw] = useState("");
  const [text, setText] = useState("dd");
  const sendmessage=()=>{
    var frameWindow = document.getElementById('frame').contentWindow;
    frameWindow.postMessage("parent에서 보냄", '*');
    var childDocument = frameWindow.document
    // var childDocument = window.child.document
    childDocument.createElement("div")
    var newDiv = childDocument.createElement("button"); 
    newDiv.textContent="parent에서 만든 버튼"
    newDiv.id="fromparent"
    childDocument.body.appendChild(newDiv); 
    
  }
  const submit=()=>{
    var frameWindow = document.getElementById('frame').contentWindow;
    frameWindow.postMessage("아이디:"+id+" 비밀번호:"+pw, '*');
  }
  function readTextFile(file)
{
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    console.log(rawFile)
    rawFile.onreadystatechange = function ()
    {
        if(rawFile.readyState === 4)
        {
          console.log("dsadsadsadasdsadasd")
            if(rawFile.status === 200 || rawFile.status == 0)
            {
                var allText = rawFile.responseText;
                console.log(allText)
                alert(allText);
            }
        }
    }
    rawFile.onreadystatechange()
    rawFile.send(null);
}
 //window.showOpenFilePicker()
 window.close()

  //var read = readTextFile("file:///C:/aa.txt");

  useEffect(() => {
    //var read = readTextFile("file:///C:/aa.txt");
    setText("awdsdawda")
    console.log("dd")
    window.addEventListener('message', function (evt) { 
      console.log(evt.data)
      if (evt.origin.indexOf('http://localhost:3001/') == 0) {
        console.log(evt.data);
      }
    });
    return () => {
        console.log('컴포넌트가 화면에서 사라짐');
    };
}, []);

// useEffect(() => {
//   setText("fgfgfdhdfhh")
//   console.log("dd")
//   window.addEventListener('message', function (evt) { 
//     console.log(evt.data)
//     if (evt.origin.indexOf('http://localhost:3001/') == 0) {
//       console.log(evt.data);
//     }
//   });
//   return () => {
//       console.log('컴포넌트가 화면에서 사라짐');
//   };
// }, [text]);
console.log(document.cookie)


  return (
    <div style={{margin:'0 auto', textAlign:'center'}}>
      부모 사이트(http://localhost://3000)
      <br/>
      <button className="sendbtn" id="sendbtn" onClick={sendmessage}>iframe child에게 정보 전송</button>
      <br/>
      <p id='test'/>
      <input className="inputbox" id="id" placeholder="아이디를 입력해주세요" onChange={(e)=>{setId(e.target.value)}}/>
      <br/>
      <input className="inputbox" id="password" placeholder="비밀번호를 입력해주세요" onChange={(e)=>{setPw(e.target.value)}} />
      <br/>
      <button className="loginbtn" type="submit" id="submit" onClick={submit}>로그인</button>
      <br/>
      <br/>  <br/>  <br/>
      <iframe id="frame" style={{ border:'10px #222222 solid',width: '300px', height: '300px' }} src="http://localhost:3001/">
      </iframe><br/>
    </div>
  );
}

export default Test;
