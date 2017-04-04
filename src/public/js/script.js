//la requete ajax après le click de bouton qui affiche les résultat sur la page html

$(document).ready(function(){
  $("#rechercher").click(function(){

    var url =  window.location.href+"api/insta/" + $("#ville").val(); //+???
    console.log(url);
    $.ajax({
                url: url,
                dataType: 'json',
                success : function(data){
                  console.log(data);

                  //on créer une table avec les résultat de la requete et on l'ajoute à un div du html
                  var str = "<table>";
                  //!!!!
                  //problème au niveau de l'accès au données Json, peu etre pb de formatage de chaine sur le rest.
                  //!!!!
                  for(var obj in data){
                    str += "<tr><td>"+data[obj].name +"</td>";
                    str += "<td>"+data[obj].num +"</td>";
                    str += "</tr>";
                    //console.log(data.installations[obj].name);
                    console.log(data.installations);
                    console.log(data.installations.name);
                  }
                  //ajouter ligne par ligne (=parser le json), revoir les cours de js
                  str += "</table>";
                  //$("#reponse").html(data.installations)
                  $("#reponse").html(str)

                  //pour arreter la recherche à i fois. + mettre i en param
                  //if ( i == 5 ) return false;
                }
    });
  });
});
