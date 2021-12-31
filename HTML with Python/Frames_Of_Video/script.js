function resize_w () {
    document.getElementById('img').width = document.getElementById('width').value
    document.getElementById('img').height = document.getElementById('width').value / 1.5
    document.getElementById('height').value = document.getElementById('width').value / 1.5
}
function resize_h () {
    document.getElementById('img').height = document.getElementById('height').value
    document.getElementById('img').width = document.getElementById('height').value * 1.5
    document.getElementById('width').value = document.getElementById('height').value * 1.5
}