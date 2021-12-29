// Read 'README.txt' for more info.

function newRow() {

    var table = document.getElementById("table");
    var row = table.insertRow(-1);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    cell1.innerHTML = document.getElementById("cell1").innerHTML
    cell2.innerHTML = document.getElementById("cell2").innerHTML
    cell3.innerHTML = document.getElementById("cell3").innerHTML

}

function remove_row() {
    var table = document.getElementById("table")
    if (table.rows.length >= 3) {
        table.deleteRow(-1)
    }
}

function tableBorder() {
    document.getElementById("table").style.backgroundColor = document.getElementById("tableBorder").value
}

function pageBackground() {
    document.body.style.backgroundColor = document.getElementById("pageBack").value
}

function titleText() {
    document.getElementById("title").style.color = document.getElementById("titleColour").value
}

function changeTitleText() {
    text = document.getElementById("titleText")
    title = document.getElementById("title")
    if (text.style.display === "none") {
        text.style.display = "block"
        title.style.display = "none"
        text.value = title.innerHTML
    } else {
        text.style.display = "none"
        title.style.display = "block"
        title.innerHTML = text.value
    }
}
