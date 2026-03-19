function validarFormulario() {

let titulo = document.forms[0]["titulo"].value;
let autor = document.forms[0]["autor"].value;
let editora = document.forms[0]["editora"].value;
let ano = document.forms[0]["ano"].value;
let paginas = document.forms[0]["paginas"].value;
let categoria = document.forms[0]["categoria"].value;
let isbn = document.forms[0]["isbn"].value;
let idioma = document.forms[0]["idioma"].value;
let descricao = document.forms[0]["descricao"].value;
let cadastrado_por = document.forms[0]["cadastrado_por"].value;


if (titulo == "") {
alert("O título é obrigatório!");
return false;
}

if (autor == "") {
alert("O autor é obrigatório!");
return false;
}

if (editora == "") {
alert("A editora é obrigatória!");
return false;
}

if (ano == "" || isNaN(ano)) {
alert("Ano deve ser um número!");
return false;
}

if (paginas == "" || paginas <= 0) {
alert("Número de páginas deve ser maior que 0!");
return false;
}

if (categoria == "") {
alert("A categoria é obrigatória!");
return false;
}

if (isbn == "") {
alert("O ISBN é obrigatório!");
return false;
}

if (idioma == "") {
alert("O idioma é obrigatório!");
return false;
}

if (descricao == "") {
alert("A descrição é obrigatória!");
return false;
}

if (cadastrado_por == "") {
alert("Informe quem cadastrou o livro!");
return false;
}

return true;

}