$(document).ready(function(){ 
  $('#enviar').on('click',function(){
  	event.preventDefault();
  	/* String Ejerce Coach como Profesion Principal */
	    var boxes = document.getElementsByClassName('ejercecoach');
	    var checked = [];
	    for(var i=0; boxes[i]; ++i){
	      if(boxes[i].checked){
	        checked.push(boxes[i].name);
	      }
	    }
	    var ejercecoachStr = checked.join();
		document.getElementById('id_coaching_profesion_principal').value = ejercecoachStr;
  	
  	/* String  EJERCE EL COACHING COMO..  */
	    var boxes = document.getElementsByClassName('ejercecoachingcomo');
	    var otraopcion = document.getElementById('otroopcion');
	    var checked = [];
	    for(var i=0; boxes[i]; ++i){
	      if(boxes[i].checked){
	        checked.push(boxes[i].name);
	      }
	    }
	    if(otraopcion.checked){
	        checked.push($("#otrotexto1").val());
	    }

	    var ejercecoachStr = checked.join();
		document.getElementById('id_ejerce_coaching_como').value = ejercecoachStr;
 
  	/* String  SU DESEMPEÑO COMO COACH HA SIDO O ES A NIVEL DE:  */
	    var boxes = document.getElementsByClassName('cnivelde');
	    var otraopcion = document.getElementById('otro2');
	    var checked = [];
	    for(var i=0; boxes[i]; ++i){
	      if(boxes[i].checked){
	        checked.push(boxes[i].name);
	      }
	    }
	    if(otraopcion.checked){
	        checked.push($("#otrotexto2").val());
	    }

	    var ejercecoachStr = checked.join();
		document.getElementById('id_coach_a_nivel_de').value = ejercecoachStr;

  	/* String  DESEMPEÑA EL COACHING EN UN CAMPO ESPECÍFICO:  */
	    var boxes = document.getElementsByClassName('coachcampo');
	    var otraopcion = document.getElementById('otro3');
	    var checked = [];
	    for(var i=0; boxes[i]; ++i){
	      if(boxes[i].checked){
	        checked.push(boxes[i].name);
	      }
	    }
	    if(otraopcion.checked){
	        checked.push($("#otrotexto3").val());
	    }

	    var ejercecoachStr = checked.join();
		document.getElementById('id_campo_especifico').value = ejercecoachStr;
 
  	/* String  EJERCE EL COACHING DE MANERA:  */
	    var boxes = document.getElementsByClassName('coachmanera');
	    var otraopcion = document.getElementById('otro4');
	    var checked = [];
	    for(var i=0; boxes[i]; ++i){
	      if(boxes[i].checked){
	        checked.push(boxes[i].name);
	      }
	    }
	    if(otraopcion.checked){
	        checked.push($("#otrotexto4").val());
	    }

	    var ejercecoachStr = checked.join();
		document.getElementById('id_coaching_de_manera').value = ejercecoachStr;

  	/* String  CUENTA USTED CON PUBLICACIONES RELACIONADAS CON EL COACHING:  */
	    var boxes = document.getElementsByClassName('publicaciones');
	    var otraopcion = document.getElementById('otro5');
	    var checked = [];
	    for(var i=0; boxes[i]; ++i){
	      if(boxes[i].checked){
	        checked.push(boxes[i].name);
	      }
	    }
	    if(otraopcion.checked){
	        checked.push($("#otrotexto5").val());
	    }

	    var ejercecoachStr = checked.join();
		document.getElementById('id_publicaciones_relacionadas').value = ejercecoachStr;

  	/* String IDENTIFIQUE LO QUE DESEARÍA QUE LA CIC LE OFRECIERA A USTED COMO MIEMBRO:  */
	    var boxes = document.getElementsByClassName('comomiembrocic');
	    var otraopcion = document.getElementById('otro7');
	    var checked = [];
	    for(var i=0; boxes[i]; ++i){
	      if(boxes[i].checked){
	        checked.push(boxes[i].name);
	      }
	    }
	    if(otraopcion.checked){
	        checked.push($("#otrotexto7").val());
	    }

	    var ejercecoachStr = checked.join();
		document.getElementById('id_que_desea_delacic').value = ejercecoachStr;


  	var form = document.getElementById('registroform');
    form.submit();
        });

  $('#otroopcion').on('click',function(){
  	var opcion = document.getElementById('otroopcion');
  		if(opcion.checked){
  			$('#otrotexto1').removeClass('notShow');
  			$('.especifique').removeClass('notShow');
	      }
	    else{
	    	$('#otrotexto1').addClass('notShow');
	    	$('.especifique').addClass('notShow');
	    }
        }); 

  $('#otro2').on('click',function(){
  	var opcion = document.getElementById('otro2');
  		if(opcion.checked){
  			$('#otrotexto2').removeClass('notShow');
  			$('.especifique2').removeClass('notShow');
	      }
	    else{
	    	$('#otrotexto2').addClass('notShow');
	    	$('.especifique2').addClass('notShow');
	    }
        });   

  $('#otro3').on('click',function(){
  	var opcion = document.getElementById('otro3');
  		if(opcion.checked){
  			$('#otrotexto3').removeClass('notShow');
  			$('.especifique3').removeClass('notShow');
	      }
	    else{
	    	$('#otrotexto3').addClass('notShow');
	    	$('.especifique3').addClass('notShow');
	    }
        }); 
  $('#otro4').on('click',function(){
  	var opcion = document.getElementById('otro4');
  		if(opcion.checked){
  			$('#otrotexto4').removeClass('notShow');
  			$('.especifique4').removeClass('notShow');
	      }
	    else{
	    	$('#otrotexto4').addClass('notShow');
	    	$('.especifique4').addClass('notShow');
	    }
        });   
  $('#otro5').on('click',function(){
  	var opcion = document.getElementById('otro5');
  		if(opcion.checked){
  			$('#otrotexto5').removeClass('notShow');
  			$('.especifique5').removeClass('notShow');
	      }
	    else{
	    	$('#otrotexto5').addClass('notShow');
	    	$('.especifique5').addClass('notShow');
	    }
        });

  $('#otro7').on('click',function(){
  	var opcion = document.getElementById('otro7');
  		if(opcion.checked){
  			$('#otrotexto7').removeClass('notShow');
  			$('.especifique7').removeClass('notShow');
	      }
	    else{
	    	$('#otrotexto7').addClass('notShow');
	    	$('.especifique7').addClass('notShow');
	    }
        }); 

/* SI O NO DE OTRA CERTIFICACION CIC */

  $('#sipublicacion').on('click',function(){
  	$('.coachingpublicaciones').removeClass('notShow');
        });
  $('#nopublicacion').on('click',function(){
  	$('.coachingpublicaciones').addClass('notShow');
        });
   $('#sievento').on('click',function(){
  	$('.eventodescripcion').removeClass('notShow');
        });
  $('#noevento').on('click',function(){
  	$('.eventodescripcion').addClass('notShow');
        });
        });