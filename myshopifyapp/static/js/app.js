actions.TitleBar.create(app, { title: '' });
$(document).ready(function() {
  
  
	$('#zohoForm').on('submit', function(e) {
	    
	    $('.pk_loader').show();
	    
	   e.preventDefault();
	    var getUrl = window.location;
        var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
	  
	
		$.ajax({
			url:   baseUrl + "/zoho/store",
			method: 'POST',
			data: $('#zohoForm').serialize(),
			success: function(response) {
			    $('.pk_loader').hide();
				if (response.error) {
					$("#alert_error").show();
					$("#error_message").text(response.error);
				} else {
					if(response.data){
						$("#alert_sucesss_error").show();
						$("#success_msg").text('Zoho Credentials Updated Successfully!');
					 }
				}
			},
			error: function(xhr, status, error) {
			     $('.pk_loader').hide();
					$("#alert_error").show();
					$("#error_message").text(error);
			}
		});
	});
	
	$('#zoho_setting_form').on('submit', function(e) {
	    
	   $('.pk_loader').show();
		e.preventDefault();
		
		 var getUrl = window.location;
        var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
 
		$.ajax({
			url: baseUrl + "/settings/store",
			method: 'POST',
			data: $('#zoho_setting_form').serialize(),
			dataType: 'json',
			success: function(response) {
			   $('.pk_loader').hide();
			  if(response.result == false){
			     $('#error_msg_id').show();
			     $('#error_msg').text(response.message);
			  }else{
			      $('#success_msg_id').show();
				  $('#success_msg').text(response.message);
			  }
				
				
			},
			error: function(xhr, status, error) {
			    $('.pk_loader').hide();
				alert('Error: ' + error);
			}
		});
	});
	
	$("#customer_table").DataTable();
	$('#zohoSyncForm').on('click', function(e) {
	    $('.pk_loader').show();
		e.preventDefault();
		var getUrl = window.location;
        var baseUrl = getUrl .protocol + "//" + getUrl.host + "/" + getUrl.pathname.split('/')[1];
		$.ajax({
			url: baseUrl +"/zoho/sync",
			method: 'POST',
			data: {sync:'manual'},
			success: function(response){
			    $('.pk_loader').hide();
				if(response == 200){
					$('#success_msg_id').show();
					$('#success_msg').text('Customers Exported Successfully to Zoho!');
				}
			},
			error: function(xhr, status, error){
			    $('.pk_loader').hide();
				alert('Error: ' + error);
			}
		});
	});
    
});
