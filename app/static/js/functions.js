function loadItems() {
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var myObj = JSON.parse(this.responseText);
      // Encontramos la tabla en el html que tenga como ID taulaItems
      var taula = document.getElementById("taulaItems");

      taula.innerHTML = "";
      // Para cada item en el archivo json, añade una fila y las propiedades de cada item (nombre, calidad, enlace, caducidad)
      for (let item in myObj.items) {
        var row = taula.insertRow(-1);
        
        var cell0 = row.insertCell(0);
        var cell1 = row.insertCell(1);
        var cell2 = row.insertCell(2);
        var cell3 = row.insertCell(3);
        var cell4 = row.insertCell(4);
        cell0.innerHTML = parseInt(item)+1;
        cell1.innerHTML = myObj.items[item].nombre;
        cell2.innerHTML = myObj.items[item].dias;
        cell3.innerHTML = myObj.items[item].calidad;
        cell4.innerHTML = '<a class="btn btn-primary" href="/producto" role="button">Ver producto</a';
      }
    }
  };
  // Abre la ruta /coger_items para después utilizar los datos con la funcion js.
  xmlhttp.open("GET", "/coger_items", true);
  xmlhttp.send();
}