function findTotal(){
    var arr = document.getElementsByClassName('eval0');
    var tot=0;
    for(var i=0;i<arr.length;i++){
        if(parseInt(arr[i].value))
            tot += parseInt(arr[i].value);
    }
    document.getElementById('Total').value = tot;
    console.log(arr);
}
