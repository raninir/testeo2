$(function(){
    //sacar los mensajes de error
    $("erroremail").hide();
	$("errornombre").hide();
	$("errortelefono").hide();
	$("errorrun").hide();
	$("errorfecha").hide();
	$("errorvivienda").hide();
	$("errorciudad").hide();
	$("errorregion").hide();
    
    //variables que indican valor de estado validacion
    var error_nombre = false;
	var error_email = false;
	var error_telefono = false;
	var error_run = false;
    var error_fecha = false;
	var error_vivienda = false;
	var error_ciudad = false;
	var error_region = false;
	
	// se llama al error para checkearlos 
    $("#errornombre").focusout(function() {

		check_nombre();
		
	});
	
	 $("#errorciudad").focusout(function() {

		check_ciudad();
		
	});
	
	
	$("#errorregion").focusout(function() {

		check_region();
		
	});
	
	
	$("#errorvivienda").focusout(function() {

		check_vivienda();
		
	});
	
	
    $("#errorrun").focusout(function() {

		check_run();
		
	});
	
	$("#errortelefono").focusout(function() {

  	    check_telefono();
		
     });
		
	$("#erroremail").focusout(function() {

		check_email();
		
	});
	$("#errorfecha").focusout(function() {

		check_email();
		
	});
     
	 // Funcion para validar el nombre dandole un rango
	function check_nombre() {
	
		var username_length = $("#idnombre").val().length;
		
		if(username_length < 5 || username_length > 20) {
			$("#errornombre").html(" Debe tener entre 10 y 40 caracteres ");
			$("#errornombre").show();
			error_username = true;
		} else {
			$("#errornombre").hide();
		}
	
	}
    //funcion para validar el telefono donde se le da un rango 
	function check_telefono() {
	
		var telefono_length = $("#idtelefono").val().length;
		
		if(telefono_length < 9 || telefono_length > 9) {
			$("#errortelefono").html(" Debe tener 9 números ");
			$("#errortelefono").show();
			error_telefono = true;
		} else {
			$("#errortelefono").hide();
		}
	
	}
	//funcion para validar la fecha en donde se selecciona en recuadro y se compara con una variable 
	function check_fecha() {
	
      var patron=new RegExp("^(19|20)+([0-9]{2})([-])([0-9]{1,2})([-])([0-9]{1,2})$");
      var fecha = "2001";

      if ((patron.test($("#idfecha").val())) && ($("#idfecha").val() < fecha)) {
            $("#errorfecha").hide();
      } else {
      	 	$("#errorfecha").html("Debe ser anterior a 2001");
            $("#errorfecha").show();
            error_fecha = true;
      }
	
	}
	//funcion para validar el rut en donde se verifica el rango y verificar con letra k
   var Fn =  {
	validaRut : function (rutCompleto) {
		rutCompleto = rutCompleto.replace("-","-");
		if (!/^[0-9]+[-|-]{1}[0-9kK]{1}$/.test( rutCompleto ))
			return false;
		var tmp 	= rutCompleto.split('-');
		var digv	= tmp[1]; 
		var rut 	= tmp[0];
		if ( digv == 'K' ) digv = 'k' ;
		
		return (Fn.dv(rut) == digv );
	},
	dv : function(T){
		var M=0,S=1;
		for(;T;T=Math.floor(T/10))
			S=(S+T%10*(9-M++%6))%11;
		return S?S-1:'k';
	}
}

	//funcion en donde se verifica la vivienda en la cual se tiene que seleccionar una opcion 
	function check_vivienda() {

		if($("#Tipovivienda option:selected").val() == 0) {
    		$("#errorvivienda").html("Seleccione una categoria");
			$("#rrorvivienda").show();
			error_vivienda = true;
		} else {
			$("#errorvivienda").hide();
		}
	}
	//funcion en donde se verifica la region en la cual se tiene que seleccionar una opcion 
	function check_region() {

		if($("#Región option:selected").val() == 0) {
    		$("#errorregion").html("Seleccione una region");
			$("#rrorregion").show();
			error_region = true;
		} else {
			$("#errorregion").hide();
		}
	}
	//funcion en donde se verifica la ciudad en la cual se tiene que seleccionar una opcion 
	function check_ciudad() {

		if($("#Ciudad option:selected").val() == 0) {
    		$("#errorciudad").html("Seleccione una ciudad");
			$("#rrorciudad").show();
			error_vivienda = true;
		} else {
			$("#errorciudad").hide();
		}
	}
	
	//funcion en donde se verifica el email dando una variable para verificarlo 
	function check_email() {

		var pattern = new RegExp(/^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i);
	
		if(pattern.test($("#email").val())) {
			$("#erroremail").hide();
		} else {
			$("#erroremail").html("Direccion inválida");
			$("#erroremail").show();
			error_email = true;
		}
	
	}


	//Funcion para retornarl el error al boton
	$("#registration_form").submit(function() {
											
		error_nombre = false;
		error_email = false;
		error_telefono = false;
		error_run = false;
		error_fecha = false;
		error_vivienda = false ;
		error_ciudad = false;
		error_region = false ;
		//
		check_ciudad ();
		check_region ();
		check_vivienda();
		check_fecha();
		check_nombre();
		check_email();
		check_telefono();
		
		if (Fn.validaRut( $("#idrun").val() )){
		$("#errorrun").hide();
	} else {
		$("#errorrun").html("El Rut no es válido");
		$("#errorrun").show();
	}
     
		
		if(error_nombre == false && error_telefono == false && error_email == false && error_fecha == false && error_vivienda == false && error_region == false && error_ciudad == false)  {
			return true;
		} else {
			return false;	
		}

	});
    

});