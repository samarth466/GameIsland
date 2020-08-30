function UncheckAll() {
  const w = document.getElementsByTagName('input');
  for(var i = 0; i < w.length; i++){
    if(w[i].type==='button'){
      w[i].checked = false;
    }
  }
}
window.onload = UncheckAll();
const buttons = document.getElementsByClassName('button')
function RedirectUser(){
  const domain = "http://127.0.0.1:8000/"
  for(var i = 0; i < buttons.length; i++){
    var button = buttons[i]
    if(button.click===true){
      switch(button.name){
        case "view":
          window.location.replace(`${domain}settings/settings/`)
        case "light color":
          window.location.replace(`${domain}settings/edit_settings/light_color/`)
        case "dark color":
          window.location.replace(`${domain}settings/edit_settings/dark_color/`)
        case "use NumPad keys for navigation":
          window.location.replace(`${domain}settings/edit_settings/use_numpad_for_movement/`)
        case "voice assistant":
          window.location.replace(`${domain}settings/edit_settings/voice_assignment/`)
      }
    }
  }
}
for(var i = 0; i<buttons.length;i++){
  buttons[i].onclick = RedirectUser()
}