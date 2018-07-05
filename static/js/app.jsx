import React from "react";

var socket = io.connect('http://localhost:5000');
socket.on('echo', function(data){
    $('#outputform').val(data.echo);
});

function send(){
    socket.emit('convert', {message : $("#inputform").val()});
}

export default class App extends React.Component {
  render () {
    return (

    <div className="container">
      <div className="row">
        <div className="col d-flex justify-content-center">
          <p>Система конвертации арабских чисел в римские и обратно</p>
        </div>
      </div>
        <div className="row">
          <div className="col d-flex justify-content-left">
            <textarea className="form-control" id="inputform" rows="3" placeholder="Send a message to the server..."></textarea>
          </div>
          <div className="col d-flex justify-content-center">
            <div className="sendbutton">
              <button type="button" className="btn btn-primary" onClick={send}>Convert</button>
            </div>
          </div>
          <div className="col d-flex justify-content-right">
            <textarea className="form-control" id="outputform" rows="3" placeholder="Convertation result..."></textarea>
          </div>
      </div>
    </div>
    )
  }
}
