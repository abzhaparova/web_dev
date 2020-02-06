var cnt=1;
function buttonClick() {
  var text = document.getElementById("userInput").value;
  document.getElementById("userInput").value = "";

  if (text.length > 0) {
    var row = document.getElementById("row");
    var task = document.createElement("div");
    row.appendChild(task);
    task.className = "task";
    task.id = cnt;
    
    //checkbox
    var checkbox = document.createElement("input");
    var checkBoxDiv = document.createElement("div");
    checkbox.className = "checkbox";
    task.appendChild(checkBoxDiv);
    checkBoxDiv.appendChild(checkbox);
    checkbox.type = "checkbox";
    
    checkbox.onclick = function Do() {
    var par = this.parentElement.parentElement.getElementsByClassName("texts")[0].firstChild;
      if (this.checked) {
        par.className = "no";
      } else {
        par.className = "yes";
      }
    };

    // task
    var paragraphDiv = document.createElement("div");
    paragraphDiv.className = "texts";
    var paragraph = document.createElement("paragraph");
    paragraph.className = cnt;
    task.appendChild(paragraphDiv);
    paragraphDiv.appendChild(paragraph);
    paragraph.innerHTML = text;
    paragraph.className = "yes";

    //delete buttn
    var deleteDiv = document.createElement("div");
    var deletes = document.createElement("button");
    deletes.className = "del";
    deletes.innerHTML = "delete";
    task.appendChild(deleteDiv);
    deleteDiv.appendChild(deletes);
    deletes.onclick = function remove() {
      this.parentElement.parentElement.remove();
      alert("are you sure you want to delete?");
    };
    cnt++;
  }
}