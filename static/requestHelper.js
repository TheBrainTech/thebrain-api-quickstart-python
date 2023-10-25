
var socket = io.connect('http://' + document.domain + ':' + location.port);

function submitForm(event) {
  event.preventDefault();

  var formData = {
    brainId: document.getElementsByName('brainId')[0].value,
    srcThtId: document.getElementsByName('srcThtId')[0].value,
    thtName: document.getElementsByName('thtName')[0].value,
    thtLabel: document.getElementsByName('thtLabel')[0].value
  };

  socket.emit('submit_form', formData);
}

socket.on('form_response', function(response) {

  var existingMessageDiv = document.getElementById('message');
  if (existingMessageDiv) {
    existingMessageDiv.remove();
  }

  var messageDiv = document.createElement('div');
  messageDiv.id = 'message';
  messageDiv.textContent = response.message;

  if (response.message.startsWith('Success')) {
    messageDiv.className = 'success-message';
  } else {
    messageDiv.className = 'error-message';
  }

  var formElement = document.querySelector('.createThoughtCard');
  formElement.appendChild(messageDiv);
});
